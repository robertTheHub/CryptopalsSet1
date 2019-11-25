class Scoreboard:
    def __init__(self, results=1, variables=tuple(), lowestScore=0):
        self.theRanking = [lowestScore] * results
        self.meta = [[aKey] * results for aKey in variables]

    def scoreToBeat(self):
        return self.theRanking[-1]

    def getSize(self):
        return len(self.theRanking)

    def insertIntoRanking(self, aScore):
        theIndex = self.getSize()
        for aIndex, aRanking in enumerate(self.theRanking):
            if aScore > aRanking:
                if aIndex < theIndex:
                    theIndex = aIndex
                aScore, self.theRanking[aIndex] = self.theRanking[aIndex], aScore
        return theIndex

    def updateMeta(self, aMetaIndex, theIndex, aList):
        if len(aList):
            for anotherIndex, aRanking in enumerate(self.meta[aMetaIndex]):
                if anotherIndex >= theIndex:
                    self.meta[aMetaIndex][anotherIndex] = aList[aMetaIndex]
                    aList[aMetaIndex] = aRanking

    def update(self, aScore, aTuple=tuple()):
        if aScore > self.scoreToBeat():
            theIndex = self.insertIntoRanking(aScore)
            for aMetaIndex in range(len(self.meta)):
                self.updateMeta(aMetaIndex, theIndex, list(aTuple))

    def topScore(self):
        return self.theRanking[0]

    def topMeta(self):
        return [aList[0] for aList in self.meta]

    def __str__(self):
        output = "\n"
        for aIndex, aRanking in enumerate(self.theRanking):
            output += "| Score: " + str(aRanking) + "\n"
            for anotherIndex, aTopic in enumerate(self.meta):
                output += "| Data Point (" + str(anotherIndex) + "): "
                output += str(self.meta[anotherIndex][aIndex]) + "\n"
            output += "------------\n"
        return output
