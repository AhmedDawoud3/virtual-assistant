import screen_brightness_control as sbc


class Brightness:
    def __init__(self):
        self.old = sbc.get_brightness()[0]

    def get_current_value(self):
        return self.old

    def increase(self):
        sbc.set_brightness(self.old + 25)
        return "Increasing brightness..."

    def decrease(self):
        sbc.set_brightness(self.old - 25)
        return "Decreasing brightness..."

    def maximum(self):
        sbc.set_brightness(100)
        return "Maximizing brightness..."

    def minimum(self):
        sbc.set_brightness(0)
        return "Minimizing brightness..."
