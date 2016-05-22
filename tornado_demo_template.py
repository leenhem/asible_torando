import time
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado_mysql import CD

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return

            # name = tornado.escape.xhtml_escape(self.current_user)
            # self.write("Hello, " + name)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        passw = self.get_argument('pass')
        a=CD()
        user,passwd=a.OD(name)
        if passwd == passw:
            self.write("User "+name+" Login sussece !")
            # self.render('poem.html',n=name,p=passw)
        else:
            self.write("password error "+passw+passwd)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers=[(r'/', IndexHandler),
                      (r'/poem', PoemPageHandler)],
            template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# self.set_secure_cookie('user_id', '1', expires_days=None, expires=time.time()+900)