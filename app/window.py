import scenes.gamescene
import scenes.menuscene
import scenes.appsettingsscene
import scenes.gamesettingsscene

from kivy.app import App
from kivy.config import Config

Config.set('modules', 'monitor', '') #FPS meter


class Window(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_kivy_settings = False

    def build(self):
        # TODO: sprawdzić co z tym resizable jest nie tak (z jakiegoś powodu nie mogę tego zablokować)
        Config.set('graphics', 'resizable', 0)


if __name__ == '__main__':
    w = Window()
    w.run()
