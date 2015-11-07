# -*- coding: utf-8 -*-
import tornado.web

from api_health import settings
from api_health.controllers.base import BaseController
from api_health.controllers.runner import JobRunner
from api_health.controllers.task import TaskManagement


def create(options):
    return tornado.web.Application(
        [
            (r'/', BaseController),
            (r'/run', JobRunner),
            (r'/task', TaskManagement)
        ],
        debug=options.get('debug'),
        static_path=settings.STATIC_PATH
    )
