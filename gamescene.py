import pyglet
import time

from grid_hexagon import Grid
import settings
import menuscene

class GameScene:
    def __init__(self):
        self.goto = GameScene
        self.grid = Grid(settings.width, settings.height, 30, 20)
        if settings.duration:
            self.game_time = time.time()
        pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)

    def on_mouse_press(self):
        self.goto = menuscene.MenuScene

    def on_draw(self):
        if settings.duration:
            time_label = "{:2.2f}".format(time.time() - self.game_time)
            time_label = pyglet.text.Label(time_label, font_size=20, x=1000, y=10, color=settings.white)
            time_label.draw()
            self.grid.on_draw()

    def on_mouse_motion(self, x, y):
        pass

    def on_mouse_release(self):
        pass
