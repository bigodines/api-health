# -*- coding: utf-8 -*-
import os
import os.path
import sys
import urllib
import json

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
        response = yield self.http_client.fetch(self.get_url('/api/task'), method='GET')
        self.assertEqual(200, response.code)
        self.assertEqual('[]', response.body)

        post_args = {'id': 1, 'url': 'http://baz.com'}
        response = yield self.http_client.fetch(self.get_url('/api/task'),
            method='POST',
            body=urllib.urlencode(post_args),
            follow_redirects=False)

        self.assertEqual(200, response.code)
        response = yield self.http_client.fetch(self.get_url('/api/task'), method='GET')
        self.assertEqual(200, response.code)
        actual = json.loads(response.body)
        self.assertEqual('http://baz.com', actual[0].get('url'))


