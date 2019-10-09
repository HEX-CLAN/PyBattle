from shape import Shape
from shapes import Shapes


class Hexagon(Shape):

    def __init__(self, center_x, center_y,size):
        super.__init__(center_x, center_y)
        shape = Shapes.HEXAGON
