from unittest import TestCase
from datetime import datetime

from ppac.utils import datetime_to_str, str_to_datetime


class TestDatetimeStrConversion(TestCase):
    def test_to_string(self):
        d = datetime(2022, 5, 3, 12, 34, 44)
        txt = datetime_to_str(d)
        self.assertEqual(txt, '2022-05-03T12:34:44')

    def test_from_string(self):
        txt = '2022-05-03T12:34:44'
        d = str_to_datetime(txt)
        self.assertEqual(d, datetime(2022, 5, 3, 12, 34, 44))
