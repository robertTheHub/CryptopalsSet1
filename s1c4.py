import cipher

if __name__ == "__main__":
    aText = open("4.txt","r")
    
    aScoreboard = cipher.singleByteXOrInIterable(aText, 10)
   
#    print(aScoreboard)
