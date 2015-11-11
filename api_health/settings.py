# -*- coding: utf-8 -*-
import os


PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

ENV = os.environ.get('ENV', 'development')
db_engine_url = 'sqlite:///:memory:' if ENV is 'test' else 'sqlite:////tmp/test.db'

