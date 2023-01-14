from modules.model import Model
import unittest
from time import strftime


class ModelTest(unittest.TestCase):
    def test_calculator_1(self):
        model = Model()
        self.assertEqual(model.process("3 + 4"), "The answer is 7")

    def test_calculator_2(self):
        model = Model()
        self.assertEqual(model.process("square root 9"), "The answer is 3")

    def test_calculator_3(self):
        model = Model()
        self.assertEqual(model.process("9 / 5"), "The answer is 1.800")

    def test_calculator_division_error(self):
        model = Model()
        self.assertEqual(model.process("9 / 0"), "): Can't divide by zero")

    def test_calculator_expression_error(self):
        model = Model()
        self.assertEqual(model.process("9 * + / 0"), None)

    def test_weather(self):
        model = Model()
        self.assertIsNotNone(model.process("What is the weather"))

    def test_date(self):
        model = Model()
        self.assertEqual(model.process("What is th date"),
                         f"Today is {strftime('%A')} {int(strftime('%d'))} {strftime('%B')} {strftime('%Y')}")

    def test_time(self):
        model = Model()
        self.assertEqual(model.process("What is the time"),
                         f"It's {int(strftime('%I'))} {int(strftime('%M'))} {strftime('%p')}")

    def test_pray(self):
        model = Model()
        self.assertRegex(model.process("What is the next pray"),
                         "[0-9]{1}|[0-9]{2} hours [0-9]{1}|[0-9]{2} minutes left for Al [a-zA-Z]*")

    def test_open_chrome(self):
        model = Model()
        self.assertTrue(model.process("open Chrome"))

    # def test_open_firefox(self):
    #     model = Model()
    #     self.assertTrue(model.process("open firefox"))

    # def test_open_facebook(self):
    #     model = Model()
    #     self.assertTrue(model.process("open facebook"))

    # def test_close_firefox(self):
    #     model = Model()
    #     model.process("open firefox")
    #     self.assertTrue(model.process("close firefox"))
    #     self.assertFalse(model.process("close nothing"))

    # def test_close_chrome(self):
    #     model = Model()
    #     model.process("open chrome")
    #     self.assertTrue(model.process("close chrome"))
    #     self.assertFalse(model.process("close nothing"))

    # def test_shutdown_timer(self):
    #     model = Model()
    #     self.assertTrue(model.process("shutdown after 3 hours and 30 minutes"))

    # def test_shutdown(self):
    #     model = Model()
    #     self.assertTrue(model.process("shutdown"))

    # def test_restart_timer(self):
    #     model = Model()
    #     self.assertTrue(model.process("restart after 3 hours and 30 minutes"))

    def test_wiki_search_1(self):
        model = Model()
        self.assertTrue(model.process("what's facebook"))

    def test_wiki_search_2(self):
        model = Model()
        self.assertTrue(model.process("what is facebook"))

    def test_wiki_search_with_wrong_word(self):
        model = Model()
        self.assertTrue(model.process("what is nltk"))

    # def test_wiki_search_with_meaningless_word(self):
    #     model = Model()
    #     self.assertFalse(model.process("what is sjiaewa"))

    def test_wiki_search_with_who_is(self):
        model = Model()
        self.assertTrue(model.process("who is mark zuckerberg"))

    def test_google_search(self):
        model = Model()
        self.assertTrue(model.process("google ai"))

    # def test_brightness_increase(self):
    #     model = Model()
    #     self.assertTrue(model.process("increase brightness"))

    # def test_brightness_decrease(self):
    #     model = Model()
    #     self.assertTrue(model.process("decrease brightness"))

    # def test_brightness_maximum(self):
    #     model = Model()
    #     self.assertTrue(model.process("maximum brightness"))

    # def test_brightness_minimum(self):
    #     model = Model()
    #     self.assertTrue(model.process("minimum brightness"))

    # def test_get_brightness(self):
    #     model = Model()
    #     self.assertEqual(model.process("current brightness"), 0)


if __name__ == "__main__":
    unittest.main()
