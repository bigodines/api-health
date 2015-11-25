# -*- coding: utf-8 -*-

import json
import urllib
import responses
from tornado.testing import AsyncHTTPTestCase, gen_test

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
    @responses.activate
    @gen_test
    def test_full_happy_path(self):
        responses.add(responses.GET,
            "http://bazbaz.com",
            body=u'{"name": "test", "numbers": [1, 2, 3]}',
            content_type='application/json',
            status=666)

        post_args = {'url': 'http://bazbaz.com', 'expected_fields': ['name']}
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
