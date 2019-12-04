import unittest
import cipher


class TestCipherMethods(unittest.TestCase):

    def test_string_hamming_distance(self):
        string_a = "this is a test"
        string_b = "wokka wokka!!!"
        self.assertEqual(cipher.hamming_distance_of_strings(string_a, string_b), 37)

    @unittest.skip("Unwritten Test")
    def test_byte_hamming_distance(self):
        pass

    @unittest.skip("Unwritten Test")
    def test_single_byte_xor(self):
        pass

    @unittest.skip("Unwritten Test")
    def test_single_byte_xor_in_byte_array(self):
        pass

    @unittest.skip("Unwritten Test")
    def test_single_byte_xor_in_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
