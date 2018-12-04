import string
import scoring
import s1c1

def byteArrayToString(byteArray):
    try:
        return byteArray.decode("utf-8")
    except Exception:
        return " "

def xorByteArrayWithString(abytearray, string):
    output = bytearray()
    i = 0
    for a in abytearray:
        output.append(a^ord(string[i]))
        i+=1
        i%=len(string)
    return output

def updateTopList(topList, value):
    first = True
    index = len(topList)
    for i in range(index):
        if value > topList[i]:
            if first:
                first = False
                index = i
            value, topList[i] = topList[i], value
    return index

def insertTopList(topList, value, index):
    while index < len(topList):
        value, topList[index] = topList[index], value
        index+=1

def findCharacter(byteArray, top):
    scoreToBeat = 0
    topScores = [0] * top
    topArrays = [''] * top
    topChars = [''] * top
    for i in range(256):
        char = chr(i)
        try:
            temp = xorByteArrayWithString(byteArray, char)
            tempText = byteArrayToString(temp)
            score = scoring.scoreString(tempText)
            if score > scoreToBeat:
                index = updateTopList(topScores, score)
                insertTopList(topArrays, tempText, index)
                insertTopList(topChars, char, index)
        except Exception as e:
            print(e)
            continue
        scoreToBeat = topScores[-1]
    return topArrays, topScores, topChars

if __name__ == "__main__":
    user_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    topArrays, topScores, topChars = findCharacter(s1c1.hexStringToByteArray(user_string), 3)
    for i in range(len(topArrays)):
        print("\n", topArrays[i])
        print("\n| Score: ", topScores[i], "\n| Using: ", topChars[i], "\n------")
