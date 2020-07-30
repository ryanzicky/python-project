#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 15:25
# @Author  : JiaYan
# @Site    : 
# @File    : MySqlDemo.py
# @Software: PyCharm

import pymysql

# 打开数据库连接
db = pymysql.connect('47.105.171.231', 'root', '123456', 'db1')

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute() 方法执行SQL查询
# cursor.execute("select version()")
# cursor.execute('show databases')

# 使用fetchone()方法获取当跳数据
# data = cursor.fetchone()
# data = cursor.fetchall()

# print('Database version : %s ' % data)
# print('Database version : ', data)



# 创建表
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE employee (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)

# 插入数据
# # SQL 插入数据
# sql = """
#     INSERT INTO employee(
#         FIRST_NAME, LAST_NAME, AGE, SEX, INCOME
#     )
#     VALUES (
#         'Mac', 'Mohan', 20, 'M', 2000
#     )
# """
#
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误回滚
#     db.rollback()

# 查询数据
# sql = 'select * from employee where income > %s' % 1000
#
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#
#         print("fname = %s, lname = %s, age = %s, sex = %s, income = %s" % (fname, lname, age, sex, income))
# except:
#     print('Error: unable to fetch data.')

# 更新数据
# sql = 'update employee set age = age + 1 where sex = "%c"' % 'M'
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# 删除数据
# sql = 'delete from employee where age > %s ' % 20
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# 关闭数据库连接
db.close()
