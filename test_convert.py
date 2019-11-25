import unittest
import convert


class TestConvertMethods(unittest.TestCase):

    def test_base64_to_bytes(self):
        pass

    def test_bytes_to_base64(self):
        input_byte_array = b"I'm killing your brain like a poisonous mushroom"
        output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(convert.bytes_to_base64(input_byte_array), output)

    def test_bytes_to_string(self):
        pass

    def test_hex_string_to_base64(self):
        input_hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(convert.hex_string_to_base64(input_hex_string), output)

    def test_hex_string_to_bytes(self):
        input_hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        output = b"I'm killing your brain like a poisonous mushroom"
        self.assertEqual(convert.hex_string_to_bytes(input_hex_string), output)

    def test_string_to_byte_array(self):
        pass
    

if __name__ == '__main__':
    unittest.main()
