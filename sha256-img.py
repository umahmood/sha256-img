# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os
import random
import hashlib

from PIL import Image, ImageDraw, ImageFont

WIDTH            = 175
HEIGHT           = 325
CHARS_PER_ROW    = 8
FONT_SIZE        = 20
BACKGROUND_COLOR = (52,56,56)

PALLETTE = {'0': (225,128,233),
            '1': (192,90,200),
            '2': (225,77,143),
            '3': (225,77,101),
            '4': (231,33,66),
            '5': (179,5,95),
            '6': (128,107,128),
            '7': (43,221,185),
            '8': (135,161,205),
            '9': (20,206,236),
            'A': (253,210,234),
            'B': (255,77,0),
            'C': (200,255,249),
            'D': (247,254,135),
            'E': (255,0,72),
            'F': (170,255,0)}

def main():
    if len(sys.argv) != 2:
        sys.exit('usage: python sha256-img.py "hello world"')
    text   = sys.argv[1]
    sha256 = hashlib.sha256()
    sha256.update(bytes(text, 'ascii'))
    digest = sha256.hexdigest().upper()
    img    = Image.new(mode='RGBA', size=(WIDTH,HEIGHT), color=BACKGROUND_COLOR)
    path   = os.path.abspath('.')
    font   = ImageFont.truetype(path + '/ttf/Hack-Bold.ttf', FONT_SIZE) 
    draw   = ImageDraw.Draw(img)
    
    x = 10
    y = 10
    for idx, char in enumerate(digest):
        if idx % CHARS_PER_ROW == 0 and idx != 0:
            y += 40
            x = 10
        rgb = PALLETTE[char]
        draw.text((x, y), char, font=font, fill=rgb) 
        x += 20
    filename = text.replace(' ', '-')
    img.save(filename+'.png')

if __name__ == '__main__':
    main()
