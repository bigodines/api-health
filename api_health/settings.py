# -*- coding: utf-8 -*-
import os
from tornado.options import define, options


define('PROJECT_PATH', default=os.path.join(os.path.abspath(os.path.dirname(__file__))))
define('TEMPLATE_PATH', default=os.path.join(options.PROJECT_PATH, 'templates'))
define('STATIC_PATH', default=os.path.join(options.PROJECT_PATH, 'static'))

define('port', default=8080)
define('debug', default=True)
define('db_engine_url', default='sqlite:////tmp/test.db')
