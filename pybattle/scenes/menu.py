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

        self.full = True

        pass

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if self.full:
            Window.fullscreen = False
            self.full = False
        else:
            Window.fullscreen = 'auto' # jesli bedzie true to wskoczy w dziwna rozdzielczosc
            self.full = True

        pass


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


