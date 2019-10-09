import pyglet
import utils

WHITE = [255]*4

class GameScene:
    def __init__(self, hex_radius):
        self.goto = GameScene
        self.image = pyglet.resource.image('game.png')
        self.hex_radius = hex_radius

    def on_mouse_press(self):
        self.goto = MenuScene

    def change_hex_radius(self, scroll_y):
        self.hex_radius -= scroll_y

    def on_draw(self):
        self.image.blit(100, 100)
        self.batch = pyglet.graphics.Batch()
        self.batch.add(6, pyglet.gl.GL_POLYGON, None, ('v2i',utils.calc_hex(512, 320, self.hex_radius)), ('c4B',WHITE*6))
        self.batch.draw()


class MenuScene:
    def __init__(self, hex_radius):
        self.goto = MenuScene
        self.label = pyglet.text.Label('PyBattle Menu', font_name='Times New Roman',
                          font_size=36, x=200, y=200,
                          anchor_x='center', anchor_y='center')
        self.hex_radius = hex_radius

    def on_mouse_press(self):
        self.goto = GameScene

    def change_hex_radius(self, scroll_y):
        self.hex_radius -= scroll_y

    def on_draw(self):
        self.label.draw()
