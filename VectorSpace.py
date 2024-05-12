import math
from PIL import Image
class VectorSpace:

	def __init__(self):
		return

	def __init__(self,imageData):
		self.imageData = imageData
		self._preprocess()

	def _preprocess(self):
		#changes the image in the form a binary matrix of 1s(text) and 0s(background)
		for i in range(self.imageData.size[1]):
			for j in range(self.imageData.size[0]):
				if(self.imageData.getpixel((j,i))==0):
					self.imageData.putpixel((j,i),1)
				else:
					self.imageData.putpixel((j,i),0)

	def printData(self):
		#prints the data in matrix form
		for i in range(self.imageData.size[1]):
			for j in range(self.imageData.size[0]):
				print "%d" %(self.imageData.getpixel((j,i))),
			print ""

	def _dot(self,v):
		#vector dot product implementation
		dotProduct = 0
		for i in range(max(self.imageData.size[1],v.imageData.size[1])):
			for j in range(max(self.imageData.size[0],v.imageData.size[0])):
				try:
					dotProduct+=self.imageData.getpixel((j,i))*v.imageData.getpixel((j,i))
				except IndexError:
					dotProduct+=0
		return dotProduct

	def magnitude(self,v):
		#second argument might not be needed, might remove it
		result = 0
		for i in range(max(self.imageData.size[1],v.imageData.size[1])):
			for j in range(max(self.imageData.size[0],v.imageData.size[0])):
				try:
					result+=self.imageData.getpixel((j,i))
				except IndexError:
					result+=0
		return math.sqrt(result)

	def cosine(self,v):
		#cosine projection used to find out similarity of text
		numerator = self._dot(v)
		magnitudeSelf = self.magnitude(v)
		magnitudeV = v.magnitude(self)
		result  = numerator / (magnitudeSelf * magnitudeV)
		return result