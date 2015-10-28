#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import click

# tornado
import tornado.ioloop
import tornado.web
# from tornado.concurrent import Future
# from tornado import gen

# jinja2
from jinja2 import Environment, FileSystemLoader

# api_health
from api_health import settings


session_opts = {
    'session.type': 'file',
    'session.auto': True
}


class BaseHandler(tornado.web.RequestHandler):
    # Load template file templates/site.html
    print settings.TEMPLATE_PATH
    templateLoader = FileSystemLoader(searchpath=settings.TEMPLATE_PATH)
    templateEnv = Environment(loader=templateLoader)


class Dummy(BaseHandler):
    def get(self):
        template = self.templateEnv.get_template('index.html')
        self.write(template.render())


@click.group()
def cmds():
    pass


@cmds.command()
@click.option('--port', default=os.environ.get('PORT', 8080), type=int,
              help=u'Set application server port!')
@click.option('--debug', default=False,
              help=u'Set application server debug!')
def runserver(port, debug):
    app = tornado.web.Application(
        [
            (r'/', Dummy)
        ],
        debug=debug
    )
    app.listen(port)
    click.echo('Server running on port: {}'.format(port))
    tornado.ioloop.IOLoop.current().start()


@cmds.command()
def test():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)


if __name__ == "__main__":
    cmds()
