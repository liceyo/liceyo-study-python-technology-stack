import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import web
from web.chat_room import ChatRoom

define("port", default=9090, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        self.chat_room = ChatRoom()
        handlers = web.handlers
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            ' ui_modules': web.ui_modules
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
