from datetime import timedelta

def calculate_due_date(submit_time, turnaround_time):
    return submit_time + timedelta(hours=turnaround_time)