import string
import scoring
import s1c1

def byteArrayToString(byteArray):
    return byteArray.decode("utf-8")

def xorByteArrayWithChar(abytearray, char): #Char to byte to xor with byte array
    output = bytearray()
    for a in abytearray:
        output.append(a^char.encode())
    return output

def findCharacter(byteArray):
    topScores = 0
    topArray = ''
    topChar = ''
    for char in string.ascii_lowercase:
        try:
            temp = xorByteArrayWithChar(byteArray, char)
            tempText = byteArrayToString(temp)
            score = scoring.scoreString(tempText)
            if score > topScore:
                topScore = score
                topArray = tempText
                topChar = char
        except Exception:
            continue
    return (topArray, topScore, topChar)

if __name__ == "__main__":
    user_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    topArray, topScore, topChar = findCharacter(s1c1.hexStringToBinaryArray(user_string))
    print(topArray, "\n")
    print(topScore, " : ", topChar)
