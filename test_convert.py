import unittest
import convert


class TestConvertMethods(unittest.TestCase):

    def test_hex_string_to_bytes(self):
        input = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        output = b"I'm killing your brain like a poisonous mushroom"
        self.assertEqual(convert.hex_string_to_bytes(input), output)

    # Set 1 Challenge 1
    def test_hex_string_to_base64(self):
        input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(convert.hex_string_to_base64(input), output)

    def test_bytes_to_base64(self):
        input = b"I'm killing your brain like a poisonous mushroom"
        output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(convert.hex_string_to_base64(input), output)


if __name__ == '__main__':
    unittest.main()
