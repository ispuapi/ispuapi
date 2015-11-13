#!/usr/bin/python

'''
 ISPUAPI (ISPU+API)
 Appliaction Programming Interface
 for PM10 data retreival on current location in Indonesia
 it is defaultly retreive data for Pekanbaru
 data retreival for other locations is still under development

 maintained by @vickydasta

 http://vickydasta.github.io/ispuapi
 http://infoispu.id/api
 see LICENSE
'''

__author__ = 'vickydasta'
__mail__ = 'vickydasta@ksl-ur.or.id'
__version__ = '2.1-beta'

# default python modules

import urllib2
import re
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError('bs4 is not installed')

# ispuapi modules

try:
    import cleaner
except ImportError:
    raise ImportError('ispuapi modules are not installed properly!')
    sys.exit(0)

URLS = { 'aqicn' : 'http://aqicn.org/city/indonesia/' ,
        'bmkg': 'http://www.bmkg.go.id/BMKG_Pusat/Kualitas_Udara/Informasi_Partikulat.bmkg'}

db_kota = ['pekanbaru',
           'jambi',
           'palembang',
           'pontianak',
           'banjarbaru',
           'samarinda',
           'palangkaraya',
           'batam']

# parsing function for ispuapi
# we make our own!

def getdataispu(data):

    data_fix = []

    for batas in range(0, len(data), 5):

        if batas > 10:
            data_fix.append(float(data[batas]))

    return data_fix


def CityCodeToName(kota):

    kota = kota.lower()

    if kota == 'pku':
        name = 'Pekanbaru'
    elif kota == 'jb':
        name = 'Jambi'

    elif kota == 'plb':
        name = 'Palembang'

    elif kota == 'plk':
        name = 'Palangkaraya'

    elif kota == 'pnt':
        name = 'Pontianak'

    elif kota == 'bjb':
        name = 'Banjarbaru'

    return name


def getupdate(data):

    """
    get the latest update
    """
    return data[-1]


def valid(sign, data):

    '''
    check for data validity the index[x] of the scrapped data
    is alwaysly changes by the host and it's affects the parsed data
    when aqi(citycode) called.
    '''

    if re.findall(sign, data) > 0:
        valid = True
    else:
        valid = False
    return valid


def getpm10(lokasi, data):
    '''
    fungsi untuk mendapatkan data ispu berdasarkan daerah dari halaman html
    (urllib2.urlopen(url))

    >>> datapku = getdata('pku', ispuapi.getdatabmkg())
    '''

    lok = CityCodeToName(lokasi.lower())

    if lok == 'pku' or lok == 'pekanbaru':
        try:
            if valid(lok, data[39]):
                val = data[39]
            else:
                val = None
        except IndexError:
            val = None

    elif lok == 'jambi' or lok == 'jb':
        try:
            if valid(lokasi, data[51]):
                val = data[51]
            else:
                val = None
        except IndexError:
            val = None

    elif lok == 'plb' or lok == 'palembang':
        try:
            if valid(lok, data[63]):
                val = data[63]
            else:
                val = None
        except IndexError:
            val = None

    elif lok == 'pnt' or lok == 'pontianak':
        try:

            if valid(lok, data[74]):
                val = data[74]
            else:
                val = None
        except IndexError:
            val = None

    elif lok == 'bjb' or lok == 'banjarbaru':
        try:
            if valid(lok, data[86]):
                val =  data[86]
            else:
                val = None
        except IndexError:
            val = None

    elif lok == 'smr' or lok == 'samarinda':
        try:
            if valid(data[109]):
                val = data[109]
            else:
                val = None
        except IndexError:
            val = None

    elif lok == 'plk' or lok == 'palangkaraya':
        try:
            if valid(lok, data[112]):
                val = data[112]
            else:
                val = None
        except IndexError:
            val = None

    else:
        val = None

    return val


def kategori(aqi):
    '''
    AQI Value to Quality based on given PM10 value
    the value is in float
    '''

    if aqi >= 0 and aqi <= 50:
        status = "BAIK"

    elif aqi >= 51 and aqi <= 150:
        status = "SEDANG"

    elif aqi >= 151 and aqi <= 250:
        status = "TIDAK SEHAT"

    elif aqi >= 251 and aqi <= 350:
        status =  "SANGAT TIDAK SEHAT"
    elif aqi > 350:
        status = "BERBAHAYA"

    return status



def getsoup(url):

    '''
    GET SOUP OBJECT

    >>> BeatifulSoup(urllib2.urlopen(url))
    >>> getsoup(url)

    the above function are the same
    '''

    try:
        soup =  BeautifulSoup(urllib2.urlopen(url))
    except Exception as e:
        raise Exception(str(e))
        return 0

    return soup

def getdata(url):


    """
    RETREIVE ALL ELEMENTS OF WEBPAGE WHICH CONTAINS
    NEEDED INFORMATIONS

    >>> from ispuapi import getdata
    >>> getdata(URLS['bmkg'])
    >>> data = {'bmkg': data_html}
    >>> clean_data = data['bmkg']
    >>> clean_data

    """


    # after some moments of research
    # we are concludes that the targets location are not based on the div
    # <div> tags are the same on every targets

    try:

        if url.lower().startswith('http://aqicn.org') or url.lower().startswith('http://www.aqicn.org'):

            soup =  getsoup(URLS['aqicn'])

            parse_data = soup.find_all("div", {"class" : 'class="modal fade modal-pekanbaru"'})

            data_clean = [tag.text for tag in soup.find_all('div')]

            data = {'aqicn':data_clean}

        elif url.lower().startswith('http://bmkg.go.id') or url.lower().startswith('http://www.bmkg.go.id'):

            soup =  getsoup(URLS['bmkg'])

            parse_data = soup.find_all("div", {"class" : 'class="modal fade modal-pekanbaru"'})

            data_clean = [tag.text for tag in soup.find_all('div')]

            data = {'bmkg':data_clean}

        else:

            raise ValueError('unable to fetch data from %s'%url)
            return 0

    except Exception as e:
        raise Exception(str(e))
        return 0

    return data


def aqi(daerah):

    """"
    main function for cleaning all garbages and
    collect clean informations
    """

    try:

        data = getdataispu(cleaner.tolatin1(cleaner.removegarbage(getpm10(daerah, getdata(URLS['bmkg'])['bmkg']))).split())

    except Exception as e:

        raise Exception(e)
        return 0

    return data
