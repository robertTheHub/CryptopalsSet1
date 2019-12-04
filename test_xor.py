import unittest
import xor


class TestXORMethods(unittest.TestCase):

    def test_two_bytes(self):
        byte_a = b"a"
        byte_b = b"a"
        solution = b"\x00"
        self.assertEqual(xor.two_bytes(byte_a, byte_b), solution)

    def test_two_hex_strings(self):
        string_a = "1c0111001f010100061a024b53535009181c"
        string_b = "686974207468652062756c6c277320657965"
        solution = b"the kid don\'t play"
        self.assertEqual(xor.two_hex_strings(string_a, string_b), solution)

    @unittest.skip("Unwritten Test")
    def test_byte_array_with_string(self):
        pass

