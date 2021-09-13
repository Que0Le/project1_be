import datetime as dt
from O365 import Account, MSGraphProtocol
import pytz
import os
from PIL import Image, ImageDraw, ImageFont
import io
import textwrap
# from app.resources import strings

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
   "Rechner organisation",
   "Einführung in die Programmierung",
   "Informatik Propädeutikum",
   "Analysis I und Lineare",
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
   dt.datetime(2021, 10, 4, 8, 00, 0, 0),
   dt.datetime(2021, 10, 4, 10, 00, 0, 0),
   dt.datetime(2021, 10, 5, 12, 00, 0, 0),
   dt.datetime(2021, 10, 6, 14, 00, 0, 0),
   dt.datetime(2021, 10, 7, 10, 00, 0, 0),
   dt.datetime(2021, 10, 8, 16, 00, 0, 0),
]

scopes = [
   'https://graph.microsoft.com/Mail.ReadWrite', 
   'https://graph.microsoft.com/Mail.Send',
   'https://graph.microsoft.com/Calendars.ReadWrite'
]


out = Image.new("1", (800, 480), 255)
fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 25)
fnt20 = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 20)
fnt10 = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 15)

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
    print(starts[i].hour)
    y=-1
    x=-1
    for j in range(len(time_range)-1):
        if starts[i].hour >= time_range[j] and starts[i].hour < time_range[j+1]:
            y=j
            break
    x = starts[i].weekday()
    if 0<=y and y<=5 and 0<=x and x<=4:
        # Now we draw to timetable
        # d.text((90+x*d1, 40+y*d2), subjects[i], font=fnt10, fill=0)
        offset = 0
        for line in textwrap.wrap(subjects[i], break_long_words=False, width=11):
            print(line)
            d.text((90+x*d1, 40+y*d2+offset), line, font=fnt10, fill=0)
            offset += fnt10.getsize(line)[1]
        d.text((90+30+x*d1, 87+y*d2), locations[i], font=fnt10, fill=0)

out.show()