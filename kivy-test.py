from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.graphics import Rectangle, Color, Line, Ellipse
from kivy.core.window import Window
import math

Config.set('modules', 'monitor', '')



class Example(AnchorLayout):
    def __init__(self):
        super().__init__(anchor_x='center', anchor_y='center')
        self.canvas.add(Color(0.3, 0.4, 0.7, 1))

        # init
        hex_grid_size = (20,10)

        # calculate grid
        pt_grid_size = (hex_grid_size[0] * 3 + 1, hex_grid_size[1] * 2 + 1)
        grid_ratio = (pt_grid_size[0] / 2, pt_grid_size[1] / 2 * math.sqrt(3))

        if self.width / grid_ratio[0] > self.height / grid_ratio[1]:
            #padding on left and right
            print("lr")
            pass
        else:
            #padding on top and bottom
            print("tb")
            pass

        self.counter = 0

        print(self.width, self.height)

        for y in range(15):
            for x in range(12):
                el_1 = Ellipse(angle_start=30,
                               angle_end=390,
                               segments=6,
                               pos=(0 + x * 122, 0 + y * 71), 
                               size=(79, 79))
                el_2 = Ellipse(angle_start=30, 
                               angle_end=390, 
                               segments=6, 
                               pos=(0 + x * 122 + 61, 0 + y * 71 + 35), 
                               size=(79, 79))
                self.canvas.add(el_1)
                self.canvas.add(el_2)
        self.canvas.add(Color(0.4, 0.5, 0.8, 1))
        self.el_c = Ellipse(angle_start=30, 
                angle_end=390, 
                segments=6, 
                pos=(self.center_x, self.center_y), 
                size=(79, 79))
        self.canvas.add(self.el_c)

    def on_window_resize(self, window, width, height):
        print("width", width, "height", height, "center_x", self.center_x)
        self.el_c.pos = (self.center_x, self.center_y)
        print(self.width)


    def on_mouse_down(self, x, y, button, modifiers):
        print("xd")

    def on_draw(self, window):
        self.el_c.pos = (self.center_x, self.center_y)
        print(self.width)

def on_touch_down(self, touch):
    print("click at: ", touch.pos)

def on_show(self):
    print("show")


class MainApp(App):
    def build(self):
        widget = Example()
        Window.bind(on_resize=widget.on_window_resize)
        #Window.bind(on_mouse_down=widget.on_mouse_down)
        Window.bind(on_touch_down=on_touch_down)
        Window.bind(on_show=on_show)
        Window.bind(on_draw=widget.on_draw)
        return widget


if __name__ == '__main__':
    MainApp().run()