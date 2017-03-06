#!/usr/bin/env python
#coding:utf-8

import MySQLdb,sys
sql=sys.argv[1]
  
def select_mysql(sql):
	conn = MySQLdb.connect(host='10.0.0.86',user='trans_data',passwd='trans_data1234',db='trans_data')

  

	cur = conn.cursor()
	if 'selectr43t43t5454t54ty54t45t4t' in sql:
		tables=sql.split()[3]
		reCount = cur.execute('desc %s'%tables)
		nRet = cur.fetchall()
		colmur=''
		for i in nRet:
			data=''
			for j in xrange(0,len(i)):
				data+='|%s'%i[j]
			#print data.split('|')[1]
			colmur=colmur+'| %s '%data.split('|')[1]
		print colmur

	cur = conn.cursor()
	reCount = cur.execute(sql)

	nRet = cur.fetchall()
	for i in nRet:
		data=''
		for j in xrange(0,len(i)):
			data+='|  %s '%i[j]
		print data
	cur.close()

	conn.close()
select_mysql(sql)
'''
while True:
	sql =raw_input("mysql_cmd:>")
	if not sql:
		continue
	if 'exit' in sql:
		sys.exit('exit mysql !')
	select_mysql(sql)
'''
