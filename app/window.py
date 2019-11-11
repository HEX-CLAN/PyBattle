from kivy.app import App
from kivy.config import Config
from scenes.gamescene import GameScene
import scenes.menuscene
import scenes.settingsscene


Config.set('modules', 'monitor', '') #FPS meter


class Window(App):
    def build(self):
        Window.size = (1740, 1360)
        pass


if __name__ == '__main__':
    w = Window()
    w.run()
