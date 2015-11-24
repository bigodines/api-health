# -*- coding: utf-8 -*-
import json
import datetime
import decimal
import urlparse

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

    @gen.coroutine
    def put(self):
        try:
            new_values = urlparse.parse_qs(self.request.body)
            for k in new_values:
                new_values[k] = new_values[k]

            task = yield TaskApi().update_task(new_values)
            self.write(json.dumps(task, default=alchemyencoder))
        except Exception as form_errors:
            self.set_status(400)
            self.write('{"error":"%s"}' % form_errors)

    @gen.coroutine
    def delete(self):
        try:
            yield TaskApi().delete_task(self.request.arguments)
            self.write('[]')

        except Exception as form_errors:
            self.set_status(400)
            self.write('{"error": "%s"}' % form_errors)


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

    @gen.coroutine
    def update_task(self, args):
        task = session.query(Task).filter_by(id=args.get('id')[0]).first()
        form = TaskForm(SimpleMultiDict(args, obj=task))
        if form.validate():
            form.populate_obj(task)
            session.commit()

        raise gen.Return(form)

    @gen.coroutine
    def delete_task(self, args):
        try:
            task = session.query(Task).filter_by(id=args.get('id')[0]).first()
            session.delete(task)
            session.commit()
            # still haven't decided on a pattern for this class, as you can see
            return True

        except:
            raise Exception("Could not delete task base on args: %s" % args)
