import kivy
kivy.config.Config.setdefault('graphics', 'resizable', True)
kivy.config.Config.setdefault('graphics', 'fullscreen', False)
kivy.config.Config.setdefault('graphics', 'borderless', False)
kivy.config.Config.set('graphics', 'resizable', True)
kivy.config.Config.set('graphics', 'fullscreen', False)
kivy.config.Config.set('graphics', 'borderless', False)
kivy.config.Config.write()

from pybattle.run import Run
from kivy.core.window import Window


if __name__ == '__main__':
    Window.fullscreen = False
    r = Run()
    r.run()


