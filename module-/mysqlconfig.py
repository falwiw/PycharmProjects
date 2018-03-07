#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import time
import datetime
# 打开数据库连接
db = pymysql.connect("122.114.13.199", "360Click", "LOVElove12354", "360Click", charset='utf8')

#使用cursor()方法创建一个游标对象
cursor = db.cursor()

sql1 = "SELECT * FROM python_user WHERE user='admin1A'"

try:
    cursor.execute(sql1)
    # 使用execute()方法执行SQL语句
    data = cursor.fetchall()
    sql_user = data[0][1]
    sql_pwd = data[0][2]
    print("数据库查询结果：", sql_user, sql_pwd)
except:
    print("出错了")
    #使用execute()方法执行SQL语句
    sign_in_time = int(time.time())

    print(sign_in_time)
    sql2 = "INSERT INTO python_user( 'signtime') VALUES(sign_in_time)"
    cursor.execute(sql2)


    #关闭游标和数据库的连接
    cursor.close()
    db.close()
