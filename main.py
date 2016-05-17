#!/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from Operation_MySQL import Operation_database
import json
f=open("C:\Users\leenhem\Desktop\iphelper.txt",'w')
host="192.168.204.11"
port=3306
user="root"
passw="cmrictpdata"
db="test"
a=Operation_database()
mmm=a.Connect_database(host,port,user,passw,db)
sql="SELECT * FROM ( " \
    "SELECT ipv4 AS ip1, ipv4 AS ip2, ip2long AS ip2long1, ip2long AS ip2long2, `update`, country, province, city, detail, isp, loc, OWNER, remark " \
    "FROM ip_addr_bank " \
    "UNION ALL " \
    "SELECT ip_start AS ip1, ip_end AS ip2, ip2long_start AS ip2long1, ip2long_end AS ip2long2, `update`, country, province, city, detail, isp, loc, OWNER, remark " \
    "FROM ip_bank ) AS zi " \
    "ORDER BY ip2long1 ASC"
# sql = "create table if not exists user(name varchar(128) primary key, created int(10))"
# sql = "create table uaaar(name varchar(128) primary key, created int(10))"
mmm.execute(sql)
for row in mmm.fetchall():
    # print row
    #c = a if a>b else b
    ip1=str(row[0]).encode(encoding="utf-8").replace('CZ88.NET','') if str(row[0]).encode(encoding="utf-8").strip() else "-"
    ip2=str(row[1]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[1]).encode(encoding="utf-8").strip()  else "-"
    ip2long1=str(row[2]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[2]).encode(encoding="utf-8").strip() else "-"
    ip2long2=str(row[3]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[3]).encode(encoding="utf-8").strip()  else "-"
    update=str(row[4]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[4]).encode(encoding="utf-8").strip() else "-"
    country=str(row[5]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[5]).encode(encoding="utf-8").strip()  else "-"
    province=str(row[6]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[6]).encode(encoding="utf-8").strip()  else "-"
    city=str(row[7]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[7]).encode(encoding="utf-8").strip() else "-"
    detail=str(row[8]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[8]).encode(encoding="utf-8").strip()  else "-"
    isp=str(row[9]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[9]).encode(encoding="utf-8").strip()  else "-"
    loc=str(row[10]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[10]).encode(encoding="utf-8").strip()  else "-"
    owner=str(row[11]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[11]).encode(encoding="utf-8").strip()  else "-"
    remark=str(row[12]).encode(encoding="utf-8").replace('CZ88.NET','') if  str(row[12]).encode(encoding="utf-8").strip()  else "-"
    # data1={}
    #1.2.5.0	1.2.7.255
    # {"startip":"1.2.5.0","endip":"1.2.7.255","startlong":"16909568","endlong":"16910335","country":"中国",
    # "province":"福建省","city":"福州市","detail":"-","isp":"电信","loc":"福建省","remark":"福建省电信"}
    # print json.dumps(data1, encoding="UTF-8", ensure_ascii=False)
    data1 = {'startip':ip1 ,'endip':ip2 ,'startlong':ip2long1,'endlong':ip2long2,'country':country,'province':province,'city':city,'detail':detail,
             'isp':isp,'loc':loc,'remark':remark}
    # print data1
    print ip1,ip2,json.dumps(data1,encoding="UTF-8",ensure_ascii=False)
    js=ip1+' '+ip2+' '+json.dumps(data1,encoding="UTF-8",ensure_ascii=False)
    f.write(js+"\n")
    # print ip1,ip2,json.dumps(data1,encoding="UTF-8",ensure_ascii=False,indent=4)
    # data1= {'uid':uid ,'ipv4':ipv4}
    # print json.dumps(data1, encoding="UTF-8", ensure_ascii=False)
    # print data1
    # json.dumps(data1,ensure_ascii=False)
    # d1 =  json.dumps(data1,sort_keys=True)
    # print d1
    # for r in row=row[0]:
    #       print r
# table="chenguangchao"
# mmm.Create_tables(mmm,table)
