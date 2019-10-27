import pyglet
import settings
import menuscene
from button import Button


class MenuScene:
    def __init__(self):
        self.goto = MenuScene
        pyglet.gl.glClearColor(0.1, 0.1, 0.1, 1)
        pyglet.font.add_file("hexagon_cup.ttf")
        pyglet.font.load('HEXAGON cup font')
        pyglet.font.add_file("CaviarDreams.ttf")
        pyglet.font.load('Caviar Dreams')
        pyglet.font.add_file('hexgon.ttf')
        pyglet.font.load('HEX:gon')
        self.header = pyglet.text.Label(
            'PyBattle',
            font_name='HEXAGON cup font',
            font_size=65,
            x=settings.width/2,
            y=settings.height-130,
            anchor_x='center',
            color=settings.cyan)

        center_x = settings.width//2
        center_y = settings.height//2
        self.buttons = []
        self.buttons.append(Button('START', center_x, center_y-28, 200, 40))
        self.buttons.append(Button('SETTINGS', center_x, center_y-78, 200, 40))
        self.buttons.append(Button('EXIT', center_x, center_y-128, 200, 40))

        self.hexagons_upper = pyglet.text.Label(
            '_                    _',
            font_name='HEX:gon',
            font_size=65,
            x=settings.width / 2,
            y=settings.height - 140,
            anchor_x='center',
            color=settings.cyan
        )

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
        self.hexagons_upper.draw()
        self.header.draw()
        for b in self.buttons:
            b.draw()

    def on_resize(self, width, height):
        pass
    
    def on_mouse_motion(self, x, y):
        for b in self.buttons:
            b.on_mouse_motion(x, y)

    def on_mouse_press(self):
        for b in self.buttons:
            b.on_mouse_press()

    def on_mouse_release(self):
        for b in self.buttons:
            if b.on_mouse_release():
                if b.label.text == 'START':
                    self.goto = gamescene.GameScene
                elif b.label.text == 'SETTINGS':
                    #TODO: zrobić przeniesienie po zrobieniu sceny
                    pass
                elif b.label.text == 'EXIT':
                    pyglet.app.exit()