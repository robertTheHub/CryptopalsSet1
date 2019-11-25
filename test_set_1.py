import unittest
import convert

class TestSetOneMethods(unittest.TestCase):

    def test_challenge_one(self):
        input_a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        solution = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(convert.hex_string_to_base64(input_a), solution)