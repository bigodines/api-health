# -*- coding: utf-8 -*-
import os
import os.path
import sys
import urllib

from tornado import gen
from tornado.testing import AsyncHTTPTestCase, gen_test

APP_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT, '..'))

from api_health import app
from api_health.models.base import Base, engine

instance = app.create()


class TestHandlerBase(AsyncHTTPTestCase):
    def setUp(self):
        Base.metadata.create_all(engine)
        super(TestHandlerBase, self).setUp()

    def get_app(self):
        return instance

    def tearDown(self):
        Base.metadata.drop_all(engine)
        super(TestHandlerBase, self).tearDown()


class TestApi(TestHandlerBase):

    @gen_test
    def test_get_empty_task_list(self):
        response = yield self.http_client.fetch(self.get_url('/api/task'), method='GET')
        self.assertEqual(200, response.code)
        self.assertEqual('[]', response.body)

    @gen_test
    def test_create_new_tasks(self):
        post_args = {'url': 'http://baz.com'}

        response = yield self.http_client.fetch(self.get_url('/api/task'),
            method='POST',
            body=urllib.urlencode(post_args),
            follow_redirects=False)

        self.assertEqual(200, response.code)

