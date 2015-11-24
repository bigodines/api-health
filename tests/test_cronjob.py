# -*- coding: utf-8 -*-
import responses

from tornado.testing import AsyncTestCase, gen_test
from tornado.queues import Queue

import api_health.cronjob as cron
from api_health.models.base import Base, session, engine
from api_health.models.task import Task


class WorkerMock(object):
    def execute(self):
        pass


class TestCronJob(AsyncTestCase):
    def setUp(self):
        super(TestCronJob, self).setUp()
        cron.queue = Queue()
        Base.metadata.create_all(engine)

    def tearDown(self):
        super(TestCronJob, self).tearDown()
        Base.metadata.drop_all(engine)

    @gen_test
    @responses.activate
    def test_producer_should_load_all_tasks(self):
        responses.add(responses.GET,
                'https://api.github.com',
                status=200)
        responses.add(responses.GET,
                'https://api.github.com/repos/bigodines/api-health/',
                status=200)

        t1 = Task(url="https://api.github.com")
        t2 = Task(url="https://api.github.com/repos/bigodines/api-health/")
        session.add(t1)
        session.add(t2)
        session.commit()

        yield cron.producer()
        self.assertEquals(cron.queue.qsize(), 2)

    @gen_test
    def test_consumer_should_run_tasks_from_queue(self):
        responses.add(responses.GET,
                'https://api.github.com',
                status=200)
        responses.add(responses.GET,
                'https://api.github.com/repos/bigodines/api-health/',
                status=200)

        t1 = Task(url="https://api.github.com")
        t2 = Task(url="https://api.github.com/repos/bigodines/api-health/")

        # sanity check
        self.assertIsNone(t1.last_run)

        cron.queue.put(t1)
        cron.queue.put(t2)

        self.io_loop.spawn_callback(cron.consumer)
        yield cron.queue.join()

        self.assertIsNotNone(t1.last_run)
        self.assertIsNotNone(t2.last_run)

