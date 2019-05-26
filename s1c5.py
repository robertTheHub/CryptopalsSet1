import s1c3

def stringToByteArray(string):
    s = bytearray()
    for char in string:
        s.append(ord(char))
    return s

if __name__ == "__main__":
    answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    hashable = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    hashable = stringToByteArray(hashable)
    print(s1c3.xorByteArrayWithString(hashable, "ICE").hex() == answer)    
