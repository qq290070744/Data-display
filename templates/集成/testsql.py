import pymysql

conn = pymysql.connect(host='121.201.68.21', port=3307, user='jiang', passwd='jiangwenhui', db='jiang', charset='UTF8')
cur = conn.cursor()
cur.execute("select version()")
conn.commit()
for i in cur:
    print(i)

cur.close()
conn.close()
