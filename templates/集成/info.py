#coding:utf-8
import json,re,pymysql

conn = pymysql.connect(host='mysql.litianqiang.com', port=7150, user='xiaoshuo', passwd='qiangzi()', db='xiaoshuo',
                       charset='UTF8')
cur = conn.cursor()
#cur.execute("select app01_commodity_categories.name,sum(total_rmb) from app01_commodity_subclass,app01_commodity_categories where categories_id=Commodity_categories_id group by app01_commodity_categories.name order by Commodity_categories_id")



with open("1.txt",encoding='utf8') as f:
    for i in f:
        if  len(i.strip())==0:
            continue
        data=re.findall("""\{name: '(.*?)', value: (.*?)\}""",i)
        print(data[0])
        cur.execute("insert into app01_city_trading_volume VALUES ('','%s','%s','%s')"%(data[0][0],data[0][1],'2018-01-01'))
conn.commit()
cur.close()
conn.close()