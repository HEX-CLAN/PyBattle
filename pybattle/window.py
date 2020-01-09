from kivy.app import App
from kivy.config import Config
import pybattle.scenes.game
import pybattle.scenes.menu
import pybattle.scenes.settings_app
import pybattle.scenes.settings_game

Config.set('modules', 'monitor', '')  # FPS meter


class Window(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_kivy_settings = False
        self.title = 'PYBATTLE'

    def build(self):
        Config.set('graphics', 'resizable', '0')
        Config.write()


# if __name__ == '__main__':
#     w = Window()
#     w.run()
