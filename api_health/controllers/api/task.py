# -*- coding: utf-8 -*-

from api_health.controllers.base import BaseController
from api_health.models.base import session
from api_health.models.task import Task


class TaskApi(BaseController):
    def get_taskas(self):
        return session.query(Task).all()

    def get(self):
        pass
