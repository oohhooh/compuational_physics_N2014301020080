from PIL import Image
import sys

def rgb2level(color_rgb):
    return color_rgb[0]*0.229 + color_rgb[1]*0.587 + color_rgb[2]*0.114

def binaryzation_yui(image, threshold=190):
    pixel_access = image.load()
    
    width, height = image.size
    for w in range(width):
        for h in range(height):
            if rgb2level(pixel_access[w, h])<threshold:
                pixel_access[w, h] = (0, 0, 0)
            else:
                pixel_access[w, h] = (255, 255, 255)
    return image

def print_(string):
    sys.stdout.write(string)

def creat_cache(path):
    image = Image.open(path)
    image = binaryzation_yui(image)
    pixel = image.load()
    width,height = image.size
    cache__ = ''
    for h in range(height):
        for w in range(width):
            if pixel[w, h][0]==0:
                cache__+='  '
            else:
                cache__+='..'
        cache__+='\n'
    return cache__

import os
import time

def play(cache, sleep=0.1):
    for i in cache:
        print (i)
        time.sleep(sleep)
        os.system('cls')

list_ = os.listdir('233.gif.ifl')
caches = []
for i in list_:
    path = '233.gif.ifl'+os.sep+i
    caches.append(creat_cache(path))

while True:
    play(caches)