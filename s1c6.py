import convert


def rawHammingDistance(byte1, byte2):
    total = 0
    for a,b in zip(byte1, byte2):
        total += bin(a^b).count("1")
    return total

def hammingDistance(string1, string2):
    total = 0
    for a,b in zip(string1, string2):
        total += bin(ord(a)^ord(b)).count("1")
    return total    

def createArrays(block, size):
    array = []
    count = 0
    temp = bytearray()
    for byte in block:
        count += 1
        temp.append(byte)
        if count == size:
            count = 0
            array.append(temp)
            temp = bytearray()
    return array

def transpose(array):
    outside = len(array)
    inside = len(array[0])
    print(outside, inside)
    tarray = []
    temp = bytearray()
    for i in range(inside):
        for j in range(outside): 
            temp.append(array[j][i])
        tarray.append(temp)
        temp = bytearray()
    return tarray

if __name__ == "__main__":
    string1 = "this is a test"
    string2 = "wokka wokka!!!"

    answer = hammingDistance(string1, string2)
    print("First test: ", answer == 37, answer, "\n")
    
    block = ""
    with open("6.txt", "r") as theBlock:
        block = convert.base64_to_byte_array(theBlock.read())
    total = 4
    
    topDist = [-1000] * total
    topSize = [-1000] * total
    best = -1000

    for key in range(2, 41):
        dist = rawHammingDistance(block[:key], block[key:2*key])
        dist2 = rawHammingDistance(block[2*key:3*key], block[3*key:4*key])
        avg = -((dist)/ (key))
        if avg > best:
            index = s1c3.updateTopList(topDist, avg)    
            s1c3.insertTopList(topSize, key, index)
            best = topDist[-1]    
    for i in range(4):
        print(i+1, "th Place", "\n| Distance: ", -topDist[i], "\n| KeySize: ", topSize[i], "\n\n---------") 

    arrays = transpose(createArrays(block, 2))
    for series in arrays:
        a,b,c = s1c3.findCharacter(series, 3)
        print(a,c)
        print("----------------------------")
