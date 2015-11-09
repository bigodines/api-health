# -*- coding: utf-8 -*-
import os
import os.path
import sys

from tornado.testing import AsyncHTTPTestCase

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


class TestApi(TestHandlerBase):

    def test_get_tasks_api(self):
        response = self.fetch('/api/task')
        self.assertEqual(200, response.code)
