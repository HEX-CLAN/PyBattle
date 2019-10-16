import pyglet
import menuscene
import gamescene
import settings


window = pyglet.window.Window(settings.width, settings.height, resizable=True)
# vsync=False to unlock more fps
window.scene_o = menuscene.MenuScene()
if settings.fps:
    window.fps_display = pyglet.window.FPSDisplay(window)
    window.fps_display.label.font_size = 20
    window.fps_display.label.color = settings.white
    window.fps_display.update_period = 0.5

@window.event
def on_draw(frame_time=0):
    window.clear()
    window.scene_o.on_draw()
    if settings.fps:
        window.fps_display.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    window.scene_o.on_mouse_press()
    if not isinstance(window.scene_o, window.scene_o.goto):
        window.scene_o = window.scene_o.goto()

@window.event
def on_resize(width, height):
    window.set_caption("{}x{}".format(width, height))
    print("{}x{}".format(width, height))

@window.event
def on_mouse_motion(x, y, dx, dy):
    window.scene_o.on_mouse_motion(x, y)


pyglet.clock.schedule_interval(on_draw, 0.0166)
# 0.001 to unlock more fpx
pyglet.app.run()
