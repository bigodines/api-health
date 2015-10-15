# -*- coding: utf-8 -*-
import unittest
from api_health.verifier import Verifier


class JsonVerifier(unittest.TestCase):

    def test_should_check_for_json_property(self):
        simple_json = u'{ "foo": "bar" }'
        verifier = Verifier(simple_json)
        self.assertTrue(verifier.has_property('foo'))
