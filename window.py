import pyglet
import scene


window = pyglet.window.Window()
window.scene_o = scene.MenuScene()

@window.event
def on_draw():
    window.clear()
    window.scene_o.on_draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    window.scene_o.on_mouse_press()
    if not isinstance(window.scene_o, window.scene_o.goto):
        window.scene_o = window.scene_o.goto()

pyglet.app.run()
