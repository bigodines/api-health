# -*- coding: utf-8 -*-

import unittest
import responses

from api_health.worker import Worker, CUSTOM_ERRORS
from api_health.models.task import Task


class TestWorker(unittest.TestCase):

    def test_contructor(self):
        task = Task(url="http://foo.com/")
        worker = Worker(task)
        self.assertFalse(worker.has_expected_data())

    @responses.activate
    def test_worker_knows_how_to_request(self):
        responses.add(responses.GET,
                "http://foo.com/",
                status=200)
        task = Task(url="http://foo.com")
        worker = Worker(task)
        worker.fetch()
        self.assertEquals(1, len(responses.calls))

    @responses.activate
    def test_worker_gets_a_404(self):
        responses.add(responses.GET,
                "http://www.idonotexist.com",
                body='{"error": "not found"}',
                content_type='application/json',
                status=404)

        task = Task(url="http://www.idonotexist.com")
        w = Worker(task)
        bad_result = w.fetch()
        self.assertEquals(1, len(w.get_errors()))
        self.assertEquals(404, w.get_errors()[0].get('code'))
        self.assertIsNone(bad_result)

    @responses.activate
    def test_worker_invalid_response(self):
        responses.add(responses.GET,
                "http://www.bigo.com",
                body='i wish i was a json',
                content_type='application/json',
                status=200)

        t = Task(url='http://www.bigo.com')
        worker = Worker(t)
        bad_result = worker.fetch()

        self.assertIsNone(bad_result)
        errors = worker.get_errors()
        self.assertEquals(CUSTOM_ERRORS.invalid_response, errors[0].get('code'))
