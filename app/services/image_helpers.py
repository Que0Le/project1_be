import io

from PIL import Image, ImageDraw, ImageFont
from fastapi.param_functions import File
from app.models.schemas.words import (
    WordOutWithIdDate
)
from app.resources import strings
from typing import List
# import datetime as dt
from O365 import calendar
import textwrap

""" Return byte buffer if output=='__buffer', else export file 'output' @"""
def create_bitmap_from_word(word: WordOutWithIdDate, output="temp.bmp"):

    out = Image.new("1", (800, 480), 255)

    fmb60 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
                               "freemono/FreeMonoBold.ttf", 60)
    fm30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMono.ttf", 30)
    fmi30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
                               "freemono/FreeMonoOblique.ttf", 30)
    fmb30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
                               "freemono/FreeMonoBold.ttf", 30)
    fmi15 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
                               "freemono/FreeMonoOblique.ttf", 15)

    # get a drawing context
    d = ImageDraw.Draw(out)

    d.text((5, 5), word.word, font=fmb60, fill=0)
    d.text((5, 60), word.type, font=fmi30, fill=0)
    d.line((0, 100, 800, 100), fill=0)
    # ---------------------------------------------
    d.text((5, 120), word.fullword, font=fm30, fill=0)
    # d.multiline_text((5, 160), word.content, font=fmb30, fill=0)
    offset = 0
    count = 0
    for line in textwrap.wrap(str(word.content), break_long_words=False, width=43):
        # print(line)
        d.text((5, 160 + offset), line, font=fm30, fill=0)
        offset += fm30.getsize(line)[1]
        count += 1
        if count==9:
            break
    d.line((0, 435, 800, 435), fill=0)
    # ---------------------------------------------
    d.text((5, 445), "Last update: " +
           word.updated_at.strftime("%m/%d/%Y, %H:%M:%S"),
           font=fmi15, fill=0
           )

    if output == "__buffer":
        img_byte_arr = io.BytesIO()
        out.save(img_byte_arr, format='bmp')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
    elif output == "__image_object":
        return out
    else:
        out.save(strings.PATH_STATIC_FOLDER + output)

# TODO: improve converting and resizing quality. Check "change" pictures in static folders
# For now, stick with: convert to black-white before POST to server.
# https://stackoverflow.com/questions/46385999/transform-an-image-to-a-bitmap


def process_bitmap_from_file(file: File, output="temp.bmp"):

    out = Image.open(io.BytesIO(file))
    o2 = out.convert('1').resize((800, 480))

    if output == "__buffer":
        img_byte_arr = io.BytesIO()
        o2.save(img_byte_arr, format='bmp')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
    else:
        o2.save(strings.PATH_STATIC_FOLDER + output, format='bmp')


def create_bitmap_from_calendar(all_events: List[calendar.Event], output="temp.bmp"):
    if len(all_events) == 0:
        return None

    out = Image.new("1", (800, 480), 255)
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 25)
    fnt20 = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 20)
    fnt10 = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 15)

    # get a drawing context
    d = ImageDraw.Draw(out)

    d1 = 130  # hard code distance
    y1 = 5    # y position
    x1 = 110
    d.text((x1 + 0 * d1, y1), "Mon", font=fnt, fill=0)
    d.text((x1 + 1 * d1, y1), "Tue", font=fnt, fill=0)
    d.text((x1 + 2 * d1, y1), "Wed", font=fnt, fill=0)
    d.text((x1 + 3 * d1, y1), "Thurs", font=fnt, fill=0)
    d.text((x1 + 4 * d1 + 20, y1), "Frid", font=fnt, fill=0)
    # # ---------------------------------------------
    d.line((80, 35, 800, 35), fill=0, width=2)
    d.line((80, 35, 80, 480), fill=0, width=2)
    # # ---------------------------------------------
    d2 = 70
    x2 = 5
    y2 = 27
    d.text((x2, y2 + 0 * d2), "08:00", font=fnt20, fill=0)
    d.text((x2, y2 + 1 * d2), "10:00", font=fnt20, fill=0)
    d.text((x2, y2 + 2 * d2), "12:00", font=fnt20, fill=0)
    d.text((x2, y2 + 3 * d2), "14:00", font=fnt20, fill=0)
    d.text((x2, y2 + 4 * d2), "16:00", font=fnt20, fill=0)
    d.text((x2, y2 + 5 * d2), "18:00", font=fnt20, fill=0)
    d.text((x2, y2 + 6 * d2), "20:00", font=fnt20, fill=0)
    # # ---------------------------------------------
    # horizontal lines
    d.line((80, 35 + 1 * d2, 800, 35 + 1 * d2), fill=0, width=1)
    d.line((80, 35 + 2 * d2, 800, 35 + 2 * d2), fill=0, width=1)
    d.line((80, 35 + 3 * d2, 800, 35 + 3 * d2), fill=0, width=1)
    d.line((80, 35 + 4 * d2, 800, 35 + 4 * d2), fill=0, width=1)
    d.line((80, 35 + 5 * d2, 800, 35 + 5 * d2), fill=0, width=1)
    d.line((80, 35 + 6 * d2, 800, 35 + 6 * d2), fill=0, width=1)
    # # ---------------------------------------------
    # vertical lines
    d.line((80 + 1 * (d1 - 0), 35, 80 + 1 * (d1 - 0), 480), fill=0, width=1)
    d.line((80 + 2 * (d1 - 0), 35, 80 + 2 * (d1 - 0), 480), fill=0, width=1)
    d.line((80 + 3 * (d1 - 0), 35, 80 + 3 * (d1 - 0), 480), fill=0, width=1)
    d.line((80 + 4 * (d1 - 0), 35, 80 + 4 * (d1 - 0), 480), fill=0, width=1)
    d.line((80 + 5 * (d1 - 0), 35, 80 + 5 * (d1 - 0), 480), fill=0, width=1)
    # # ---------------------------------------------

    time_range = [8, 10, 12, 14, 16, 18]  # TODO: move to config
    for event in all_events:
        y = -1
        x = -1
        for j in range(len(time_range) - 1):
            if event.start.hour >= time_range[j] and event.start.hour < time_range[j + 1]:
                y = j
                break
        x = event.start.weekday()
        if 0 <= y and y <= 5 and 0 <= x and x <= 4:
            # Now draw this event to timetable
            offset = 0
            for line in textwrap.wrap(event.subject, break_long_words=False, width=11):
                d.text((90 + x * d1, 40 + y * d2 + offset), line, font=fnt10, fill=0)
                offset += fnt10.getsize(line)[1]
            d.text((90 + 30 + x * d1, 87 + y * d2),
                   event.location['displayName'], font=fnt10, fill=0)

    if output == "__buffer":
        img_byte_arr = io.BytesIO()
        out.save(img_byte_arr, format='bmp')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
    else:
        out.save(strings.PATH_STATIC_FOLDER + output, format='bmp')
