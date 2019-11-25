import unittest
import convert
import xor
import cipher


class TestSetOneMethods(unittest.TestCase):

    def test_challenge_one(self):
        string_a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        solution = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(convert.hex_string_to_base64(string_a), solution)

    def test_challenge_two(self):
        string_a = "1c0111001f010100061a024b53535009181c"
        string_b = "686974207468652062756c6c277320657965"
        solution = "746865206b696420646f6e277420706c6179"
        self.assertEqual(xor.two_hex_strings(string_a, string_b).hex(), solution)

    def test_challenge_three(self):
        string_a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        solution_text = "Cooking MC\'s like a pound of bacon"
        solution_key = "X"
        byte_string = convert.hex_string_to_bytes(string_a)
        board = cipher.single_byte_xor(byte_string, 1)
        self.assertEqual(board.top_meta()[0], solution_key)
        self.assertEqual(board.top_meta()[1], solution_text)

    def test_challenge_four(self):
        text_file = open("4.txt", "r")
        board = cipher.single_byte_xor_in_iterable(text_file, 10)
        solution_text = "Now that the party is jumping\n"
        solution_key = "5"
        self.assertEqual(board.top_meta()[0], solution_key)
        self.assertEqual(board.top_meta()[1], solution_text)

    def test_challenge_five(self):
        string_a = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
        key = "ICE"
        input_byte_array = convert.string_to_byte_array(string_a)
        self.assertEqual(xor.byte_array_with_string(input_byte_array, key).hex(), answer)

    def test_challenge_six(self):
        pass
