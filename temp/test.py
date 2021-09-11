
from PIL import Image, ImageDraw, ImageFont
import io

file = "../static/change_original.png"
threshold = 110

# convert image to a list of pixels
img = Image.open(file)
pixels = list(img.getdata())

# convert data list to contain only black or white
newPixels = []
for pixel in pixels:
    # if looks like black, convert to black
    if pixel[0] <= threshold:
        newPixel = (0, 0, 0)
    # if looks like white, convert to white
    else:
        newPixel = (255, 255, 255)
    newPixels.append(newPixel)

# create a image and put data into it
newImg = Image.new(img.mode, img.size)
newImg.putdata(newPixels)
# newImg.save('new-letter.jpg')
newImg.show()
# with open("../static/change_original.png", 'rb') as file:
#     out = Image.open(file)
#     o2 = out.resize((800, 480)).convert('1')
#     # o2.save('../static/tu.bmp')
#     o2.show()
#     # out.save('../static/tu.bmp')
#     # out.show()
exit()

id="id"
word="word"
type="type"
fullword="fullword"
content="content-skafnbka-sfkn3=fmwoeif\niwhrffhwesefowofw-ffwo\nefnskefnsfknufhu2fhesiofne"
created_at="created_at"
updated_at="updated_at"

# create an image
out = Image.new("1", (800, 480), 255)
img_byte_arr = io.BytesIO()
# get a font
fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
fnt60 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 60)
fnt30 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 30)
fnt20 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 30)
# get a drawing context
d = ImageDraw.Draw(out)


d.text((5,5), word, font=fnt60, fill=0)
d.text((5,60), type, font=fnt30, fill=0)
d.line((0, 100, 800, 100), fill=0)
# ---------------------------------------------
d.text((5,120), fullword, font=fnt30, fill=0)
d.multiline_text((5,160), content, font=fnt20, fill=0)
d.line((0, 430, 800, 430), fill=0)
# ---------------------------------------------
d.text((5,440), updated_at, font=fnt30, fill=0)

# draw multiline text
# d.multiline_text((20,20), "Hello\nWorld", font=fnt, fill=0)
# d.line((0, 0) + (800, 480), fill=0)
# d.line((0, 480, 800, 0), fill=0)

out.save(img_byte_arr, format='bmp')
img_byte_arr = img_byte_arr.getvalue()
print(img_byte_arr)
# out.save('static/pil_text.bmp')

out.show()

# img.save('static/pil_text.png')