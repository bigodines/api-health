# -*- coding: utf-8 -*-
import json

from jsonpath_rw import parse


class Verifier(object):

    def __init__(self, json_body):
        self.json_obj = json_body if isinstance(json_body, dict) else json.loads(json_body)

    def has_property(self, path):
        expr = parse(path)
        return len(expr.find(self.json_obj)) > 0

    def does_not_have_property(self, path):
        return not self.has_property(path)
