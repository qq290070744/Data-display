#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import datetime
import time
import os
import sys
from flask import Flask,render_template,url_for
app = Flask(__name__)
reload(sys)
sys.setdefaultencoding( "utf-8" )

def connMySQL_insert(sql,args):
        try:
            conn=MySQLdb.connect(host='10.0.0.86',user='trans_data',passwd='trans_data1234',db='trans_data',port=3306,charset='utf8')
            cur=conn.cursor()
            cur.execute(sql % args)
            #cur.execute('commit')
            #cur.execute('flush privileges')
            results = cur.fetchall()
            return results
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
             print "Mysql Error %d: %s" % (e.args[0], e.args[1])

class Categories:
	'大类'
	def __init__(self, cate='', data='', data_addup=0):
		self.cate = cate
		self.data = data
		self.data_addup = data_addup

	def displayCate(self):
		return self.cate
		#print self.cate

	def displayData(self):
		return self.data
		#print self.data
	def displayData_addup(self):
		return self.data_addup

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/pie')
def realtime():
        return render_template('pie.html', categories = categories, str1 = str1, str2=str2, y=y[0],c=c[0],d=d[0], y1=y[1],c1=c[1],d1=d[1], y2=y[2],c2=c[2],d2=d[2], y3=y[3],c3=c[3],d3=d[3], y4=y[4],c4=c[4],d4=d[4], y5=y[5],c5=c[5],d5=d[5], y6=y[6],c6=c[6],d6=d[6], y7=y[7],c7=c[7],d7=d[7], y8=y[8],c8=c[8],d8=d[8], y9=y[9],c9=c[9],d9=d[9], y10=y[10],c10=c[10],d10=d[10])


if __name__ == '__main__':
	str1 = ''
	str2 = ''
	time1 = datetime.datetime.now()
        print str(time1)[:19]
        time_ = str(time1)[:10] + ' 00:00:00'

	sql_0 = 'select sum(total) from sub_category where time_ >= "%s"'
	total = connMySQL_insert(sql_0,time_)
	sum_ = total[0][0]
	#print sum_

	top = 0
	categories = '['
	cate_id = []
	dict_data = {}
	dict_cate_per = {}
	sql_1 = 'select sum(s.total) as zong, l.name, s.cate_id from sub_category  s inner join ls_category  l on s.`cate_id`=l.`id` where time_ >= "%s" group by cate_id order by zong desc limit 10'
	info = connMySQL_insert(sql_1,time_)
	#print info
	for i in info:
		per = float(str(int(i[0])/sum_)[:6])*100
		#print i[1], i[0], str(per)+'%'#, i[2]
		str1 += str(i[1])+','+ str(i[0])+','+str(per)+'%<br/>'#, i[2]
		top += int(i[0])
		categories += '"'+i[1]+'",'
		#list_data.append(str(per)[:5])
		cate_id.append(i[2])
		dict_cate_per[i[2]] = per
		dict_data[i[2]] = i[0]

	other = int(sum_) - top
	#print '其他', other, float(str(other/sum_)[:6])*100
	dict_cate_per[0] = float(str(other/sum_)[:6])*100
	cate_id.append(0)

	#print cate_id
	print '+++++++++'
	categories = categories + '"其他"]'
	#print categories

	#list_data.append(str(float(str(other/sum_)[:6])*100)[:5])
	#print list_data


	list_pid = []
	sql_3 = 'select sum(s.total) as zong,s.cate_id,l.name,l.parent_id,c2.name from sub_category_det s inner join ls_category  l on s.`cate_id`=l.`id` INNER JOIN ls_category c2 on c2.id=l.parent_id  where time_ >= "%s" group by cate_id order by zong desc limit 20'
	info = connMySQL_insert(sql_3,time_)
	for i in info:
		#print i[2],i[0],str(100 * float(i[0])/float(sum_))[:5]+'%',i[4]
		str2 += str(i[2])+','+str(i[0])+','+str(100 * float(i[0])/float(sum_))[:5]+'%,'+str(i[4])+'<br/>'
		list_pid.append(i[3])

	dict_cate = {}
	list_pid = list(set(list_pid))
	for i in list_pid:
		dict_cate[i] = Categories('[','[')
	#print dict_cate

	print '================'
	for i in info:
		cate = dict_cate[i[3]].displayCate() + '"' +  str(i[2]) + '",'
		data = dict_cate[i[3]].displayData() + str(100 * float(i[0])/float(sum_))[:5] + ','
		data_addup = dict_cate[i[3]].displayData_addup() + i[0]
		dict_cate[i[3]] = Categories(cate,data,data_addup)
	
	for k,v in dict_cate.items():
		#print k
		cate = v.displayCate() + '"other"]' 
		if dict_data.has_key(k):
			other_data = float(dict_data[k] - v.displayData_addup())/sum_
			data = v.displayData() + str(other_data * 100)[:5]+']'
			#print k,other_data
		else:
			data = v.displayData() + ']'
		dict_cate[k] = Categories(cate,data)


	"""
	for i in range(len(cate_id)):
		i = cate_id[i]
		if dict_cate.has_key(i):
			print dict_cate_per[i],dict_cate[i].displayCate()
		else:print i,dict_cate_per[i]
	"""

	count_cate = len(cate_id)
	y = []
	c = []
	d = []
	for i in range(11):
		y.append(0)
		c.append('[]')
		d.append('[]')

	for i in range(count_cate):
		c_id = cate_id[i]
		y[i] = dict_cate_per[c_id]
		if not y[i]:
			y[i] = 0
		if dict_cate.has_key(c_id):
                	c[i] = dict_cate[c_id].displayCate()
                	d[i] = dict_cate[c_id].displayData()
        	else:
                	c[i] = '[]'
                	d[i] = '[]'


	"""
	c_id = cate_id[0]
	y = dict_cate_per[c_id]
	if dict_cate.has_key(c_id):
		c = dict_cate[c_id].displayCate()
		d = dict_cate[c_id].displayData()
	else:
		c='[]'
		d='[]'
	print y,c,d
	"""
	app.debug = True
        app.run(host='0.0.0.0',port=17202)
