import screen_brightness_control as sbc


class Brightness:
    """This class controls the brightness of the screen"""
    def __init__(self):
        """This function gets the current brightness and stores it for future use"""
        self.old = sbc.get_brightness()[0]

    def get_current_value(self):
        """This function returns the current brightness"""
        return self.old

    def increase(self):
        """This function increases the brightness by 25%"""
        sbc.set_brightness(self.old + 25)
        return "Increasing brightness..."

    def decrease(self):
        """This function decreases the brightness by 25%"""
        sbc.set_brightness(self.old - 25)
        return "Decreasing brightness..."

    def maximum(self):
        """This function sets the brightness to 100%"""
        sbc.set_brightness(100)
        return "Maximizing brightness..."

    def minimum(self):
        """This function sets the brightness to 0%"""
        sbc.set_brightness(0)
        return "Minimizing brightness..."