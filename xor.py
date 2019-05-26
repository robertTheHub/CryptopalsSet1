import convert

def theseBytes(aBytes, anotherBytes):
    output = bytearray()
    for a,b in zip(aBytes, anotherBytes):
        output.append(a^b)
    return output

def hexStrings(aString, anotherString):
    aBytes = convert.hexStringToBytes(aString) 
    anotherBytes = convert.hexStringToBytes(anotherString)
    output = theseBytes(aBytes,anotherBytes)
    return output

def bytesWithString(aByteArray, aString):
    anotherByteArray = convert.stringToByteArray(aString)
    aRemainder = len(aByteArray) % len(aString)
    aDivisor = len(aByteArray) // len(aString)
    anotherByteArray = anotherByteArray[:] * aDivisor + anotherByteArray[:aRemainder]
    return theseBytes(aByteArray, anotherByteArray)
