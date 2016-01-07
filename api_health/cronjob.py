# -*- coding: utf-8 -*-

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue
from tornado.options import options as opts
import os
import sys
import datetime

APP_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT, '.'))


from api_health import settings
from api_health.worker import Worker
from api_health.controllers.api.task import TaskApi


# globals. *ugh*
queue = Queue()


@gen.coroutine
def consumer():
    while True:
        try:
            task = yield queue.get()
            print task.last_run
            print datetime.datetime.now()
            if task.last_run is None or \
                    (task.last_run + datetime.timedelta(seconds=opts.minimum_interval)) < \
                    datetime.datetime.now():

                print "x" * 60
                Worker(task).execute()
        finally:
            queue.task_done()


@gen.coroutine
def producer():
    tasks = yield TaskApi().get_tasks()
    [queue.put(t) for t in tasks]


@gen.coroutine
def main():
    IOLoop.current().spawn_callback(consumer)
    yield [producer(), queue.join()]
    print "Done"
    raise gen.Return("Done")

if __name__ == "__main__":
    io_loop = IOLoop.current()
    io_loop.run_sync(main)
