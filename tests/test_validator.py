import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("hanif"))

    def test_validate_name_false_with_valid_hanif5(self):
        self.assertEqual(False, validate_name("hanif5"))

    def test_validate_name_false_with_valid_5(self):
        self.assertEqual(False, validate_name("5"))

    def test_validate_name_false_with_valid_specialString(self):
        self.assertEqual(False, validate_name("thitipong#@]"))

    def test_validate_name_false_with_valid_free(self):
        self.assertEqual(False, validate_name(""))

    def test_validate_name_false_with_valid_specString(self):
        self.assertEqual(False, validate_name("thitipong purinsuwan"))

    def test_validate_id_True_with_valid_13(self):
        self.assertEqual(True, validate_id("1234567891123"))

    def test_validate_id_False_with_valid_14(self):
        self.assertEqual(False, validate_id("12345678911234"))

    def test_validate_phone_number_false_with_valid_test01(self):
        self.assertEqual(False, validate_phone_number("test01"))

    def test_validate_phone_number_True_with_valid_0123456789(self):
        self.assertEqual(True, validate_phone_number("0123456789"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
