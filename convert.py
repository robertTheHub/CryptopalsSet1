import base64

def hexStringToBytes(hexString):
    return bytes.fromhex(hexString)

def bytesToBase64String(aBytes):
    return base64.b64encode(aBytes)

def hexStringToBase64(aString):
    aBytes = hexStringToBytes(aString)
    return bytesToBase64String(aBytes)    

def stringToByteArray(aString):
    output = bytearray()
    for aLetter in aString:
        output.append(ord(aLetter))
    return output

def bytesToString(aBytes):
    try:
        return aBytes.decode("utf-8")
    except Exception:
        try:
            output = ""
            for aByte in aBytes:
                output += chr(aByte)
            return output
        except Exception:
            return ""        
