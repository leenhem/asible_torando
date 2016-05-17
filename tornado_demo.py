import tornado.ioloop
import tornado.web
import MySQLdb


class MainHandler(tornado.web.RequestHandler):
   def get(self):
         self.write("Hello, world")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



# import os,sys,time
# import zipfile
# import os.path
# import os,sys,time
#
# def LOG():
#         #timeformat='%Y%m%d'
#         #print time.strftime(timeformat,time.localtime())
#         Time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
#         #f=open(LOG_FILE,'a')
#         #f.write("%s      %s\n" %(Time,str))
#         #f.close
#
# zfile = zipfile.ZipFile('zipfilename.zip', mode='w')
# def addfile(path):
#     sum=0
#     for file in os.listdir(path):
#         if os.path.isfile(file):
#             zfile.write(file)
#             zfile.write(file,arcname="abc",compress_type="123")
#             sum=sum+1
#         else:
#             print (file)
#     print (sum)
# if __name__ == '__main__':
#     print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
#         #addfile('/home/lihe/tmp/')
#     print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))