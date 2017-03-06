#!/usr/bin/env python
# coding:utf-8

import MySQLdb, sys


# sql=sys.argv[1]

def select_mysql(sql):
    conn = MySQLdb.connect(host='10.0.0.86', user='trans_data', passwd='trans_data1234', db='trans_data',
                           charset='UTF8')

    cur = conn.cursor()
    reCount = cur.execute(sql)

    nRet = cur.fetchall()
    cur.close()

    conn.close()
    return nRet


def insert_mysql(sql):
    conn = MySQLdb.connect(host='mysql.litianqiang.com', port=7150, user='xiaoshuo', passwd='qiangzi()', db='xiaoshuo',

                           charset='UTF8')

    cur = conn.cursor()

    cur.execute(sql)
    nRet = cur.fetchall()
    conn.commit()

    cur.close()

    conn.close()
    return nRet

if __name__ == "__main__":
    select_ls_category = "select sub_count,total,left(right(time_,8),5),time_ from sub_realtime  where time_>curdate() order by time_ desc limit 1"
    data = select_mysql(select_ls_category)
    for i in data:
        insert_ls_category = '''insert into app01_real (numner,rmb,time,updatetime) values (%s,%s,'%s','%s') '''%(i[0],i[1],i[2],i[3])
        if not insert_mysql("select * from app01_real where updatetime='%s'"%i[3]):
            insert_mysql(insert_ls_category)
            print(insert_ls_category)