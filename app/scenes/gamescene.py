from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color, Line, Ellipse
from kivy.core.window import Window
from tile import Tile
import math
import generator


class GameScene(Screen):

    def create_grid(self):
        self.hex_grid_size = (30,20)
        self.pt_grid_size = (self.hex_grid_size[0] * 3 + 1, self.hex_grid_size[1] * 2 + 1)
        self.grid_ratio = (self.pt_grid_size[0] / 2, self.pt_grid_size[1] / 2 * math.sqrt(3))

        self.grid = generator.generate_map(
                        width = self.hex_grid_size[0],
                        height = self.hex_grid_size[1],
                        seed = 42352336,
                        water = 10,
                        max_diff = 1
                    )

        for x in range(self.hex_grid_size[0]):
            for y in range(self.hex_grid_size[1]):
                self.canvas.add(self.grid[x][y].color)
                self.canvas.add(self.grid[x][y])

    def recalculate(self):
        if self.width / self.grid_ratio[0] > self.height / self.grid_ratio[1]:
            self.unit_h = self.height // self.pt_grid_size[1]
            self.unit_w = int(self.unit_h // math.sqrt(3))
        else:
            self.unit_w = self.width // self.pt_grid_size[0]
            self.unit_h = int(self.unit_w * math.sqrt(3))+ 1

        self.padding = ((self.width - self.pt_grid_size[0] * self.unit_w) / 2,
                        (self.height - self.pt_grid_size[1] * self.unit_h) / 2)

        for column in range(self.hex_grid_size[0]):
            x = 3 * self.unit_w * column + self.padding[0]
            for row in range(self.hex_grid_size[1]):
                y = self.unit_h * 2 * row + self.unit_h * ((column+1) % 2) + self.unit_h - self.unit_w * 2 + self.padding[1]
                self.grid[column][row].pos = (x, y)
                self.grid[column][row].size = (self.unit_w * 4 - 2, self.unit_w * 4 - 2)

    def on_enter(self):
        self.create_grid()
        self.recalculate()
        Window.bind(on_resize=self.on_window_resize)

    def on_window_resize(self, window, width, height):
        self.recalculate()
        print("new size:", self.width, self.height)
