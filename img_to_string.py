from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

from pytesseract import image_to_string
Img = Image.open('sample.png'); 
txt = image_to_string(Img);
print(txt);
