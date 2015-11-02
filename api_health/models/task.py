# -*- coding: utf-8 -*-


class Task(object):

    def __init__(self, url, expected_fields=None):
        self.url = url
        self.expected_fields = expected_fields
