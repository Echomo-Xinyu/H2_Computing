import math


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width + self.height) * 2


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def getArea(self):
        return super().getArea()

    def getPerimeter(self):
        return super().getPerimeter()


class Rhombus(Rectangle):
    def __init__(self, diagonal1, diagonal2):
        super().__init__(diagonal1, diagonal2)

    def getArea(self):
        return super().getArea() / 2

    def getPerimeter(self):
        return math.sqrt(self.width**2 + self.height**2)


class Trapezium(Rectangle):
    def __init__(self, a, b, c, d, h):
        super().__init__(a, b)
        self.c, self.d, self.h = c, d, h

    def getArea(self):
        return 0.5 * (self.width + self.height) * self.h

    def getPerimeter(self):
        return self.width + self.height + self.c + self.d


class Parallelogram(Rectangle):
    def __init__(self, width, side, height):
        super().__init__(width, height)
        self.side = side

    def getArea(self):
        return super().getArea()

    def getPerimeter(self):
        return 2 * (self.width + self.height)


class Kite(Rectangle):
    def __init__(self, width, height, line1, line2, line3, line4):
        super().__init__(width, height)
        self.line1, self.line2, self.line3, self.line4 = line1, line2, line3, line4

    def getArea(self):
        return super().getArea() / 2

    def getPerimeter(self):
        return self.line1 + self.line2 + self.line3 + self.line4