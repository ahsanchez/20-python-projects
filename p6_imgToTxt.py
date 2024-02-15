import pytesseract
import os
from PIL import Image


def convert():
    img = Image.open("descarga.png")
    text = pytesseract.image_to_string(img)
    print(text)


convert()
