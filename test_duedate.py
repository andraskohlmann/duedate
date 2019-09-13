import unittest

from datetime import datetime
from duedate import calculate_due_date


class TestDueDateCalculator(unittest.TestCase):
    def test_method_exists(self):
        calculate_due_date(datetime.now(), 0)
