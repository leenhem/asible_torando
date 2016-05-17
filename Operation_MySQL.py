# -*- coding: utf-8 -*-
import time
import MySQLdb
#connection
class Operation_database(object):
    def Connect_database(self,parameter_host,parameter_port,parameter_user,parameter_pass,parameter_db):
        c=MySQLdb.connect(
            host=parameter_host,
            port=parameter_port,
            user=parameter_user,
            passwd=parameter_pass,
            db=parameter_db,
            charset="utf8")
        cursor = c.cursor()
        return cursor
    def Drop_tables(self,table):
        sql = "drop table if exists user"
        self.cursor.execute(sql)
    def Create_tables(self,a,table):
        sql = "create table if not exists user(name varchar(128) primary key, created int(10))"
        a.execute(sql)
#     def Insert_tables(self,table):
#         sql = "insert into user(name,created) values(%s,%s)"
#         param = ("aaa", Mint(time.time()))
#         n = cursor.execute(sql,param)
#         print 'insert',n
#     def Insert_mulit_tables(self,tables):
#         sql = "insert into user(name,created) values(%s,%s)"
#         param = (("bbb",int(time.time())), ("ccc",33), ("ddd",44) )
#         n = cursor.executemany(sql,param)
#         print 'insertmany',n
#     def Update_tables(self,tables):
#         sql = "update user set name=%s where name='aaa'"
#         param = ("zzz")
#         n = cursor.execute(sql,param)
#         print 'update',n
#
# host="127.0.0.1"
# port=3306
# user="root"
# passw="root"
# db="mysql"
# a=Operation_database()
# mmm=a.Connect_database(host,port,user,passw,db)
# print mmm
#
# #select
# n = cursor.execute("select * from user")
# for row in cursor.fetchall():
#     print row
#     for r in row:
#         print r
#
# #delete
# sql = "delete from user where name=%s"
# param =("bbb")
# n = cursor.execute(sql,param)
# print 'delete',n
#
# #select
# n = cursor.execute("select * from user")
# print cursor.fetchall()
#
# cursor.close()
#
# #commit
# conn.commit()
# #close
# conn.close()