# -*- coding: utf-8 -*-
# jinja2
from jinja2 import Environment, FileSystemLoader
# tornado
import tornado.web
from tornado.options import options as settings


class SimpleMultiDict(dict):
    def getlist(self, key):
        return self[key]

    def __repr__(self):
        return type(self).__name__ + '(' + dict.__repr__(self) + ')'


class BaseController(tornado.web.RequestHandler):
    templateLoader = FileSystemLoader(searchpath=settings.TEMPLATE_PATH)
    templateEnv = Environment(loader=templateLoader,
                              trim_blocks=True)

    def get(self):
        template = self.templateEnv.get_template('angular_index.html')
        self.write(template.render())
