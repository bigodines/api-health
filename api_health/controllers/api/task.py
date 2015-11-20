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
    """
    Interfaces with TaskApi rendering the responses in a developer friendly
    format. (for use facing templates, refer to controllers/task.py)
    """
    @gen.coroutine
    def get(self):
        all_tasks = yield TaskApi().get_tasks()
        response = json.dumps([r.to_json() for r in all_tasks], default=alchemyencoder)
        self.write(response)

    @gen.coroutine
    def post(self):
        try:
            task = yield TaskApi().add_task(self.request.arguments)
            self.write(json.dumps(task, default=alchemyencoder))
        except Exception as form_errors:
            self.set_status(400)
            self.write('{"error":"%s"}' % form_errors)


class TaskApi(object):
    """
    Core business for the task management. This class is responsible for storing
    and retrieving Task related operations.
    """
    @gen.coroutine
    def get_tasks(self):
        """Returns a list of tasks available"""
        all_tasks = session.query(Task).all()
        session.flush()
        raise gen.Return(all_tasks)

    @gen.coroutine
    def add_task(self, args):
        """
        Stores a new Task() and returns a TaskForm() to be rendered
        or Raise and exception with the invalid/missing fields
        """
        task = Task()
        form = TaskForm(SimpleMultiDict(
                        args, obj=task))
        if form.validate():
            form.populate_obj(task)
            session.add(task)
            session.commit()
            raise gen.Return(form)

        # would rather be explicit here.
        raise Exception("%s" % form.errors)
