import cipher
import convert

if __name__ == "__main__":
    string_a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    byte_string = convert.hex_string_to_bytes(string_a)
    board = cipher.single_byte_xor(byte_string, 1)
    print(board)
