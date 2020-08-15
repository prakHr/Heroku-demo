import os
import gradio as gr
import barcode
from barcode.writer import ImageWriter
import time

from PIL import Image
from skimage.io import imread
from skimage.util import img_as_ubyte
import os
import time
'''
def greet(name):
    return "Hello "+name+"!"
gr.Interface(fn=greet,inputs="text",outputs="text").launch()
'''
def print_barcode(barcode_Name):
    Code_128="code128"
    ean=barcode.get(Code_128,barcode_Name,writer=ImageWriter())
    f=ean.save("C:\\Users\\HP\\Desktop\\Heroku-Demo\\static\\people_photo\\"+barcode_Name)
    sk_image=imread(f)
    image=img_as_ubyte(sk_image)
    return image
gr.Interface(fn=print_barcode,inputs="text",outputs="image").launch()

