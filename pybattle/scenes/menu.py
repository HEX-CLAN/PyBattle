from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy import Config


class Menu(Screen):
    def on_enter(self):
        print("=== menu.py on_enter")
        print("window:", Window.size)
        print("config: (" + Config.get('graphics', 'width') + ", " + Config.get('graphics', 'height') + ")")

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.mode = 0

        pass

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if self.mode == 1:
            Window.fullscreen = True
            Window.size = (800, 450)
            self.mode = 2
            return

        if self.mode == 2:
            Window.fullscreen = 'auto'
            self.mode = 0
            return

        if self.mode == 0:
            Window.fullscreen = False
            self.mode = 1
            return




    # def on_touch_down(self, touch):
    #     #Config.set('graphics', 'fullscreen', 'auto')
    #     #Window.fullscreen = 'auto'
    #
    #     print("=== menu.py on_touch")
    #     print("window:", Window.size)
    #     print("config: (" + Config.get('graphics', 'width') + ", " + Config.get('graphics', 'height') + ")")
    #     print("click: " + str(touch.pos))
    #
    #     pass


