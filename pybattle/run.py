from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
import pybattle.scenes.game
import pybattle.scenes.menu
import pybattle.scenes.settings_app
import pybattle.scenes.settings_game

Config.set('modules', 'monitor', '')  # FPS meter
#Config.set('graphics', 'fullscreen', 1)

class Run(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.use_kivy_settings = False
        self.title = 'PYBATTLE'

    def build(self):
        #Config.set('graphics', 'resizable', 1)

        #Config.write()
        pass

    def on_start(self):
        print("=== run.py on_start")
        print("window:", Window.size)
        print("config: (" + Config.get('graphics', 'width') + ", " + Config.get('graphics', 'height') + ")")



# if __name__ == '__main__':
#     w = Window()
#     w.run()





# pecet pokazuje 5120x2880 a ustawienie jest 1440x900-HIDPI
# lapek pokazuje 2880x1800 a ustawienie jest 1440x900-HIDPI