from datetime import timedelta

WORKING_HOURS_START = 9
WORKING_HOURS_FINISH = 17

WORKING_DAYS = [
    0, 1, 2, 3, 4
]

def _is_working_hours(time):
    return WORKING_HOURS_START <= time.hour < WORKING_HOURS_FINISH

def _is_weekday(time):
    return time.weekday() in WORKING_DAYS

def _is_worktime(time):
    return _is_weekday(time) and _is_working_hours(time)

def calculate_due_date(submit_time, turnaround_time):
    due_date = submit_time
    remaining_hours = turnaround_time
    while remaining_hours > 0 or not _is_worktime(due_date):
        if _is_worktime(due_date):
            remaining_hours -= 1
        due_date += timedelta(hours=1)
    return due_date