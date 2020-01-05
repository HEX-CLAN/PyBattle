import numpy

from kivy.uix.screenmanager import Screen
from utils.tile import util_get_closest_tile
from utils import generator
from utils import settings


class GameScene(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.hex_grid_size = (int(settings.game_data['map_width']), int(settings.game_data['map_height']))
        self.pt_grid_size = (self.hex_grid_size[0] * 3 + 1, self.hex_grid_size[1] * 2 + 1)
        self.grid_ratio = (self.pt_grid_size[0] / 2, self.pt_grid_size[1] / 2 * numpy.sqrt(3))
        self.grid = generator.generate_map(
            width=self.hex_grid_size[0],
            height=self.hex_grid_size[1],
            seed=42352336,
            water=settings.game_data['water_level'],
            max_diff=1
        )

    def on_enter(self):
        self.create_grid()
        self.recalculate()

    def create_grid(self):
        for x in range(self.hex_grid_size[0]):
            for y in range(self.hex_grid_size[1]):
                self.canvas.add(self.grid[x][y].color)
                self.canvas.add(self.grid[x][y])
                for l in range(6):
                    self.canvas.add(self.grid[x][y].nearby_tiles[l]['line_color'])
                    self.canvas.add(self.grid[x][y].nearby_tiles[l]['line'])

    def recalculate(self):
        if self.window_is_with_vertical_padding():
            self.unit_h = self.height // self.pt_grid_size[1]
            self.unit_w = int(self.unit_h // numpy.sqrt(3))
        else:
            self.unit_w = self.width // self.pt_grid_size[0]
            self.unit_h = int(self.unit_w * numpy.sqrt(3)) + 1

        self.padding = ((self.width - self.pt_grid_size[0] * self.unit_w) / 2,
                        (self.height - self.pt_grid_size[1] * self.unit_h) / 2)

        for column in range(self.hex_grid_size[0]):
            x = 3 * self.unit_w * column + self.padding[0]
            for row in range(self.hex_grid_size[1]):
                y = self.unit_h * 2 * row + self.unit_h * ((column + 1) % 2) + self.unit_h - self.unit_w * 2 + \
                    self.padding[1]
                self.grid[column][row].set_pos_and_size(pos=(x, y), size=(self.unit_w * 4 - 2, self.unit_w * 4 - 2))

    def window_is_with_vertical_padding(self):
        return self.width / self.grid_ratio[0] > self.height / self.grid_ratio[1]

    def on_touch_down(self, touch):
        position = (touch.x, touch.y)
        tiles = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y].contains(position):
                    tiles.append(self.grid[x][y])

        tile = util_get_closest_tile(tiles, position)
        if tile is not None:
            side = tile.get_side(position)
            print(f"{tile.pos_on_grid} {side}")
            tile.activate_line(side)
        else:
            print("Poza")
