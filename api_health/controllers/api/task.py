# -*- coding: utf-8 -*-
import json
import datetime
import decimal

from tornado import gen

from api_health.controllers.base import BaseController, SimpleMultiDict
from api_health.models.base import session
from api_health.models.task import Task, TaskForm


def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


class TaskApiController(BaseController):
    @gen.coroutine
    def get(self):
        all_tasks = TaskApi().get_tasks()
        response = json.dumps([r.to_json() for r in all_tasks], default=alchemyencoder)
        self.write(response)

    @gen.coroutine
    def post(self):
        task = Task()
        form = TaskForm(SimpleMultiDict(
                        self.request.arguments, obj=task))
        if form.validate():
            form.populate_obj(task)
            TaskApi().add_task(task)
            self.write('[]')
        else:
            self.set_status(400)
            self.write('{"error":"%s"}' % form.errors)


class TaskApi(object):
    def get_tasks(self):
        return session.query(Task).all()

    def add_task(self, task=None):
        session.add(task)
        session.flush()
