import os
import numpy
from kivy import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from pybattle.utils import settings


class SettingsApp(Screen):
    MIN_WINDOW_WIDTH = 1024
    MAX_WINDOW_WIDTH = 1920
    MIN_WINDOW_HEIGHT = 768
    MAX_WINDOW_HEIGHT = 1080
    FULLSCREEN = False # (c) TODO: zaimplementować opcję zmiany na fullscreen

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app_data = {
            'width': self.MIN_WINDOW_WIDTH,
            'height': self.MIN_WINDOW_HEIGHT,
            'fullscreen': self.FULLSCREEN
        }

    def on_enter(self):
        if os.path.isfile('pybattle/data/app.npy'):
            self.read_app_settings_data()
            #self.update()
        else:
            self.create_user_file()

    def create_user_file(self):
        if not os.path.isdir('pybattle/data'):
            os.mkdir('pybattle/data')
        f = open('pybattle/data/app.npy', 'w+')
        f.close()
        numpy.save('pybattle/data/app.npy', self.app_data)

    def read_app_settings_data(self):
        self.app_data = numpy.load('pybattle/data/app.npy', allow_pickle=True).item()

    def get_new_data_and_save(self, new_width, new_height):
        self.app_data['width'] = new_width
        self.app_data['height'] = new_height
        #self.update()

    def update(self):
        #Window.size = (self.app_data['width'], self.app_data['height'])
        #Config.set('graphics', 'fullscreen', 1)
        settings.app_data = self.app_data

    def on_leave(self):
        self.update()
        numpy.save('pybattle/data/app.npy', self.app_data)
