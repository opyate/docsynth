import random
import os
import glob
from PIL import Image, ImageColor, ImageFont, ImageDraw

from lib.assets import get_random_prefab_text, get_random_font

def draw_text_on_img(img, text, config):
    font = get_random_font()
    print('font', font)
    scribble(img, font, text)

def scribble(img, font_path, text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 16)
    draw.text((10, 10), text, (0, 0, 0), font=font)

def random_font(fontsarr):
    # TODO weighted towards "common" fonts?
    return random.choice(fontsarr)


def get(maxwidth=580):
    imgpath = get_random_prefab_text()
    img = Image.open(imgpath)
    width, height = img.size

    # resize
    newwidth = maxwidth - random.randint(0,100)
    if width > newwidth:
        ratio = (newwidth/float(width))
        newheight = int((float(height)*float(ratio)))
        img_resized = img.resize((newwidth, newheight), Image.ANTIALIAS)
    else:
        # do not inflate
        newwidth = width
        newheight = height
        img_resized = img



    return {
        'original': {
            'img': img,
            'w': width,
            'h': height,
        },
        'resized': {
            'img': img_resized,
            'w': newwidth,
            'h': newheight,
        }
    }
