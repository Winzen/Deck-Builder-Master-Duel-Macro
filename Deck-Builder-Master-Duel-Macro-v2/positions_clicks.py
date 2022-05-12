from pyautogui import size, rightClick, click, moveTo, pixel


class ClickPositions:
    def __init__(self, x_pixel, y_pixel, raw_value_y=False):
        self.resolution = size()

        self.compensation = self.resolution.width - self.resolution.height

        self.percentage_y = y_pixel / 900

        if raw_value_y is True:
            self.height = y_pixel

        else:

            self.height = self.resolution.height * (
                self.percentage_y if self.compensation > 350 else self.percentage_y + 0.07)

            self.height = self.resolution.height * self.percentage_y - 0.03 if self.compensation > 550 else self.height

        self.width = int(self.resolution.width) * (x_pixel / 1440)

        self.sizes = [self.width, self.height]

    def right_click(self):
        rightClick(self.width, self.height)

    def left_click(self):
        click(self.width, self.height)

    def move(self):
        moveTo(self.width, self.height)

    def pixel(self):
        return pixel(int(self.width), int(self.height))
