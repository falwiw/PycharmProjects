#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("122.114.13.199", "360Click", "LOVElove12354", "360Click", charset='utf8')

#使用cursor()方法创建一个游标对象
cursor = db.cursor()
#使用execute()方法执行SQL语句
cursor.execute("SELECT * FROM python_user")

#使用fetall()获取全部数据
data = cursor.fetchall()

#打印获取到的数据
print(data)

#关闭游标和数据库的连接
cursor.close()
db.close()
