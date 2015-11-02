# -*- coding: utf-8 -*-


class Task(object):
    """
    A simple VO to encapsulate
    the domain of a Task. (Should be as dummy as possible)
    """
    def __init__(self, url, expected_fields=None):
        self.url = url
        self.expected_fields = expected_fields
