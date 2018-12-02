import base64

def hexStringToByteArray(hexString):
    return bytes.fromhex(hexString)

def byteArrayToB64String(byteArray):
    return base64.b64encode(byteArray)

if __name__ == "__main__":
    user_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    answer = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print(byteArrayToB64String(hexStringToByteArray(user_string))==answer)

