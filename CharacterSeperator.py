class CharacterSeperator:

	"""Splits the captcha into multiple images character by character. Will be replacing the Vertical and Horizontal White Strip detection functions with better ways (a threshold type method perhaps)."""

	def __init__(self,filteredImage):
		self.filteredImage = filteredImage

	def _isVerticalWhiteStrip(self,filteredImage,x):
		for y in range(self.filteredImage.size[1]):
			#iterate over rows
			if(self.filteredImage.getpixel((x,y))==0):
				return False
		return True

	def _isHorizontalWhiteStrip(self,filteredImage,y):
		for x in range(filteredImage.size[0]):
			#iterate over columns
			if(filteredImage.getpixel((x,y))==0):
				return False
		return True

	def _determineBoundary(self):
		#spits out the co-ordinates of vertical lines to seperate the characters
		characterBoundaryList = []
		previousIsWhite = True;
		for x in range(self.filteredImage.size[0]):
			currentIsWhite = self._isVerticalWhiteStrip(self.filteredImage,x)
			if currentIsWhite==False and previousIsWhite==True:
				characterBoundaryList.append(x)
			elif currentIsWhite==True and previousIsWhite==False:
				characterBoundaryList.append(x-1)
			previousIsWhite = currentIsWhite
		return characterBoundaryList

	def _filterLowerAndUpperStrips(self,image):
		#removes the upper and lower white strips in the seperated characters
		previousIsWhite=True
		upperY = 0
		lowerY = image.size[1]-1
		for y in range(image.size[1]):
			currentIsWhite = self._isHorizontalWhiteStrip(image,y)
			if currentIsWhite==False and previousIsWhite==True:
				upperY = y
			elif currentIsWhite==True and previousIsWhite==False:
				lowerY = y-1
			previousIsWhite = currentIsWhite
		return image.crop((0,upperY,image.size[0],lowerY+1))

	def getSeperatedImages(self):
		#returns a list of seperated characters
		boundaryPoints = self._determineBoundary()
		if len(boundaryPoints)%2==1:
			raise ValueError("Odd number of co-ordinates provided. Cannot seperate this image. Filter it further")
		isolatedCharacters = []
		startingPointIndex = 0
		while(startingPointIndex < len(boundaryPoints)):
			endingPointIndex = startingPointIndex+1
			temporaryImage = self.filteredImage.crop((boundaryPoints[startingPointIndex],0,boundaryPoints[endingPointIndex]+1,self.filteredImage.size[1]))
			temporaryImage = self._filterLowerAndUpperStrips(temporaryImage)
			isolatedCharacters.append(temporaryImage)
			startingPointIndex+=2
		return isolatedCharacters