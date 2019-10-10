import pyglet
import scene

WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, caption="1024x640", resizable=True)
window.scene_o = scene.MenuScene(WINDOW_WIDTH, WINDOW_HEIGHT)

@window.event
def on_draw():
    window.clear()
    window.scene_o.on_draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    window.scene_o.on_mouse_press()
    if not isinstance(window.scene_o, window.scene_o.goto):
        window.scene_o = window.scene_o.goto(WINDOW_WIDTH,WINDOW_HEIGHT)

@window.event
def on_resize(width, height):
    window.set_caption("{}x{}".format(width, height))

pyglet.app.run()
