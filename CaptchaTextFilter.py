from PIL import Image

class CaptchaTextFilter:

	def __init__(self,redThreshold=(78,255),blueThreshold=(0,60),greenThreshold=(0,60)):
		self.redThreshold = redThreshold
		self.greenThreshold = greenThreshold
		self.blueThreshold = blueThreshold

	def processImage(self,imageFile):
		if type(imageFile)==type(""):
			inputImage = Image.open(imageFile)
		else:
			inputImage = imageFile
		outputImage = Image.new("P",inputImage.size,255)
		for x in range(inputImage.size[1]):
			for y in range(inputImage.size[0]):
 				pix = inputImage.getpixel((y,x))
				if pix[0]>=self.redThreshold[0] and pix[0]<=self.redThreshold[1] and pix[1]>=self.greenThreshold[0] and pix[1]<=self.greenThreshold[1] and pix[2]>=self.blueThreshold[0] and pix[2]<=self.blueThreshold[1]:
					outputImage.putpixel((y,x),0)
		return outputImage