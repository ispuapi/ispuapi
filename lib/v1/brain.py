#!/usr/bin/python
# sistem kontrol bot
# bot bekerja secara autonomous
# tanpa ada interfensi dari siapapun kecuali dalam
# proses start-end system
# http://vickydasta.github.io/ispubot
# http://vickydasta.github.io/ispuapi
# LICENSE: SEE LICENSE


__author__ = "vickydasta"
__about__ = "ispubot brain"


class kb:
    ConsumerKey = "mDqDZ2UNT7MvPu2qYLVi6ExVv"
    ConsumerSecret = "nZnYvZaKCFTw0hX2c8EafRDAkrEV13sNDJSkkcsPQKkcDmHBVW"
    AccesToken = "4007689573-WE5eJBT0vdU8pZ5hel6Kqm91uM6xtdRfIcbK5HX"
    AccesTokenSec = "48kgPuBsersOv3G7qXg6yMN91PYfuv6JOiBkEX7ZC8BxI"


def kategori(aqi):
    '''
    AQI Value to Quality based on
    '''
    if aqi >= 0 and aqi <= 50:
        status = "BAIK"
    elif aqi >= 51 and aqi <= 150:
        status = "SEDANG"
    elif aqi >= 151 and aqi <= 250:
        status = "TIDAK SEHAT"
    elif aqi >= 251 and aqi <= 350:
        status =  "SANGAT TIDAK SEHAT"
    else:
        status = "BERBAHAYA"

    return status

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
    return data[-1]

def getdata(lokasi, data):
    '''
    fungsi untuk mendapatkan data ispu berdasarkan daerah dari halaman html
    (urllib2.urlopen(url))
    >> datapku = getdata('pku', ispuapi.getdatabmkg())
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
            val = data[102]
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


def getdataispu(data):
    data_fix = []
    for batas in range(0, len(data), 5):
        if batas > 10:
            data_fix.append(float(data[batas]))
    return data_fix



def starttwitterbot(data):
    print '[{}] Memulai sistem twitterbot pada: '.format(strftime("%Y-%m-%d %H:%M:%S"))
    Status = str(strftime("%H:%M:%S %m-%d")) + " LEVEL AQI: "+ data + " STATUS: "+ categorize(data)
    t.statuses.update(status="Status indeks polusi udara pd : "+ Status + " #HAZE #ASAP #HACKERMELAWANASAP #HACKATHONMERDEKA" )
    print '[{}] Kicaiaun AQI {} Terkirim'.format(strftime("%Y-%m-%d %H:%M:%S"), strftime("%H:%M:%S") )
