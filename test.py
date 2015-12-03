#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import tornado.options
from api_health import settings
tornado.options.parse_config_file(os.path.join(tornado.options.options.PROJECT_PATH, "conf/test.conf"))
logging.getLogger().setLevel(logging.CRITICAL)
import nose


if __name__ == "__main__":
    nose.run(argv=["", "--where=./tests", "--with-coverage", '--cover-package=api_health'])
