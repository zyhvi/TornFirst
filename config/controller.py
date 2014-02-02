import tornado.web
from config.options import *


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        todos = db.query('SELECT * FROM todo')
        self.render('index.html',todos = todos)
