from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color, Line, Ellipse
from kivy.core.window import Window
from tile import Tile
import math


class GameScene(Screen):

    def calc_pre(self):
        self.hex_grid_size = (30,20)
        self.pt_grid_size = (self.hex_grid_size[0] * 3 + 1, self.hex_grid_size[1] * 2 + 1)
        self.grid_ratio = (self.pt_grid_size[0] / 2, self.pt_grid_size[1] / 2 * math.sqrt(3))
        self.grid = [[0] * self.hex_grid_size[1] for i in range(self.hex_grid_size[0])]

        self.col = [

            Color(181 / 255, 209 / 255, 100 / 255, 1),
            Color( 70 / 255, 132 / 255, 200 / 255, 1),
            Color( 60 / 255, 116 / 255, 197 / 255, 1),
            Color( 50 / 255,  99 / 255, 193 / 255, 1),
            Color( 40 / 255,  82 / 255, 189 / 255, 1),
            Color( 30 / 255,  65 / 255, 185 / 255, 1) 
        ]

        f = open('test.map', 'r')
        row_i = 0
        char_i = 0
        for row in f.readlines():
            char_i = 0
            for char in row:
                if char in ('0', '1', '2', '3', '4', '5'):
                    self.canvas.add(self.col[int(char)])
                    self.grid[char_i][row_i] = Tile()
                    self.canvas.add(self.grid[char_i][row_i])
                    char_i += 1
            row_i += 1
        f.close()

    def calc_re(self):
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
        self.calc_pre()
        self.calc_re()
        Window.bind(on_resize=self.on_window_resize)

    def on_window_resize(self, window, width, height):
        self.calc_re()
        print("new size:", self.width, self.height)
