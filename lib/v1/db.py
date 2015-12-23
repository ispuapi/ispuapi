#!/usr/bin/python

import MySQLdb as mdb
import ispuapi as api
import sys
from time import sleep
from time import strftime
import brain

'''
database-thing for ispubot

www.infoispu.org/<kodekota>
www.infoispu.org/<pku>

example:

Setup
>> import enginx
>> dbinfo = setup(hostname, username, password, database)
>> db = enginx.setup('127.0.0.1','root','toor','botdata')

Connect to MySQL database
>> con = mdb.connect(dbinfo.gethost(), dbinfo.getusername(), dbinfo.getpwd(), dbinfo.getdb);
>> enginx.insert('1')
>> True
'''

host = '127.0.0.1'
username = 'ispubot'
password = 'toor'
db = 'ispubot'

class setup:
    def __init__(self, host, username, password, db):
        self.host = host
        self.username = username
        self.password = password
        self.db = db

    def gethost(self):
        return self.host

    def getusername(self):
        return self.username

    def getpwd(self):
        return self.password

    def getdb(self):
        return self.db

dbinfo = setup(host, username, password, db)

try:
    print 'connecting to %s'%dbinfo.getdb()
    con = mdb.connect(dbinfo.gethost(), dbinfo.getusername(), dbinfo.getpwd(), dbinfo.getdb());
    cur = con.cursor()
    print 'connected to %s'%dbinfo.getdb()
except Exception:
    raise Exception('cannot connect to database %s'%dbinfo.getdb)

def insert(data):
    try:
        cur.execute("INSERT INTO `ispu` (`id`, `pm10`, `time`) VALUES (NULL, {}, NOW());".format(data))
        con.commit()
        print data
        return True
    except Exception as e:
        raise Exception('cannot perform data insert to %s'%dbinfo.getdb())
        print e

def delete(data):
    pass

def getdata():
    data = cur.execute("SELECT * FROM `ispu`;")

def main():
    while True:
        print insert(api.aqi('pku')[-1])
        print '[%s] data updated...'%strftime("%H:%M:%S %m-%d")
        sleep(60)

if __name__ == '__main__':
    main()
