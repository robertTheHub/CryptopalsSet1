import cipher

if __name__ == "__main__":
    input_text = open("4.txt", "r")

    aScoreboard = cipher.single_byte_xor_in_iterable(input_text, 10)
#    print(aScoreboard)
