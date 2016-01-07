# -*- coding: utf-8 -*-
import os
from tornado.options import define, options


define('PROJECT_PATH', default=os.path.join(os.path.abspath(os.path.dirname(__file__))))
define('CLIENT_PATH', default=os.path.join(options.PROJECT_PATH, 'client'))
define('TEMPLATE_PATH', default=os.path.join(options.CLIENT_PATH, 'templates'))
define('STATIC_PATH', default=os.path.join(options.PROJECT_PATH, 'static'))

define('port', default=8080)
define('debug', default=True)
define('db_engine_url', default='sqlite:////tmp/test.db')
define('minimum_interval', default=10) # minimum of interval between checking the same task again
