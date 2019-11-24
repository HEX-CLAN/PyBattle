from kivy.graphics import Color, Ellipse

colors = [
    (181 / 255, 209 / 255, 100 / 255, 1),
    ( 70 / 255, 132 / 255, 200 / 255, 1),
    ( 60 / 255, 116 / 255, 197 / 255, 1),
    ( 50 / 255,  99 / 255, 193 / 255, 1),
    ( 40 / 255,  82 / 255, 189 / 255, 1),
    ( 30 / 255,  65 / 255, 185 / 255, 1)
]


class Tile(Ellipse):
    def __init__(self):
        super().__init__(angle_start=30, angle_end=390, segments=6, pos=(0, 0), size=(0, 0))
        self.depth = 0
        self.color = Color(rgba=(181 / 255, 209 / 255, 100 / 255, 1))

        pass

    def set_depth(self, depth):
        if depth < 0 or depth > 5:
            print("ERROR: WRONG DEPTH !!!")
        else:
            self.depth = depth
            self.color.rgba = colors[depth]

