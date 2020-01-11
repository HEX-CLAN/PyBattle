from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
import pybattle.scenes.game
import pybattle.scenes.menu
import pybattle.scenes.settings_app
import pybattle.scenes.settings_game

Config.set('modules', 'monitor', '')  # FPS meter


class Run(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'PYBATTLE'

    def build(self):
        pass

    def on_start(self):
        pass
