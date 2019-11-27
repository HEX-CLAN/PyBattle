from kivy.app import App
from kivy.config import Config
import scenes.gamescene
import scenes.menuscene
import scenes.settingsscene

from scenes.settingsscene import json_settings

Config.set('modules', 'monitor', '') #FPS meter


class Window(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_kivy_settings = False

    def build_config(self, config):
        config.setdefaults("General", {'width': 768, 'height': 1024})

    def build_settings(self, settings):
        settings.add_json_panel("Settings", self.config, data=json_settings)

    def on_config_change(self, config, section, key, value):
        if key == "width":
            Config.set('graphics', 'width', value)
        elif key == "height":
            Config.set('graphics', 'height', value)


if __name__ == '__main__':
    w = Window()
    w.run()
