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
        try:
            task = TaskApi().add_task(self.request.arguments)
            self.write(json.dumps(task, default=alchemyencoder))
        except Exception as form_errors:
            self.set_status(400)
            self.write('{"error":"%s"}' % form_errors)


class TaskApi(object):
    def get_tasks(self):
        return session.query(Task).all()

    def add_task(self, args):
        task = Task()
        form = TaskForm(SimpleMultiDict(
                        args, obj=task))
        if form.validate():
            form.populate_obj(task)
            session.add(task)
            session.flush()
            return form

        # would rather be explicit here.
        raise Exception("%s" % form.errors)
