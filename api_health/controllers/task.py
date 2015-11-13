# -*- coding: utf-8 -*-
from .base import BaseController
from .api.task import TaskApi
from ..models.base import session
from ..models.task import Task


class TaskManagement(BaseController):

    def get(self):
        template_name = "list.html"
        if False:
            template_name = 'detail.html'

        template = self.templateEnv.get_template(template_name)
        all_tasks = TaskApi().get_tasks()
        print all_tasks
        self.write(template.render(all_tasks=all_tasks))

    def post(self):
        task_api = TaskApi()
        try:
            taskForm = TaskApi().add_task(self.request.arguments)
            self.get() # success leads to a list and confirmation message. (in the future)

        except Exception:
            template = self.templateEnv.get_template('detail.html')
            self.write(template.render())
