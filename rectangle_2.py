from rectangle import Rectangle, Square, Circle, LocatedRectangle


rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# print(rect_1.get_area())
# print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

# print(square_1.get_area_square(), square_2.get_area_square())
circ_1 = Circle(4)
circ_2 = Circle(7)

l_rect_1 = LocatedRectangle(5, 10, 50, 100)
l_rect_2 = LocatedRectangle(10, 15, 55, 105)

figures = [rect_1, rect_2, square_1, square_2, circ_1, circ_2, l_rect_1, l_rect_2]
for figure in figures:
    print(figure.get_area())


print(str(l_rect_1))
print(str(l_rect_2))
