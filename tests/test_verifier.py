# -*- coding: utf-8 -*-
import unittest
import json
from api_health.verifier import Verifier


class JsonVerifier(unittest.TestCase):

    def test_should_be_smart_about_constructor_initializtion(self):
        simple_json = u'{ "foo": "bar" }'
        json_dict = json.loads(simple_json)
        try:
            v1 = Verifier(simple_json)
            v2 = Verifier(json_dict)
        except:
            self.fail('Verifier() constructor should deal with both ' \
                    'string and object json')

    def test_should_check_for_json_property(self):
        simple_json = u'{ "foo": "bar" }'
        verifier = Verifier(simple_json)
        self.assertTrue(verifier.has_property('foo'))
        self.assertFalse(verifier.has_property('bleh'))
