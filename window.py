import pyglet
import scene

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 720

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, caption="1024x640", resizable=True)
# vsync=False to unlock more fps
window.scene_o = scene.MenuScene(WINDOW_WIDTH, WINDOW_HEIGHT)
window.fps_display = pyglet.window.FPSDisplay(window)
window.fps_display.label.font_size = 20
window.fps_display.label.color = (255,255,255,255)
window.fps_display.update_period = 0.5

@window.event
def on_draw(mhm=0):
    window.clear()
    window.scene_o.on_draw()
    window.fps_display.draw()
    print(mhm)

@window.event
def on_mouse_press(x, y, button, modifiers):
    window.scene_o.on_mouse_press()
    if not isinstance(window.scene_o, window.scene_o.goto):
        window.scene_o = window.scene_o.goto(WINDOW_WIDTH,WINDOW_HEIGHT)

@window.event
def on_resize(width, height):
    window.set_caption("{}x{}".format(width, height))

pyglet.clock.schedule_interval(on_draw, 0.016)
# 0.001 to unlock more fpx
pyglet.app.run()
