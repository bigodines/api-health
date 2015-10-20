# -*- coding: utf-8 -*-

import requests

from api_health.verifier import Verifier

class Worker(object):
    """
    A worker is responsible for doing a task and iterating over its output
    in order to verify if it contains what would be expected
    """
    def __init__(self, task):
        self.task = task
        self.errors = []
        self.is_done = False

    def get_errors(self):
        return self.errors

    def has_expected_data(self):
        return self.errors == [] and self.is_done

    def fetch(self):
        result = requests.get(self.task.url)
        try:
            result.raise_for_status()
            json_result = result.json()
            return json_result
        except requests.HTTPError, e:
            self.add_error(code=result.status_code, body=result.text)
            return None
        except ValueError, e:
            self.add_error(code=CUSTOM_ERRORS.invalid_response, body=result.text)
            return None
        return result

    def execute(self):
        response = self.fetch()
        self.verify(response)
        self.is_done = True

    def verify(self, json_data):
        if not json_data or not self.task.expected_fields:
            return

        verifier = Verifier(json_data)
        buggy_expects = filter(verifier.does_not_have_property, self.task.expected_fields)
        # TODO: this could be a map()
        [self.add_error(CUSTOM_ERRORS.missing_field, body="Path not found on json: %s" % e) for e in buggy_expects]

    def add_error(self, code,body=None):
        self.errors.append({
            'url': self.task.url,
            'code': code,
            'message': body
            })

class CUSTOM_ERRORS:
    invalid_response, missing_field, type_error = range(1,4)


