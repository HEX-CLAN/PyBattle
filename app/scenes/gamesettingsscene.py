import os

import numpy as np
from kivy.uix.screenmanager import Screen


class GameSettingsScene(Screen):
    MIN_WATER_LEVEL = 0
    MAX_WATER_LEVEL = 100
    DEFAULT_PLAYER_COLOR = 'red'  # TODO: ustawić domyślny kolor gracza

    def __init__(self, **kw):
        super().__init__(**kw)
        self.game_data = {
            'water_level': self.MIN_WATER_LEVEL,  # TODO: ustawić domyślną ilość wody
            'player_color': self.DEFAULT_PLAYER_COLOR
        }
        if os.path.isfile('data/game.npy'):
            self.read_game_settings_data()
        else:
            self.create_game_file()

    def create_game_file(self):
        f = open('data/game.npy', 'w+')
        f.close()
        np.save('data/game.npy', self.game_data)

    def read_game_settings_data(self):
        self.game_data = np.load('data/game.npy', allow_pickle=True).item()

    def get_new_data_and_save(self, new_water_level, new_player_color):
        self.game_data['water_level'] = new_water_level
        self.game_data['player_color'] = new_player_color
        self.save_to_file()

    def save_to_file(self):
        np.save('data/game.npy', self.game_data)
