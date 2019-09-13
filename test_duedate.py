import unittest

from datetime import datetime
from duedate import calculate_due_date


class TestDueDateCalculator(unittest.TestCase):
    def test_method_exists(self):
        calculate_due_date(datetime.now(), 0)

    def test_turnaround_time_zero_due_date_is_submit_time(self):
        submit_time = datetime(2019, 9, 13, 9, 0)
        due_date = calculate_due_date(submit_time, 0)
        self.assertEqual(submit_time, due_date)

    def test_turnaround_time_one_hour_due_date_is_submit_time_plus_one_hour(self):
        submit_time = datetime(2019, 9, 13, 9, 0)
        expected_due_date = datetime(2019, 9, 13, 10, 0)
        due_date = calculate_due_date(submit_time, 1)
        self.assertEqual(expected_due_date, due_date)
