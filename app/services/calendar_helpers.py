from app.core.config import settings
from app.services.image_helpers import create_bitmap_from_calendar
import datetime as dt


def get_calendar_for_this_week():
    if settings.account:
        schedule = settings.account.schedule()
        calendar = schedule.get_default_calendar()

        today = dt.datetime(2021, 10, 10)
        start = today - dt.timedelta(days=today.weekday())
        end = start + dt.timedelta(days=6)
        # print("Today: " + str(today))
        # print("Start: " + str(start))
        # print("End: " + str(end))

        q = calendar.new_query('start').greater_equal(start)
        q.chain('and').on_attribute('end').less_equal(end)

        events = calendar.get_events(query=q, include_recurring=True) 
        print(events)
        for event in events:
            print(event.st)


    ## Something not right. Return None
    return None

