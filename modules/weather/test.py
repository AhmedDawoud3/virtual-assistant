from weather import Weather
import unittest


class Weather_Test(unittest.TestCase):
    def test_with_invalid_city(self):
        self.assertEqual(Weather("kefr el-shoulk"),
                         "Sorry, Couldn't get weather")

    def test_with_valid_city(self):
        self.assertNotEqual(Weather("kafr El Sheikh"),
                            "Sorry, Couldn't get weather")

    def test_with_another_valid_city(self):
        self.assertNotEqual(Weather("Cairo"),
                            "Sorry, Couldn't get weather")


if __name__ == "__main__":
    unittest.main()
