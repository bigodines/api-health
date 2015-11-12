#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import click

# 3rd pty
import tornado.ioloop
# from tornado.concurrent import Future
# from tornado import gen

@click.group()
def cmds():
    pass


@cmds.command()
@click.option('--port', default=os.environ.get('PORT', 8080), type=int,
              help=u'Set application server port!')
@click.option('--debug', default=False,
              help=u'Set application server debug!')
def runserver(port, debug):
    # api_health
    from api_health import app

    instance = app.create({'debug': debug})
    instance.listen(port)

    click.echo('Server running on port: {}'.format(port))
    tornado.ioloop.IOLoop.current().start()


@cmds.command()
def test():
    import unittest
    from api_health import settings
    settings.db_engine_url = 'sqlite:///:memory:'
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)


if __name__ == "__main__":
    cmds()
