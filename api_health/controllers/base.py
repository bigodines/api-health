# -*- coding: utf-8 -*-
# jinja2
# tornado
import tornado.web


class SimpleMultiDict(dict):
    def getlist(self, key):
        return self[key]

    def __repr__(self):
        return type(self).__name__ + '(' + dict.__repr__(self) + ')'


class BaseController(tornado.web.RequestHandler):

    def get(self):
        self.render("angular_index.html")
