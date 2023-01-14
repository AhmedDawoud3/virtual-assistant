import unittest
from brightness import Brightness


class ModelTest(unittest.TestCase):
    def test_brightness_increase(self):
        brightness = Brightness()
        self.assertTrue(brightness.increase())

    def test_brightness_decrease(self):
        brightness = Brightness()
        self.assertTrue(brightness.decrease())

    def test_brightness_maximum(self):
        brightness = Brightness()
        self.assertTrue(brightness.maximum())

    def test_brightness_minimum(self):
        brightness = Brightness()
        self.assertTrue(brightness.minimum())

    def test_get_brightness(self):
        brightness = Brightness()
        self.assertEqual(brightness.get_current_value(), 0)


if __name__ == "__main__":
    unittest.main()
