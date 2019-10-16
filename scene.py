import pyglet
import utils
from grid_hexagon import Grid
import settings
import time


class GameScene:
    def __init__(self):
        self.goto = GameScene
        self.grid = Grid(settings.width, settings.height, 30, 20)
        if settings.duration:
            self.game_time = time.time()
        pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)

    def on_mouse_press(self):
        self.goto = MenuScene

    def on_draw(self):
        if settings.duration:
            time_label = "{:2.2f}".format(time.time() - self.game_time)
            time_label = pyglet.text.Label(time_label, font_size=20, x=1000, y=10, color=settings.white)
            time_label.draw()
            self.grid.on_draw()

class MenuScene:
    def __init__(self):
        self.goto = MenuScene
        self.label = pyglet.text.Label('PyBattle', font_name='Times New Roman',
                          font_size=36, x=200, y=200,
                          anchor_x='center', anchor_y='center', color=(1,0,0,255))
        pyglet.gl.glClearColor(176/255, 220/255, 112/255, 1)

    def on_mouse_press(self):
        self.goto = GameScene

    def on_draw(self):
        self.label.draw()
