from splinter import Browser
import time
import os
from PIL import Image
from CharacterSeperator import *
from CaptchaTextFilter import *
from CaptchaToTextConverter import *
IMAGE_FILE_NAME = 'test_image.jpg'

def getCaptcha():
	os.system("wget 'http://www.indianrail.gov.in/captcha_code_file.php?rand=%3C?php%20echo%20rand();%20?%3E' -O  "+IMAGE_FILE_NAME)
	image = Image.open(IMAGE_FILE_NAME)
	image.show()
	c = CaptchaToTextConverter(image)
	text = c.getText()
	print text
	return text

getCaptcha()