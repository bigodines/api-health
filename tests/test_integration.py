# -*- coding: utf-8 -*-

import json
import urllib
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase, gen_test

import api_health.cronjob as cron
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
        super(TestHandlerBase, self).tearDown()
        Base.metadata.drop_all(engine)


class TestIntegration(TestHandlerBase):
    @gen_test
    def test_full_happy_path(self):
        post_args = {'url': 'http://bazuka.com'}
        response = yield self.http_client.fetch(self.get_url('/api/task'),
            method='POST',
            body=urllib.urlencode(post_args),
            follow_redirects=False)
        self.assertEquals(200, response.code)

        yield self.http_client.fetch(self.get_url('/api/run'))

        response = yield self.http_client.fetch(self.get_url('/api/task'))
        self.assertEquals(200, response.code)
        actual = json.loads(response.body)

        self.assertEquals("SUCCESS", actual[0].get('status'))
        self.assertIsNotNone(actual[0].get('last_run'))
