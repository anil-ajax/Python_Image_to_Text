## Language translation using Python and Pytesseract library
* Following steps have been executed on Windows 10 with Python 3.7 and Translate
Step 1: Install PIP
Install PIP if you don’t have already. To install PIP follow step 2 in this document
http://rsyspedia.india.rsystems.com/Knowledge%20Library/Information%20Technology/PythanAndDjangoSetUp.pdf

## Step 2: Install PIL and Pytesseract
pip install Pytesseract
Another librabry called PIL or pillow is also needed which now a days comes bundled with Pytesseract itself. So no need to install separately. 

## Step 3: Write image to text conversion script
from PIL import Image
from pytesseract import image_to_string
Img = Image.open(‘<image path here>’); 
txt = image_to_string(Img);
print(txt);

## Note: on windows if you face module not found error for tesseract please download and install tesseract ocr from http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
Then add these two lines in your script

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract' 
So finally the script looks like
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from pytesseract import image_to_string
Img = Image.open('sample.png'); 
txt = image_to_string(Img);
print(txt);

## Step 4: Test your script
python img_to_string.py



