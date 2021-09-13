from typing import List
import datetime as dt
from O365 import calendar


def get_calendar_for_this_week(schedule: calendar.Schedule) -> List[calendar.Event]:
    all_events = []
    c = schedule.get_default_calendar()
    # Get first and last (working) day of this week
    today = dt.datetime(2021, 10, 10)   # TODO: this is hardcode for demo purpose
    start = today - dt.timedelta(days=today.weekday())
    end = start + dt.timedelta(days=6)
    # Prepare query
    q = c.new_query('start').greater_equal(start)
    q.chain('and').on_attribute('end').less_equal(end)

    events = c.get_events(query=q, include_recurring=True)
    for event in events:
        all_events.append(event)
    return all_events
