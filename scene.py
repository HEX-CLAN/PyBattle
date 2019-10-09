import pyglet

WHITE = [255]*4

class GameScene:
    def __init__(self):
        self.goto = GameScene
        self.image = pyglet.resource.image('game.png')
        self.batch = pyglet.graphics.Batch()
        self.batch.add(4, pyglet.gl.GL_POLYGON, None, ('v2i',[10,60,10,110,390,60,390,110]), ('c4B',WHITE*4))

    def on_mouse_press(self):
        self.goto = MenuScene

    def on_draw(self):
        self.image.blit(100, 100)
        self.batch.draw()


class MenuScene:
    def __init__(self):
        self.goto = MenuScene
        self.label = pyglet.text.Label('PyBattle Menu', font_name='Times New Roman',
                          font_size=36, x=200, y=200,
                          anchor_x='center', anchor_y='center')

    def on_mouse_press(self):
        self.goto = GameScene

    def on_draw(self):
        self.label.draw()
