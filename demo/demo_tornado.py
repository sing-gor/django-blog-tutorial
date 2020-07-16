import tornado.ioloop
import tornado.web
import os
from services.site_data import SiteData

site_data = SiteData('http://127.0.0.1:7000')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html", site_data=site_data)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", site_data=site_data)

class ShowHandler(tornado.web.RequestHandler):
    def get(self,pk):
        self.render(f"show_{pk}.html", site_data=site_data)

handlers = [
        (r"/", MainHandler),
        (r"/articles/([^/]+)", ShowHandler),
        (r"/articles/", IndexHandler),

    ]


class Application(tornado.web.Application):

    def __init__(self,handlers):

        self.handlers = handlers
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)






if __name__ == "__main__":

    app = Application(handlers)
    app.listen(7000)
    tornado.ioloop.IOLoop.current().start()
