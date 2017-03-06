#!/usr/bin/env python
#coding:utf-8
import pymysql,time,datetime
ltime=time.localtime(time.time()-300)
print(time.time()-300)
datestrftime=time.strftime('%Y-%m-%d %H:%M:%S',ltime)
print(datestrftime)

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

    select = "SELECT SUM(value),itemid FROM zabbix.history_uint WHERE   clock>=%s and itemid in (35529,35528,35526,36052) group by itemid"%(time.time()-300)
    data = select_mysql(select)
    itemname={35529:'生活馆',35528:'电商',35526:'SSO',36052:'.NET'}
    for i in data:
        num=int(datestrftime[-4])
        if num>5:
            num=5
        elif num<5:
            num=0

        insert="insert into app01_business_real_time_access values (null,'%s','%s','%s%s',curdate())"%(itemname[i[1]],i[0],datestrftime[11:-4],num)
        end='{}{}'.format(datestrftime[11:-4],num)
        if end=='23:55':
            insert=insert.replace("curdate()","curdate()-1")
        insert_mysql(insert)
        #print(insert)