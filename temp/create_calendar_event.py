""" Not work properly!!! """

import datetime as dt
from O365 import Account, MSGraphProtocol
import pytz
import os

CLIENT_ID = 'drgrgrg'
SECRET_ID = '<your secret id>'
SECRET_VALUE = 'dergdfhdthd'

credentials = (CLIENT_ID, SECRET_VALUE)



scopes = [
   'https://graph.microsoft.com/Mail.ReadWrite', 
   'https://graph.microsoft.com/Mail.Send',
   'https://graph.microsoft.com/Calendars.ReadWrite'
]

# account = Account(credentials, scopes=scopes)
# account.authenticate()

protocol = MSGraphProtocol() 
# #protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>') 
# scopes = ['Calendars.Read.Shared']
account = Account(credentials, protocol=protocol)

if account.authenticate(scopes=scopes):
   print('Authenticated!')

schedule = account.schedule()
calendar = schedule.get_default_calendar()

# q = calendar.new_query('start').greater_equal(dt.datetime(2021, 1, 1))
# q.chain('and').on_attribute('end').less_equal(dt.datetime(2021, 12, 12))

daysOftheWeek = ("ISO Week days start from 1",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
                )

subjects = [
   "Rechnerorganisation",
   "Einführung in\ndie Programmierung",
   "Informatik Propädeutikum",
   "Analysis I und\nLineare Algebra",
   "Diskrete Strukturen",
   "Stochastik",
]
locations = [
   "H101",
   "MA01",
   "FT100",
   "A101",
   "C101",
   "H105",
]
os.environ['TZ'] = 'Europe/Berlin'
starts = [
   dt.datetime(2021, 9, 19, 8, 00, 0, 0),
   dt.datetime(2021, 9, 19, 10, 00, 0, 0),
   dt.datetime(2021, 9, 20, 12, 00, 0, 0),
   dt.datetime(2021, 9, 21, 14, 00, 0, 0),
   dt.datetime(2021, 9, 22, 10, 00, 0, 0),
   dt.datetime(2021, 9, 22, 16, 00, 0, 0),
]

for i in range(0, len(subjects)):
   new_event = calendar.new_event()  # creates a new unsaved event 
   new_event.subject = subjects[i]
   new_event.location = locations[i]
   new_event.start = starts[i]
   print(starts[i])
   # so new_event.start becomes: datetime.datetime(2018, 9, 5, 19, 45, tzinfo=<DstTzInfo 'Europe/Paris' CEST+2:00:00 DST>)
   new_event.recurrence.set_weekly(
         interval=1, days_of_week=[daysOftheWeek[starts[i].isoweekday()]], first_day_of_week='Monday', end=dt.datetime(2021, 4, 1))
   new_event.remind_before_minutes = 15

   new_event.save()