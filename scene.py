import pyglet


class GameScene:
    def __init__(self):
        self.goto = GameScene
        self.image = pyglet.resource.image('hello.png')

    def on_mouse_press(self):
        self.goto = MenuScene

    def on_draw(self):
        self.image.blit(0, 0)


class MenuScene:
    def __init__(self):
        self.goto = MenuScene
        self.label = pyglet.text.Label('Hello, world', font_name='Times New Roman',
                          font_size=36, x=200, y=200,
                          anchor_x='center', anchor_y='center')

    def on_mouse_press(self):
        self.goto = GameScene

    def on_draw(self):
        self.label.draw()
