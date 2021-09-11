import datetime as dt
from O365 import Account, MSGraphProtocol
import pytz
import os

CLIENT_ID = '3a9eef7d-ab34-45f1-a9fd-3780564d7a2e'
SECRET_ID = '<your secret id>'
SECRET_VALUE = 'kpiQvG6_4ovz05n4c7Sn8.KOZE0rT.21s_'

credentials = (CLIENT_ID, SECRET_VALUE)

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
# if account.authenticate(scopes=scopes):

#    schedule = account.schedule()
#    calendar = schedule.get_default_calendar()


#    today = dt.datetime(2021, 10, 10)
#    start = today - dt.timedelta(days=today.weekday())
#    end = start + dt.timedelta(days=6)
#    print("Today: " + str(today))
#    print("Start: " + str(start))
#    print("End: " + str(end))

#    q = calendar.new_query('start').greater_equal(start)
#    q.chain('and').on_attribute('end').less_equal(end)

#    events = calendar.get_events(query=q, include_recurring=True) 
#    print(events)
#    for event in events:
#       print(event)
#       print(event.start.astimezone())

from PIL import Image, ImageDraw, ImageFont
import io
# from app.resources import strings

out = Image.new("1", (800, 480), 255)

# fmb60 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMonoBold.ttf", 60)
# fm30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMono.ttf", 30)
# fmi30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMonoOblique.ttf", 30)
# fmb30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMonoBold.ttf", 30)
# fmi15 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMonoOblique.ttf", 15)

fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 25)
fnt20 = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 20)

# get a drawing context
d = ImageDraw.Draw(out)
# Draw 
# d.line((0, 0, 800, 0), fill=0, width=5)

d1=130 #hard code distance
y1=5   # y position
x1 = 110
d.text((x1+0*d1,y1), "Mon", font=fnt, fill=0)
d.text((x1+1*d1,y1), "Tue", font=fnt, fill=0)
d.text((x1+2*d1,y1), "Wed", font=fnt, fill=0)
d.text((x1+3*d1,y1), "Thurs", font=fnt, fill=0)
d.text((x1+4*d1+20,y1), "Frid", font=fnt, fill=0)
# # ---------------------------------------------
d.line((80, 35, 800, 35), fill=0, width=2)
d.line((80, 35, 80, 480), fill=0, width=2)
# # ---------------------------------------------
d2 = 70
x2=5
y2 = 27
d.text((x2, y2+0*d2), "08:00", font=fnt20, fill=0)
d.text((x2, y2+1*d2), "10:00", font=fnt20, fill=0)
d.text((x2, y2+2*d2), "12:00", font=fnt20, fill=0)
d.text((x2, y2+3*d2), "14:00", font=fnt20, fill=0)
d.text((x2, y2+4*d2), "16:00", font=fnt20, fill=0)
d.text((x2, y2+5*d2), "18:00", font=fnt20, fill=0)
d.text((x2, y2+6*d2), "20:00", font=fnt20, fill=0)
# # ---------------------------------------------
# horizontal
d.line((80, 35+1*d2, 800, 35+1*d2), fill=0, width=1)
d.line((80, 35+2*d2, 800, 35+2*d2), fill=0, width=1)
d.line((80, 35+3*d2, 800, 35+3*d2), fill=0, width=1)
d.line((80, 35+4*d2, 800, 35+4*d2), fill=0, width=1)
d.line((80, 35+5*d2, 800, 35+5*d2), fill=0, width=1)
d.line((80, 35+6*d2, 800, 35+6*d2), fill=0, width=1)
# # ---------------------------------------------
# vertical
d.line((80+1*(d1-0), 35, 80+1*(d1-0), 480), fill=0, width=1)
d.line((80+2*(d1-0), 35, 80+2*(d1-0), 480), fill=0, width=1)
d.line((80+3*(d1-0), 35, 80+3*(d1-0), 480), fill=0, width=1)
d.line((80+4*(d1-0), 35, 80+4*(d1-0), 480), fill=0, width=1)
d.line((80+5*(d1-0), 35, 80+5*(d1-0), 480), fill=0, width=1)
# # ---------------------------------------------
time_range = [8, 10, 12, 14, 16, 18]
for i in range(0, len(subjects)):
    for j in range(len(time_range)-1):
        if starts[i] >= time_range[j] and starts[i] < time_range[j+1]:
            pass
# # ---------------------------------------------




# d.text((5,5), word.word, font=fmb60, fill=0)
# d.text((5,60), word.type, font=fmi30, fill=0)
# d.line((0, 100, 800, 100), fill=0)
# # ---------------------------------------------
# d.text((5,120), word.fullword, font=fm30, fill=0)
# d.multiline_text((5,160), word.content, font=fmb30, fill=0)
# d.line((0, 435, 800, 435), fill=0)
# # ---------------------------------------------
# d.text((5,445), "Last update: " + word.updated_at.strftime("%m/%d/%Y, %H:%M:%S"), font=fmi15, fill=0)

out.show()