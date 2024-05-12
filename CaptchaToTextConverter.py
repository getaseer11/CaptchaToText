from PIL import Image
from CharacterSeperator import *
from CaptchaTextFilter import *
from VectorSpace import *
from CharacterClassifier import *

class CaptchaToTextConverter:
    def __init__(self,inputImage):
        self.inputImage = inputImage
        self.outputText = None
        self.everyCharacterProbabilityList = None

    def getText(self,debug = False):
        if self.outputText==None:
            captchaTextFilter = CaptchaTextFilter()
            noiseRemovedImage = captchaTextFilter.processImage(self.inputImage)
            characterSeperator = CharacterSeperator(noiseRemovedImage)
            seperatedCharactersImages = characterSeperator.getSeperatedImages()
            self.everyCharacterProbabilityList = []
            self.outputText = ""
            for characterImage in seperatedCharactersImages:
                characterClassifier = CharacterClassifier(characterImage)
                characterProbabilityList = characterClassifier.getCharacterProbabilityList()
                self.everyCharacterProbabilityList.append(characterProbabilityList)
                self.outputText+=characterProbabilityList[0][0]
            if debug:
                # noiseRemovedImage.show()
                for i in range(len(self.everyCharacterProbabilityList)):
                    print "%d th character " %i
                    for j in range(len(self.everyCharacterProbabilityList[i])):
                        print self.everyCharacterProbabilityList[i][j]
                    print "="*20
        return self.outputText