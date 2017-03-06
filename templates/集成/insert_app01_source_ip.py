#!/usr/bin/rnv python
#:coding:utf-8
import pymysql, sys,time,datetime
date = float(time.time())-86400
ltime=time.localtime(date)
timeStr = time.strftime("%Y%m%d", ltime)
datestrftime=time.strftime('%Y-%m-%d',ltime)

# sql=sys.argv[1]

def select_mysql(sql):
    conn = pymysql.connect(host='120.76.65.147', user='jiang', passwd='Jiangwenhui1@3', db='ipStatic',
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

    select = "select count(*) as counts,province from ha_ip_%s group by province order by counts desc"%(timeStr)
    data = select_mysql(select)

    for i in data:
        insert="insert into app01_source_ip values (null,'%s','%s','%s')"%(i[1],i[0],datestrftime)
        insert_mysql(insert)
        print(insert)