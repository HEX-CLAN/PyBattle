import pyglet
from pyglet.text import Label 

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world', font_name='Times New Roman',
                          font_size=36, x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
image = pyglet.resource.image('hello.png')



@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0, 0)

pyglet.app.run()