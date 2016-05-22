from Operation_MySQL import Operation_database
host="127.0.0.1"
port=3306
user="root"
passw='11qq```'
db="ansible_user"
a=Operation_database()
class CD(object):
    def OD(self,name):
        name="lihe"
        mmm=a.Connect_database(host,port,user,passw,db)
        sql="select * from ansible_user.auth WHERE 1=1 and uname = \""+name+"\" limit 1"
        mmm.execute(sql)
        for row in mmm.fetchall():
            # print row
            return row[1],row[2]