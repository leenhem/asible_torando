import tornado.httpserver
import tornado.ioloop
import tornado.web

class OtherHandler(tornado.web.RedirectHandler):
    def get(self):
        self.redirect('/hello',permanent=True)

class helloworld(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world\n")
        raise tornado.web.HTTPError(status_code=555,log_message="aaaaa",reason="asdfasdfasdfasdfasdfasdfasdf")

class testpage(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="abc">'
                   '</form></body></html>')
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))

class MainHandlerh(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)
class MainHandlerc(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie", "myvalue")
            self.write("Your cookie was not set yet!")
        else:
            self.write("Your cookie was set!")

class CostomApplication(tornado.web.Application):
    def __init__(self):
        handles=[
            (r"/", MainHandler),
            (r"/hello", helloworld),
            # (r"/test", tornado.web.RedirectHandler, {'url': '/hello'}),
            (r"/test", OtherHandler),
            (r"/story/([0-9]+)", StoryHandler),
            (r"/aaa",MainHandlerh),
            (r"/cookie",MainHandlerc)
        ]
        super(CostomApplication,self).__init__(handles)


# application = tornado.web.Application([
#     (r"/", MainHandler),
#     (r"/cookie", MainHandlerc),
# ], cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")
# if __name__ == ' __main__ ':
application=tornado.httpserver.HTTPServer(CostomApplication())
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
