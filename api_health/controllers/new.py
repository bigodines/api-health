# -*- coding: utf-8 -*-
from .base import BaseController
from api_health.models.task import TaskForm


class NewTaskController(BaseController):

    def get(self):
        template = self.templateEnv.get_template('detail.html')
        self.write(template.render(form=TaskForm()))
