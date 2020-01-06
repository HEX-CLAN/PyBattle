from utils import generator
from utils import settings
import numpy
from kivy.graphics.instructions import Canvas
from utils.tile import util_get_closest_tile


class Map:
    def __init__(self, width, height, seed, water, max_diff):
        self.width = width # grid dimensions 
        self.height = height
        self.seed = seed
        self.water = water
        self.max_diff = max_diff

        self.canvas = Canvas()

        self.tile = generator.generate_map(
            width=self.width,
            height=self.height,
            seed=self.seed,
            water=self.water,
            max_diff=self.max_diff
        )

        for x in range(self.width):
            for y in range(self.height):
                self.canvas.add(self.tile[x][y])

        # real pixel dimensions
        self.real_x = 0
        self.real_y = 0
        self.real_w = 0
        self.real_h = 0

    def update_canvas(self, x, y, w, h):
        # gets maximal rectangle dimensions in pixels to contain canvas

        help_points_size = (self.width * 3 + 1, self.height * 2 + 1)

        if w / self.width > h / (self.height * numpy.sqrt(3)):
            # more padding on left and right
            uy = h // help_points_size[1]
            ux = int(uy // numpy.sqrt(3))
        else:
            # more padding on top and bottom
            ux = w // help_points_size[0]
            uy = int(ux * numpy.sqrt(3)) + 1

        self.real_x = (w - help_points_size[0] * ux) / 2
        self.real_y = (h - help_points_size[1] * uy) / 2
        self.real_w = help_points_size[0] * ux
        self.real_h = help_points_size[1] * uy

        for column in range(self.width):
            x = 3 * ux * column + self.real_x
            for row in range(self.height):
                y = uy * 2 * row + uy * ((column + 1) % 2) + uy - ux * 2 + self.real_y
                self.tile[column][row].set_pos_and_size(pos=(x, y), size=(ux * 4 - 2, ux * 4 - 2))

    def click(self, position):
        tiles = []
        for x in range(self.width):
            for y in range(self.height):
                if self.tile[x][y].contains(position):
                    tiles.append(self.tile[x][y])

        tile = util_get_closest_tile(tiles, position)
        if tile is not None:
            side = tile.get_side(position)
            print(f"{tile.grid_pos} {side}")
            tile.activate_line(side)
        else:
            print("Poza")
