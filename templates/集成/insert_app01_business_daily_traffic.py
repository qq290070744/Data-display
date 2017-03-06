#!/usr/bin/env python
#coding:utf-8
import pymysql,time,datetime

date = time.strftime('%Y-%m-%d')
time.strptime(date, '%Y-%m-%d')
j=time.mktime(time.strptime(date,'%Y-%m-%d'))
z=float(j)-86400
day=86400*11

ltime=time.localtime(z-day)
timeStr = time.strftime("%Y%m%d", ltime)
datestrftime=time.strftime('%Y-%m-%d',ltime)

def select_mysql(sql):
    conn = pymysql.connect(host='120.76.65.147', user='jiang', passwd='Jiangwenhui1@3', db='zabbix',
                           charset='UTF8')

    cur = conn.cursor()
    reCount = cur.execute(sql)

    nRet = cur.fetchall()
    cur.close()

    conn.close()
    return nRet


def insert_mysql(sql):
    conn = pymysql.connect(host='121.201.68.21', port=3307, user='jiang', passwd='jiangwenhui', db='daxiangzhanshi',

                           charset='UTF8')

    cur = conn.cursor()

    cur.execute(sql)
    nRet = cur.fetchall()
    conn.commit()

    cur.close()

    conn.close()
    return nRet

if __name__ == "__main__":

    select = "SELECT SUM(value),itemid FROM zabbix.history_uint WHERE  clock < %s and clock>=%s and itemid in (35529,35528,35526,36052) group by itemid"%(float(j)-day ,float(z)-day)
    data = select_mysql(select)
    itemname={35529:'生活馆',35528:'电商',35526:'SSO',36052:'.NET'}
    for i in data:
        #print(itemname[i[1]],i[0],'curdate()',datestrftime)
        insert="insert into app01_business_daily_traffic values (null,'%s','%s',curdate(),'%s')"%(itemname[i[1]],i[0],datestrftime)
        insert_mysql(insert)
        print(insert)
