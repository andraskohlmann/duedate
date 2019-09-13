import unittest
from ddt import ddt, data, unpack
from datetime import datetime
from duedate import calculate_due_date

@ddt
class TestDueDateCalculator(unittest.TestCase):
    @unpack
    @data(
        {
            'test_case': 'Turnaround time is zero, due date is submit time',
            'submit_time': datetime(2019, 9, 13, 9, 0),
            'turnaround_time': 0,
            'expected_due_date': datetime(2019, 9, 13, 9, 0)
        },
        {
            'test_case': 'Turnaround time is zero, due date is submit time',
            'submit_time': datetime(2019, 9, 13, 9, 0),
            'turnaround_time': 1,
            'expected_due_date': datetime(2019, 9, 13, 10, 0)
        },
        {
            'test_case': 'Turnaround time is zero, due date is submit time',
            'submit_time': datetime(2019, 9, 12, 17, 0),
            'turnaround_time': 0,
            'expected_due_date': datetime(2019, 9, 13, 9, 0)
        },
        {
            'test_case': 'Turnaround time is zero, due date is submit time',
            'submit_time': datetime(2019, 9, 12, 16, 38),
            'turnaround_time': 1,
            'expected_due_date': datetime(2019, 9, 13, 9, 38)
        }
    )
    def test_due_date_calculation(self, test_case, submit_time, turnaround_time, expected_due_date):
        due_date = calculate_due_date(submit_time, turnaround_time)
        self.assertEqual(expected_due_date, due_date, msg=test_case)
