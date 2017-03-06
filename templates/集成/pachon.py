import requests,re,pymysql,time
date = time.strftime('%Y-%m-%d')
def insert_mysql(sql):
    conn = pymysql.connect(host='121.201.68.21', port=3307, user='jiang', passwd='jiangwenhui', db='daxiangzhanshi',
                           charset='UTF8')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    for i in cur:
        print(i)

    cur.close()
    conn.close()

ret = requests.get('http://120.76.65.147:5000/ip')
data=re.findall('''<div id="menu" style="height:750px;width:200px;float:left;">(.*?)</div>''',ret.text)
djcs=re.findall(">(.*?),(.*?)<",data[0])
print(data[1])
insert_mysql("delete from app01_the_number_of_clicks")
for i in djcs:
    sql="insert into app01_the_number_of_clicks values (null,'%s','%s','%s')"%(i[0],i[1],date)
    insert_mysql(sql)
    print(sql)

source_ip=re.findall(">(.*?),(.*?)<",data[1])
insert_mysql("delete from app01_source_ip")
for i in source_ip:
    sql="insert into app01_source_ip values (null,'%s','%s','%s')"%(i[0],i[1],date)
    insert_mysql(sql)
    print(sql)