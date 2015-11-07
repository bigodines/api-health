# -*- coding: utf-8 -*-
import os
import os.path
import sys

from tornado.options import options
from tornado.testing import AsyncHTTPTestCase
from api_health.controllers.api.task import TaskApi

APP_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT, '..'))

import api_health.app
instance = api_health.app.create()


class TestHandlerBase(AsyncHTTPTestCase):
    def setUp(self):
        super(TestHandlerBase, self).setUp()

    def get_app(self):
        return instance

    def get_http_port(self):
        return options.port


class TestApi(TestHandlerBase):

    def test_get_tasks_api(self):
        pass

