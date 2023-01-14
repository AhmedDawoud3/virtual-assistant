from user_data import UserData
import unittest


class User_test(unittest.TestCase):
    def test_get_name(self):
        user_data = UserData()
        self.assertEqual(user_data.get_name(), "Mostafa")

    def test_get_city(self):
        user_data = UserData()
        self.assertEqual(user_data.get_city(), "Kafr El Sheikh")

    def test_get_voice(self):
        user_data = UserData()
        self.assertEqual(user_data.get_voice(), 0)

    # def test_change_name(self):
    #     user_data = UserData()
    #     user_data.set_name("Mohamed")
    #     self.assertEqual(user_data.get_name(), "Mohamed")

    # def test_change_city(self):
    #     user_data = UserData()
    #     user_data.set_city("Cairo")
    #     self.assertEqual(user_data.get_city(), "Cairo")

    # def test_change_voice(self):
    #     user_data = UserData()
    #     user_data.set_voice(0)
    #     self.assertEqual(user_data.get_voice(), 0)


if __name__ == "__main__":
    unittest.main()
