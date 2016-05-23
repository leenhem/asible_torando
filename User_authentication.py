import tornado.web
import tornado.httpserver

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        self.xsrf_form_html()
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)

class LoginHandler(BaseHandler):
    def get(self):
        self.xsrf_form_html()
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')


    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")

settings = {
    "cookie_secret":"61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url":"/login",
    "xsrf_cookies":True,
}

# <form action="/new_message" method="post">
# {{ xsrf_form_html() }}
# <input type="text" name="message"/>
# <input type="submit" value="Post"/>
# </form>


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
], **settings)

application=tornado.httpserver.HTTPServer(application)
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
