# -*- coding: utf-8 -*-
import os
import os.path
import sys
import urllib
import json

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
    def test_task_CRUD(self):
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        response = yield self.http_client.fetch(self.get_url('/api/task'),
            method='GET',
            headers=headers)
        self.assertEqual(200, response.code)
        # assert it is empty
        self.assertEqual('[]', response.body)

        post_args = {'url': 'http://baz.com'}
        response = yield self.http_client.fetch(self.get_url('/api/task'),
            method='POST',
            body=urllib.urlencode(post_args),
            follow_redirects=False)

        self.assertEqual(200, response.code)
        response = yield self.http_client.fetch(self.get_url('/api/task'), method='GET')
        self.assertEqual(200, response.code)
        actual = json.loads(response.body)
        # assert it created
        self.assertEqual('http://baz.com', actual[0].get('url'),
                "should have created a task")

        post_args = {'id': actual[0].get('id'), 'url': 'http://xoxoxo.com'}
        yield self.http_client.fetch(self.get_url('/api/task'),
            method='PUT',
            headers=headers,
            body=json.dumps(post_args),
            follow_redirects=False)

        response = yield self.http_client.fetch(self.get_url('/api/task'),
                method='GET')
        self.assertEqual(200, response.code)
        actual = json.loads(response.body)
        # assert it is updated
        self.assertEqual('http://xoxoxo.com', actual[0].get('url'),
                "should have updated a task")

        yield self.http_client.fetch(self.get_url('/api/task?id=%s' % actual[0].get("id")),
                method="DELETE")

        response = yield self.http_client.fetch(self.get_url('/api/task'), method='GET')
        # should be back to the empty state
        self.assertEqual('[]', response.body,
                "should have deleted the task")

    @gen_test
    def test_bogus_delete(self):
        try:
            yield self.http_client.fetch(self.get_url('/api/task?id=100'),
                method="DELETE")
            self.assertTrue(False, "was expecting a 400")
        except Exception as e:
            self.assertEqual(400, e.code)
