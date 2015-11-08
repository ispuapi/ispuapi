#!/usr/bin/python

'''
 ISPUAPI (ISPU+API)
 Appliaction Programming Interface
 for PM10 data retreival on current location in Indonesia
 it is defaultly retreive data for Pekanbaru
 data retreival for other locations is still under development


 http://vickydasta.github.io/ispuapi
 http://infoispu.id/api
 see LICENSE
'''

__author__ = 'vickydasta'
__mail__ = 'vickydasta@ksl-ur.or.id'
__version__ = '1.5'


# default python modules

import urllib2
import re
from bs4 import BeautifulSoup
import sys

# ispuapi modules

try:
    import brain.brain as brain
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



def getdataispu(data):

    data_fix = []

    for batas in range(0, len(data), 5):

        if batas > 10:
            data_fix.append(float(data[batas]))

    return data_fix



def getpm10(lokasi, data):
    '''
    fungsi untuk mendapatkan data ispu berdasarkan daerah dari halaman html
    (urllib2.urlopen(url))

    >>> datapku = getdata('pku', ispuapi.getdatabmkg())
    '''

    lok = lokasi.lower()

    if lok == 'pku' or lok == 'pekanbaru':

        try:
            val = data[39]
        except IndexError:
            raise IndexError('tidak dapat mengekstrak data dari bmkg')

    elif lok == 'jambi' or lok == 'jb':
        try:
            val = data[51]

        except IndexError:
            raise IndexError('%s tidak terdaftar dalam basis pengetahuan'%lok)

    elif lok == 'plb' or lok == 'palembang':
        try:
            val = data[63]
        except IndexError:
            raise IndexError('%s tidak terdaftar dalam basis pengetahuan'%lok)

    elif lok == 'pnt' or lok == 'pontianak':
        try:
            val = data[74]
        except IndexError:
            raise IndexError('%s tidak terdaftar dalam basis pengetahuan'%lok)

    elif lok == 'bjb' or lok == 'banjarbaru':
        try:
            val = data[86]
        except IndexError:
            raise IndexError('%s tidak terdaftar dalam basis pengetahuan'%lok)

    elif lok == 'smr' or lok == 'samarinda':
        try:
            val = data[109]
        except IndexError:
            raise IndexError('%s tidak terdaftar dalam basis pengetahuan'%lok)

    elif lok == 'plk' or lok == 'palangkaraya':
        try:
            val = data[112]
        except IndexError:
            raise IndexError('%s tidak terdaftar dalam basis pengetahuan'%lok)

    else:
        raise Exception('%s tidak ada dalam basis pengetahuan!'%lok)

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

            soup =  getsoup(url)

            parse_data = soup.find_all("div", {"class" : 'class="modal fade modal-pekanbaru"'})

            data_clean = [tag.text for tag in soup.find_all('div')]

            data = {'aqicn':data_clean}

        elif url.lower().startswith('http://bmkg.go.id') or url.lower().startswith('http://www.bmkg.go.id'):

            soup =  getsoup(url)

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


def kotasigntoword(kota):

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

def main():
    import matplotlib.pyplot as plt
    plt.plot(aqi('pku'))
    plt.xlabel('waktu')
    plt.ylabel('Tingkat PM10')
    plt.show()

if __name__ == '__main__':
    print 'running test'
    main()
