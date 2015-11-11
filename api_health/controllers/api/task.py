# -*- coding: utf-8 -*-
import json


from api_health.controllers.base import BaseController, SimpleMultiDict
from api_health.models.base import session
from api_health.models.task import Task, TaskForm


class TaskApiController(BaseController):
    def get(self):
        all_tasks = TaskApi().get_tasks()
        self.write(json.dumps(all_tasks, default=str))

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
        session.commit()
