from lib import *
import random
import argparse
import sys
import numpy as np
import traceback

from PIL import Image, ImageColor, ImageFont, ImageDraw


def gen(conf=None):
    #  (8.5 x 11 inches) to 612 x 792 pixels
    size = (612, 792)
    color = (255, 255, 255)
    img = Image.new("RGB", size, color)
    vertleft = 792

    # text
    #draw_text_on_img(img, 'hello world isnt it great\n'*10, conf)
    # PIL.Image.FLIP_LEFT_RIGHT, PIL.Image.FLIP_TOP_BOTTOM
    txt = get_text(maxwidth=580)['resized']
    txtimg = txt['img'].convert("RGB")
    x = 20
    y = 50
    vertleft -= 50
    img.paste(txtimg, (x, y, x + txt['w'], y + txt['h']))

    # table
    cells, bounding = get_table(img, y + txt['h'], conf, maxwidth=580)
    bh = bounding[3] + txt['h'] + random.randint(20,40)
    vertleft -= bh

    y = y + bh
    # more text
    while vertleft > 0:
        txt2 = get_text(maxwidth=580)['resized']
        txt2img = txt2['img'].convert("RGBA")
        vertleft -= txt2['h']
        if y + txt2['h'] < 792 and x + txt2['w'] < 612:
            print('y', y, 'next height', txt2['h'], 'sum', y + txt2['h'])
            print('x', x, 'next width', txt2['w'], 'sum', x + txt2['w'])
            img.paste(txt2img, (x, y, x + txt2['w'], y + txt2['h']))
        y += txt2['h']

    # verify cells
    if False:
        draw = ImageDraw.Draw(img)
        for cell in cells:
            x = cell[0]
            y = cell[1]
            w = cell[2]
            h = cell[3]
            draw.rectangle((x, y, x + w, y + h), outline='pink', fill=None)


    return img, cells

def generator(batch_size=1000):
    while True:
        imgs = []
        tables = []
        while len(imgs) < batch_size:
            try:
                img, cells = gen()
                imgs.append(img)
                tables.append(cells)
            except:
                traceback.print_exc(file=sys.stderr)
                sys.stderr.flush()

        yield (imgs, tables)


def save_image(img, file_path, image_type=None):
    if image_type:
        img.save(file_path, image_type)
    else:
        img.save(file_path)
    print('image saved', file_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fonts', '-f', dest="fonts", type=str, help="Space-delimited font locations")
    args = parser.parse_args()

    img, cells = gen(config(args))
    path = './out.png'
    save_image(img, path)

if __name__ == '__main__':
    main()
