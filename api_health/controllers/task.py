# -*- coding: utf-8 -*-
from .base import BaseController
from ..models.base import session
from ..models.task import Task


class TaskManagement(BaseController):

    def get(self):
        template_name = "list.html"
        if False:
            template_name = 'detail.html'

        template = self.templateEnv.get_template(template_name)
        all_tasks = session.query(Task).all()
        print all_tasks
        task = Task(url="foo")
        session.add(task)
        self.write(template.render(all_tasks=all_tasks))

    def post(self):
        task = Task(url="http://bleh.com")
        session.add(task)
