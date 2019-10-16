import pyglet
from pyglet.gl import *
import settings
import gamescene
from button import Button


class MenuScene:
    def __init__(self):
        self.goto = MenuScene
        pyglet.gl.glClearColor(0.1, 0.1, 0.1, 1)
        pyglet.font.add_file("hexagon_cup.ttf")
        pyglet.font.load('HEXAGON cup font')
        pyglet.font.add_file("CaviarDreams.ttf")
        pyglet.font.load('Caviar Dreams')
        self.header = pyglet.text.Label(
            'PyBattle',
            font_name='HEXAGON cup font',
            font_size=70,
            x=settings.width/2,
            y=settings.height-130,
            anchor_x='center',
            color=(35, 255, 204, 255))

        center_x = settings.width//2
        center_y = settings.height//2
        self.start_button = Button('START', center_x, center_y + 50, 200, 40)
        self.settings_button = Button('SETTINGS', center_x, center_y, 200, 40)
        self.exit_button = Button('EXIT', center_x, center_y - 50, 200, 40)

    def on_mouse_press(self):
        self.goto = gamescene.GameScene

    def on_draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', (383, 181,
                                      383, 381,
                                      717, 381,
                                      717, 181)),
                             ('c4B', settings.cyan_frame))
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', (378, 176,
                                      378, 386,
                                      722, 386,
                                      722, 176)),
                             ('c4B', settings.cyan_frame))
        self.header.draw()
        self.start_button.draw()
        self.settings_button.draw()
        self.exit_button.draw()

    def on_mouse_motion(self, x, y):
        self.start_button.on_hover(x, y)
        self.settings_button.on_hover(x, y)
        self.exit_button.on_hover(x, y)
