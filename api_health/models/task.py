# -*- coding: utf-8 -*-


class Task(object):
    """
    A taski is a dummy structure that contains the API endpoint, request
    parameters and a set of assertions to be made once the results are given.

    Its existing purpose is to serve as a instruction set to be used by workers.
    Please, no business logic here.
    """
    def __init__(self, url, req_options=None, expected_fields=[]):
        self.url = url
        self.request_otpions = req_options
        self.expected_fields = expected_fields

    def __repr__(self):
        return "<Task(%s)>" & self.url
