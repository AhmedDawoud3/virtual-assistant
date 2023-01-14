from modules.calculate.helper import *
from math import sqrt


class Calculate:
    def can_calculate(self, text):
        text = replace_text_by_num(text)
        if not is_math_expression(text):
            return False

        text = replace_text_by_num(text)
        text = replace_expressions(text)

        try:
            result = eval(text)
            if float(result).is_integer():
                self.result = "The answer is {}".format(int(result))
                return True
            else:
                self.result = "The answer is {:.3f}".format(result)
                return True

        except ZeroDivisionError:
            self.result = "): Can't divide by zero"
            return True
        except SyntaxError:
            return False
        except NameError:
            return False
        except Exception as e:
            print(e)
            return False

    def get_result(self):
        return self.result
