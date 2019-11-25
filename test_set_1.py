import unittest
import convert
import xor


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
