# -*- coding: utf-8 -*-

import unittest
import responses

from api_health.worker import Worker
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
