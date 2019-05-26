import convert
import xor
import scoreboard
import scoring

def singleByteXOr(aBytes, results=1):
    aScoreboard = scoreboard.Scoreboard(results, ("Guess", "Result"))
    for i in range(256):
        aChar = chr(i)
        aBytes = xor.bytesWithString(aBytes, aChar)
        aString = convert.bytesToString(aBytes)
        aScore = scoring.scoreString(aString)
        print(aString)
        aScoreboard.update(aScore, (aChar, aString))       
    return aScoreboard
    
def singleByteXOrInIterable(aIterable, results=1):
    aScoreboard = scoreboard.Scoreboard(results, ("Guess", "Result"))
    if True: #for aLine in aIterable
        aLine = aIterable.readlines()[171].strip()
        aBytes = convert.hexStringToBytes(aLine)
        anotherScoreboard = singleByteXOr(aBytes, 10)
#        aScoreboard.update(anotherScoreboard.topScore(), anotherScoreboard.topMeta())
        print(anotherScoreboard)
    return aScoreboard

