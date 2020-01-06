import numpy
from kivy.uix.screenmanager import Screen
from utils.map import Map


class GameScene(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.map = Map()
        self.canvas.add(self.map.canvas)

    def on_enter(self):
        self.map.update_canvas(x=0, y=0, w = self.width, h = self.height)

    def on_touch_down(self, touch):
        self.map.click(position = (touch.x, touch.y))

