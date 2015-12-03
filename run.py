#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click

# 3rd pty
import tornado.ioloop
from tornado.options import options as opts

from api_health import settings


def help():
    pass


def runserver():
    # api_health
    from api_health import app

    instance = app.create({'debug': opts.debug})
    instance.listen(opts.port)

    click.echo('Server running on port: {}'.format(opts.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    runserver()
