# -*- coding: utf-8 -*-
from tornado import gen

from api_health.controllers.base import BaseController
from api_health.controllers.api.task import TaskApi
from api_health.worker import Worker


class RunApiController(BaseController):
    @gen.coroutine
    def get(self):
        """ Manually run one task or all tasks.
        plese be careful when using this method, as the cronjob.py is a more efficient
        solution using queues"""
        tasks = yield TaskApi().get_tasks()
        [Worker(t).execute() for t in tasks]
        self.write('')
