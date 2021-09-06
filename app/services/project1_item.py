import io

from PIL import Image, ImageDraw, ImageFont

from app.models.schemas.words import (
    WordOutWithIdDate
)

def create_bitmap_from_word(word: WordOutWithIdDate):

    img_byte_arr = io.BytesIO()
    out = Image.new("1", (800, 480), 255)
    # get a font
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    fnt60 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 60)
    fnt30 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 30)
    fnt20 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 30)
    # get a drawing context
    d = ImageDraw.Draw(out)


    d.text((5,5), word.word, font=fnt60, fill=0)
    d.text((5,60), word.type, font=fnt30, fill=0)
    d.line((0, 100, 800, 100), fill=0)
    # ---------------------------------------------
    d.text((5,120), word.fullword, font=fnt30, fill=0)
    d.multiline_text((5,160), word.content, font=fnt20, fill=0)
    d.line((0, 430, 800, 430), fill=0)
    # ---------------------------------------------
    d.text((5,440), word.updated_at.strftime("%m/%d/%Y, %H:%M:%S"), font=fnt30, fill=0)
    # out.save('static/pil_text.bmp')
    #out.show()

    out.save(img_byte_arr, format='bmp')
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr