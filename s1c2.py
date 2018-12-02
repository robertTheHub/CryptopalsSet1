from s1c1 import *

def xorByteArrays(abytearray, bbytearray):
    output = bytearray()
    for a,b in zip(abytearray, bbytearray):
        output.append(a^b)
    return output

if __name__ == "__main__":
    astring = "1c0111001f010100061a024b53535009181c"
    bstring = "686974207468652062756c6c277320657965"
    answer = "746865206b696420646f6e277420706c6179"

    abyte = hexStringToByteArray(astring) 
    bbyte = hexStringToByteArray(bstring)
    xored = xorByteArrays(abyte,bbyte)
    print(xored.hex() == answer)
