from kivy.graphics import Color, Ellipse

class Tile(Ellipse):
    def __init__(self):
        super().__init__(angle_start=30, angle_end=390, segments=6, pos=(0, 0), size=(10, 10))
        pass
