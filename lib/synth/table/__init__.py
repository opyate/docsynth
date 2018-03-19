import random
from PIL import Image, ImageColor, ImageFont, ImageDraw
import numpy as np
import string
from lib.assets import get_random_font

letters = set()
letters.update(list(string.ascii_letters))

numbers = set(list(string.digits))


def draw_text_on_img(img, cells, config, cellw):
    # config not used currently, since we're now using our internal fonts
    font = get_random_font()
    print('font', font)
    scribble(img, font, cells, cellw)

def scribble(img, font_path, cells, cellw):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 16)
    for cell in cells:
        x = cell[0]
        y = cell[1]

        cap = max(int(cellw/12), 6)
        #cap = int(cellw/12)
        stufflen = random.randint(5,cap)

        stuff = ''.join(random.sample(letters, stufflen))
        draw.text((x + 5, y), stuff, (0, 0, 0), font=font)

def get(img, yoffset, config, maxwidth=580):
    draw = ImageDraw.Draw(img)
    rows = random.randint(4,10)
    cols = random.randint(2,7)
    cellh = 20 + random.randint(0,10)
    yoffset = yoffset + random.randint(15,30)
    xoffset = random.randint(15,30)
    cellw = int((maxwidth - random.randint(xoffset,200)) / cols)
    cells = []
    if random.randint(0,1) == 0:
        cellborder = "white"
        boundingborder = "black"
    else:
        cellborder = "black"
        boundingborder = "white"

    altbg = (
        random.randint(128,255),
        random.randint(128,255),
        random.randint(128,255),
    )
    altbg_enabled = random.randint(0,1) == 0

    for y in range(rows):
        for x in range(cols):
            xx = x * cellw + xoffset
            yy = y * cellh + yoffset
            if y % 2 == 0 and altbg_enabled:
                fill = altbg
            else:
                fill = None

            draw.rectangle((xx, yy, xx + cellw, yy + cellh), outline=cellborder, fill=fill)
            cells.append([xx, yy, cellw, cellh])

    # bounding box
    [print(cell) for cell in cells]
    cells = np.array(cells)
    bx = np.min(cells[:,0])
    by = np.min(cells[:,1])
    bw = np.sum(cells[:cols,2])
    bh = np.sum(cells[:rows,3])
    bounding = [bx, by, bw, bh]
    print('bounding', bx, by, bw, bh)
    draw.rectangle((bx, by, bx + bw, by + bh), outline=boundingborder)

    # text
    draw_text_on_img(img, cells, config, cellw)


    return cells, bounding
