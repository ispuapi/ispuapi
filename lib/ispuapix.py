#!/usr/bin/python
# ISPUAPI
# Appliaction Programming Interface untuk data retreival perival ISPU/AQI
# AQI/ISPU related data from hosts/web services
# current web host/services are
# Daerah target data:
# Pekanbaru
# Jambi
# Palembang
# Pontianak
# Banjarbaru
# Samarinda
# Palangkaraya
# BMKG (bmkg.go.id)
# AQICN (aqicn.org)
# Badan Lingkungan Hidup Kota Pekanbaru (blh.pekanbaru.go.id)
# http://vickydasta.github.io/ispuapi
# http://vickydasta.github.io/ispubot
# see LICENSE

__author__ = "vickydasta"

'''
The MIT License (MIT)
Copyright (c) 2015 Vicky Vernando Dasta
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE

'''


import urllib2
import re
from bs4 import BeautifulSoup

class kb:
    # basis pengetahuan
    aqicn = 'http://aqicn.org/city/indonesia/'
    bmkg = 'http://www.bmkg.go.id/BMKG_Pusat/Kualitas_Udara/Informasi_Partikulat.bmkg'
    db_kota = ['pekanbaru', 'jambi','palembang', 'pontianak','banjarbaru','samarinda','palangkaraya']

def getsoup(url):
    return BeautifulSoup(urllib2.urlopen(url))

def getDataAqi(daerah):
    if daerah.lower() not in kb.db_kota:
        raise Exception('data %s tidak ditemukan di basis pengetahuan'%daerah)
    soup = getsoup(kb.aqicn+daerah)
    parse_data = soup.find_all("td", {"id" : re.compile('^cur_')})
    data_clean = [tag.text for tag in soup.find_all("td")]
    if len(data_clean) <= 34:
        raise Exception('data %s tidak ditemukan di database aqicn.org'%daerah)
    return data_clean

def getdataaqi(daerah):
    soup = BeautifulSoup(urllib2.urlopen('http://aqicn.org/city/indonesia/'+daerah))
    parse_data = soup.find_all("td", {"id" : re.compile('^cur_')})
    data_clean = [tag.text for tag in soup.find_all("td")]
    if len(data_clean) <= 34:
        raise Exception("%s not exists on aqicn.org database!"%daerah)
    return data_clean

def getdatabmkg():
    soup =  BeautifulSoup(urllib2.urlopen('http://www.bmkg.go.id/BMKG_Pusat/Kualitas_Udara/Informasi_Partikulat.bmkg'))
    parse_data = soup.find_all("div", {"class" : 'class="modal fade modal-pekanbaru"'})
    data_clean = [tag.text for tag in soup.find_all('div')]
    return data_clean

def getdatablh():
    soup = BeautifulSoup(urllib2.urlopen('http://www.blh.pekanbaru.go.id/index.php'))
    parse_data = soup.find_all("td", {"id" : re.compile('^span')})
    data_clean = [tag.text for tag in soup.find_all("td")]
    return data_clean
