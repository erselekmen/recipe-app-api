from app import calculator

from django.test import SimpleTestCase


class CalcTests(SimpleTestCase):

    def test_add(self):
        res = calculator.add(5, 6)
        self.assertEqual(res, 11)
