#!/usr/bin/python

import ispuapi
import brain
import cleaner

# tweet(aqi(daerah))
# telegram(aqi(daerah))

def aqi(daerah):
    datapku = brain.getdata(daerah, ispuapi.getdatabmkg())
    data_clean = cleaner.tolatin1(cleaner.removegarbage(datapku))
    dataispu = brain.getdataispu(data_clean.split())
    return dataispu

def getdataplb():
    datapku = brain.getdata('pku', ispuapi.getdatabmkg())
    data_clean = cleaner.tolatin1(cleaner.removegarbage(datapku))
    dataipsu = brain.getdataispu(data_clean.split())
