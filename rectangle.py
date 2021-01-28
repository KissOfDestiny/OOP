from math import pi


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_radius(self):
        return self.r

    def set_radius(self, r):
        self.r = r

    def get_area(self):
        return pi * self.r ** 2


class LocatedRectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_y(self, x):
        self.x = x

    def set_x(self, x):
        self.x = x

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def __str__(self):
        return str(f"Rectangle ({self.get_x()}, {self.get_y()}, {self.get_width()}, {self.get_height()})")
