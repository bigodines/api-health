# -*- coding: utf-8 -*-

from datetime import datetime
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

from api_health.controllers.api.task import TaskApi


# globals. *ugh*
queue = Queue()


@gen.coroutine
def consumer():
    while True:
        task = yield queue.get()
        try:
            task.last_run = datetime.now()
        finally:
            queue.task_done()


@gen.coroutine
def producer():
    [queue.put(t) for t in TaskApi().get_tasks()]


@gen.coroutine
def main():
    pass

if __name__ == "__main__":
    io_loop = IOLoop.concurrent()
    io_loop.run_sync(main)
