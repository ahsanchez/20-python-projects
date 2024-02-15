import pytesseract
import os
from PIL import Image


def convert():
    img = Image.open("ocr-img-example.jpg")
    text = pytesseract.image_to_string(img)
    print(text)


convert()
