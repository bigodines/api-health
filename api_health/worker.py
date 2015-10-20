# -*- coding: utf-8 -*-

import requests


class Worker(object):
    """
    A worker is responsible for doing a task and iterating over its output
    in order to verify if it contains what would be expected
    """
    def __init__(self, task):
        self.task = task
        self.errors = []

    def get_errors(self):
        return self.errors

    def has_expected_data(self):
        return False

    def fetch(self):
        result = requests.get(self.task.url)
        try:
            result.raise_for_status()
            json_result = result.json()
            return result
        except requests.HTTPError, e:
            self.errors.append({'url': self.task.url,
                                'code': result.status_code,
                                'body': result.text or None
                                })
            return None
        except ValueError, e:
            self.errors.append({'url': self.task.url,
                                'code': CUSTOM_ERRORS.invalid_response,
                                'body': result.text or None
                                })
            return None
        return result

    def verify(self):
        pass

class CUSTOM_ERRORS:
    invalid_response, missing_field, type_error = range(1,4)


