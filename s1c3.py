import cipher
import convert

if __name__ == "__main__":
    input_a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    input_bytes = convert.hex_string_to_bytes(input_a)
    aScoreboard = cipher.single_byte_xor(input_bytes, 1)
    print(aScoreboard)
