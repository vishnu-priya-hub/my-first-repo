from unittest import TestCase
from rest_framework.reverse import reverse
import unittest
from apoc.employee import views


class HelloViewTest(TestCase):

    expected_input = {'message': 'Hello, World!!'}
    expected_output = {'message': 'Hello, World!'}
    def test_get(self):
        self.assertEqual(views.get(self.expected_input), self.expected_output)

