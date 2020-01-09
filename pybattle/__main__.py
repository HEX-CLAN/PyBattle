import kivy
kivy.config.Config.setdefault('graphics', 'resizable', True)
kivy.config.Config.setdefault('graphics', 'fullscreen', 'auto')
kivy.config.Config.setdefault('graphics', 'borderless', False)
kivy.config.Config.set('graphics', 'resizable', True)
kivy.config.Config.set('graphics', 'fullscreen', 'auto')
kivy.config.Config.set('graphics', 'borderless', False)
kivy.config.Config.write()
from pybattle.run import Run


if __name__ == '__main__':
    r = Run()
    r.run()
