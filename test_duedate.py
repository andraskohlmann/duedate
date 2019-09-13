import unittest
from ddt import ddt, data, unpack
from datetime import datetime, timedelta
from duedate import calculate_due_date

THIS_WEEK_MONDAY = datetime.today() - timedelta(days=datetime.today().weekday())
THIS_WEEK_MONDAY = THIS_WEEK_MONDAY.replace(hour=0, minute=0, second=0, microsecond=0)

MONDAY, TUESDAY, FRIDAY = 0, 1, 4
THIS_WEEK, NEXT_WEEK, NEXT_NEXT_WEEK = 0, 1, 2

def get_time(week, day, hour, minute):
    days = week * 7 + day
    return THIS_WEEK_MONDAY + timedelta(days=days, hours=hour, minutes=minute)

@ddt
class TestDueDateCalculator(unittest.TestCase):
    @unpack
    @data(
        {
            'test_case': 'Turnaround time is zero, due date is submit time',
            'submit_time': get_time(THIS_WEEK, MONDAY, 9, 0),
            'turnaround_time': 0,
            'expected_due_date': get_time(THIS_WEEK, MONDAY, 9, 0)
        },
        {
            'test_case': 'Turnaround time is one hour, due date is submit time plus one hour',
            'submit_time': get_time(THIS_WEEK, MONDAY, 9, 0),
            'turnaround_time': 1,
            'expected_due_date': get_time(THIS_WEEK, MONDAY, 10, 0)
        },
        {
            'test_case': 'Turnaround time is zero, submit time is 17pm, due date is next day 9am',
            'submit_time': get_time(THIS_WEEK, MONDAY, 17, 0),
            'turnaround_time': 0,
            'expected_due_date': get_time(THIS_WEEK, TUESDAY, 9, 0)
        },
        {
            'test_case': 'Turnaround time is five hours, due date is next day',
            'submit_time': get_time(THIS_WEEK, MONDAY, 14, 38),
            'turnaround_time': 5,
            'expected_due_date': get_time(THIS_WEEK, TUESDAY, 11, 38)
        },
        {
            'test_case': 'Turnaround time is eight hours, submit date is friday, due date is next week',
            'submit_time': get_time(THIS_WEEK, FRIDAY, 14, 31),
            'turnaround_time': 8,
            'expected_due_date': get_time(NEXT_WEEK, MONDAY, 14, 31)
        },
        {
            'test_case': 'Turnaround time is more than a week, landing on a weekend, due date is next Monday',
            'submit_time': get_time(THIS_WEEK, MONDAY, 9, 0),
            'turnaround_time': 80,
            'expected_due_date': get_time(NEXT_NEXT_WEEK, MONDAY, 9, 0)
        }
    )
    def test_due_date_calculation(self, test_case, submit_time, turnaround_time, expected_due_date):
        due_date = calculate_due_date(submit_time, turnaround_time)
        self.assertEqual(expected_due_date, due_date, msg=test_case)
