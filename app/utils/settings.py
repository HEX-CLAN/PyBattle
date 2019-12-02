from kivy import Config
import numpy as np
from kivy.core.window import Window

MIN_WINDOW_WIDTH = 1024
MAX_WINDOW_WIDTH = 1920
MIN_WINDOW_HEIGHT = 768
MAX_WINDOW_HEIGHT = 1080
fps = True
duration = True


class Settings:
    user_data = {
        'width': MIN_WINDOW_HEIGHT,
        'height': MIN_WINDOW_HEIGHT
    }

    def set_default_settings(self):
        Config.set('graphics', 'width', MIN_WINDOW_WIDTH)
        Config.set('graphics', 'height', MIN_WINDOW_HEIGHT)

    def create_user_file(self):
        f = open('data/userdata.npy', 'w+')
        f.close()
        np.save('data/userdata.npy', self.user_data)

    def read_user_data(self):
        self.user_data = np.load('data/userdata.npy', allow_pickle=True).item()

    def update_and_save(self, new_user_data):
        self.user_data = new_user_data
        self.update()
        self.save()
        print(self.user_data)

    def update(self):
        Window.size = (self.user_data['width'], self.user_data['height'])

    def save(self):
        np.save('data/userdata.npy', self.user_data)
