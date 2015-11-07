# -*- coding: utf-8 -*-
# jinja2
from jinja2 import Environment, FileSystemLoader
# tornado
import tornado.web

from api_health import settings


class BaseController(tornado.web.RequestHandler):
    templateLoader = FileSystemLoader(searchpath=settings.TEMPLATE_PATH)
    templateEnv = Environment(loader=templateLoader,
                              trim_blocks=True)

    def get(self):
        template = self.templateEnv.get_template('index.html')
        self.write(template.render())
