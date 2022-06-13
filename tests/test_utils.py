from unittest import TestCase
from datetime import datetime

from ppac.utils import datetime_to_str, str_to_datetime


class TestDatetimeStrConversion(TestCase):
    def test_to_string(self):
        date_time = datetime(2022, 5, 3, 12, 34, 44)
        txt = datetime_to_str(date_time)
        self.assertEqual(txt, '2022-05-03T12:34:44')

    def test_from_string(self):
        txt = '2022-05-03T12:34:44'
        date_time = str_to_datetime(txt)
        self.assertEqual(date_time, datetime(2022, 5, 3, 12, 34, 44))
