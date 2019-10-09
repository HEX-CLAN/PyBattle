from shape import Shape
from shapes import Shapes


class Square(Shape):

    def __init__(self, center_x, center_y):
        super.__init__(center_x, center_y)
        shape = Shapes.SQUARE
