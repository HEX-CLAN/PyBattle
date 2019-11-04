from kivy.app import App
from kivy.config import Config
import scenes.gamescene
import scenes.menuscene
import scenes.settingsscene


Config.set('modules', 'monitor', '') #FPS meter


class Window(App):
    def build(self):
        pass


if __name__ == '__main__':
    w = Window()
    w.run()
