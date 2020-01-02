import os

import numpy as np
from kivy import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from utils import settings


class AppSettingsScene(Screen):
    MIN_WINDOW_WIDTH = 1024
    MAX_WINDOW_WIDTH = 1920
    MIN_WINDOW_HEIGHT = 768
    MAX_WINDOW_HEIGHT = 1080
    DEFAULT_THEME = 'light'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app_data = {
            'width': self.MIN_WINDOW_WIDTH,
            'height': self.MIN_WINDOW_HEIGHT,
            'theme': self.DEFAULT_THEME
        }
        if os.path.isfile('data/app.npy'):
            self.read_app_settings_data()
            self.update()
        else:
            self.create_user_file()
            self.set_default_settings()

    def set_default_settings(self):
        Config.set('graphics', 'width', self.MIN_WINDOW_WIDTH)
        Config.set('graphics', 'height', self.MIN_WINDOW_HEIGHT)

    def create_user_file(self):
        f = open('data/app.npy', 'w+')
        f.close()
        np.save('data/app.npy', self.app_data)

    def read_app_settings_data(self):
        self.app_data = np.load('data/app.npy', allow_pickle=True).item()

    def get_new_data_and_save(self, new_width, new_height, new_theme):
        self.app_data['width'] = new_width
        self.app_data['height'] = new_height
        self.app_data['theme'] = new_theme
        self.update()
        self.save_to_file()

    def update(self):
        Window.size = (self.app_data['width'], self.app_data['height'])
        settings.app_data = self.app_data

    def save_to_file(self):
        np.save('data/app.npy', self.app_data)
