import os
import scenes.gamescene
import scenes.menuscene
import scenes.settingsscene

from kivy.app import App
from kivy.config import Config

from utils.settings import Settings

Config.set('modules', 'monitor', '') #FPS meter


class Window(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_kivy_settings = False
        self.settings = Settings()

    def build(self):
        if os.path.isfile('data/userdata.npy'):
            self.settings.read_user_data()
            self.settings.update()
        else:
            self.settings.create_user_file()
            self.settings.set_default_settings()


if __name__ == '__main__':
    w = Window()
    w.run()
