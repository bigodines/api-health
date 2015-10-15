# -*- coding: utf-8 -*-
import json


class Verifier(object):

    def __init__(self, json_body):
        self.json_obj = json.loads(json_body)

    def has_property(self, path):
        return path in self.json_obj
