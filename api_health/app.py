# -*- coding: utf-8 -*-
import tornado.web
from tornado.options import options as settings

from api_health.controllers.base import BaseController
from api_health.controllers.task import TaskManagement
from api_health.controllers.new import NewTaskController
from api_health.controllers.api.run import RunApiController
from api_health.controllers.api.task import TaskApiController


def create(options={}):
    return tornado.web.Application(
        [
            (r'/app/?.*', BaseController),
            (r'/task/(.*)', TaskManagement),
            (r'/new_task', NewTaskController),

            # API
            (r'/api/run', RunApiController),
            (r'/api/task', TaskApiController),

            # Routes to the angular app
            (r'/client/(.*)', tornado.web.StaticFileHandler,
                {"path": settings.CLIENT_PATH})
        ],
        debug=options.get('debug'),
        static_path=settings.STATIC_PATH
    )
