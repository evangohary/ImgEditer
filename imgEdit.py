from importlib.resources import path
from math import factorial
from PIL import Image, ImageEnhance, ImageFilter
import os

path = './img'
pathOut = './ImgEditer'

for filename in os.listdir(path): # opens images in folder
   img = Image.open(f"{path}/{filename}")

   edit = img.filter(ImageFilter.SHARPEN).convert('L')

   factor = 1.5
   enhancer = ImageEnhance.Contrast(edit)
   edit = enhancer.enhance(factor)

   clean_name = os.path.splitext(filename)[0]

   edit.save(f'.{pathOut}/{clean_name}_edited.jpg')