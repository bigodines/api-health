# -*- coding: utf-8 -*-
import json

from api_health.controllers.base import BaseController
from api_health.models.base import session
from api_health.models.task import Task


class TaskApiController(BaseController):
    def get(self):
        all_tasks = TaskApi().get_tasks()
        self.write(json.dumps(all_tasks))


class TaskApi(object):
    def get_tasks(self):
        return session.query(Task).all()
