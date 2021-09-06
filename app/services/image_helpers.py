import io

from PIL import Image, ImageDraw, ImageFont
from fastapi.param_functions import File
from app.models.schemas.words import (
    WordOutWithIdDate
)
from app.resources import strings

""" Return byte buffer if output=='', else export file """
def create_bitmap_from_word(word: WordOutWithIdDate, output=""):

    out = Image.new("1", (800, 480), 255)

    fmb60 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMonoBold.ttf", 60)
    fm30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMono.ttf", 30)
    fmi30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMonoOblique.ttf", 30)
    fm20 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMono.ttf", 30)
    fmi10 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMonoOblique.ttf", 15)

    # get a drawing context
    d = ImageDraw.Draw(out)

    d.text((5,5), word.word, font=fmb60, fill=0)
    d.text((5,60), word.type, font=fmi30, fill=0)
    d.line((0, 100, 800, 100), fill=0)
    # ---------------------------------------------
    d.text((5,120), word.fullword, font=fm30, fill=0)
    d.multiline_text((5,160), word.content, font=fm20, fill=0)
    d.line((0, 435, 800, 435), fill=0)
    # ---------------------------------------------
    d.text((5,445), "Last update: " + word.updated_at.strftime("%m/%d/%Y, %H:%M:%S"), font=fmi10, fill=0)

    if output!="":
        out.save(strings.PATH_STATIC_FOLDER + output)
    else:
        img_byte_arr = io.BytesIO()
        out.save(img_byte_arr, format='bmp')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr

# TODO: improve converting and resizing quality. Check "change" pictures in static folders
# For now, stick with: convert to black-white before POST to server.
# https://stackoverflow.com/questions/46385999/transform-an-image-to-a-bitmap
def process_bitmap_from_file(file: File, output=""):

    out = Image.open(io.BytesIO(file))
    o2 = out.convert('1').resize((800, 480))

    if output!="":
        o2.save(strings.PATH_STATIC_FOLDER + output, format='bmp')
    else:
        img_byte_arr = io.BytesIO()
        o2.save(img_byte_arr, format='bmp')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr