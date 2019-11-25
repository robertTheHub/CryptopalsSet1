import xor


if __name__ == "__main__":
    string_a = "1c0111001f010100061a024b53535009181c"
    string_b = "686974207468652062756c6c277320657965"
    solution = "746865206b696420646f6e277420706c6179"

    answer = xor.two_hex_strings(string_a, string_b).hex()
    print(answer == solution)
