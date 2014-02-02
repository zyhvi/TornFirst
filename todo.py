#!/usr/bin/dev python
#coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import os.path

from config import controller
from config import options

from config.options import *
from config.controller import *

class Todo(tornado.web.Application):
    def __init__(self):
        Handlers = [
        (r'/', controller.IndexHandler),
        ]

        settings = dict(
        debug = True,
        blog_title = 'TODO',
        template_path = 'templates',
        static_path = 'static',
        )

        tornado.web.Application.__init__(self, Handlers, **settings)


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Todo())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
