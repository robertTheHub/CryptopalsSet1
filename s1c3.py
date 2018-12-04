import cipher
import convert

if __name__ == "__main__":
    aString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    
    aBytes = convert.hexStringToBytes(aString) 
    aScoreboard = cipher.singleByteXOr(aBytes, 1)

    print(aScoreboard)
