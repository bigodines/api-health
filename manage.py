#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import click

# tornado
import tornado.ioloop
import tornado.web
# from tornado.concurrent import Future
# from tornado import gen

# api_health
from api_health.controllers.base import BaseController
from api_health.controllers.runner import JobRunner
from api_health.controllers.task import TaskManagement
session_opts = {
    'session.type': 'file',
    'session.auto': True
}


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
            (r'/', BaseController)
            (r'/run', JobRunner)
            (r'/task', TaskManagement)
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
