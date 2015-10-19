# -*- coding: utf-8 -*-

import requests


class Worker(object):
    """
    A worker is responsible for doing a task and iterating over its output
    in order to verify if it's what it has been expected
    """
    def __init__(self, task):
        self.task = task

    def has_expected_data(self):
        return False

    def fetch(self):
        result = requests.get(self.task.url)
        return result
