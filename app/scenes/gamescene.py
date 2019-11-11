from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color, Line, Ellipse
from kivy.core.window import Window
from tile import Tile
import math

class GameScene(Screen):

    def calc_pre(self):
        self.hex_grid_size = (20,10)
        self.pt_grid_size = (self.hex_grid_size[0] * 3 + 1, self.hex_grid_size[1] * 2 + 1)
        self.grid_ratio = (self.pt_grid_size[0] / 2, self.pt_grid_size[1] / 2 * math.sqrt(3))
        self.grid = [[0] * self.hex_grid_size[1] for i in range(self.hex_grid_size[0])]

        self.canvas.add(Color(0.231, 0.451, 0.761, 1))
        for column in range(self.hex_grid_size[0]):
            for row in range(self.hex_grid_size[1]):
                self.grid[column][row] = Tile()
                self.canvas.add(self.grid[column][row])

    def calc_re(self):
        if self.width / self.grid_ratio[0] > self.height / self.grid_ratio[1]:
            self.unit_h = self.height // self.pt_grid_size[1]
            self.unit_w = int(self.unit_h // math.sqrt(3))
        else:
            self.unit_w = self.width // self.pt_grid_size[0]
            self.unit_h = int(self.unit_w * math.sqrt(3))+ 1

        for column in range(self.hex_grid_size[0]):
            x = 3 * self.unit_w * column
            for row in range(self.hex_grid_size[1]):
                y = self.unit_h * 2 * row + self.unit_h * ((column+1) % 2) + self.unit_h - self.unit_w * 2
                self.grid[column][row].pos = (x, y)
                self.grid[column][row].size = (self.unit_w * 4 - 2, self.unit_w * 4 - 2)
                
        self.rec.size=(self.pt_grid_size[0] * self.unit_w, self.pt_grid_size[1] * self.unit_h)

    def on_enter(self):
        print("Start Game")

        self.canvas.add(Color(1, 1, 1, 1))
        self.rec = Rectangle(pos=(0,0), size=(0, 0))
        self.canvas.add(self.rec)

        self.calc_pre()
        self.calc_re()

        Window.bind(on_resize=self.on_window_resize)


    def on_window_resize(self, window, width, height):
        print("resize")
        self.calc_re()

