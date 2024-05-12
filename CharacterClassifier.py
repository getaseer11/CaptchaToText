from CharacterSeperator import *
from CaptchaTextFilter import *
from VectorSpace import *
import os
from operator import itemgetter

class CharacterClassifier:

	DATA_DIRECTORY = "./trainingData/"

	def __init__(self,image):
		self.vectorSpace = VectorSpace(image)
		self.image = image

	def getCharacterProbabilityList(self):

		probabilityDict = {}
		for f in os.listdir(self.DATA_DIRECTORY):
			try:
				os.listdir(self.DATA_DIRECTORY+f)
			except OSError:
				continue
			for x in os.listdir(self.DATA_DIRECTORY+f):
				im = Image.open(self.DATA_DIRECTORY+f+"/"+x)
				cosineSimilarity = self.vectorSpace.cosine(VectorSpace(im))
				if probabilityDict.has_key(f):
					probabilityDict[f]=max(probabilityDict[f],cosineSimilarity)
				else:
					probabilityDict[f]=cosineSimilarity
		characterProbabilityList = []
		for j,k in sorted(probabilityDict.items(), key=itemgetter(1), reverse=True)[:10]:
			characterProbabilityList.append((j,k))
		return characterProbabilityList