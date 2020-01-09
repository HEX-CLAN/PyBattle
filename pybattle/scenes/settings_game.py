import os
import numpy
from kivy.uix.screenmanager import Screen
from pybattle.utils import settings


class SettingsGame(Screen):
    MIN_WATER_LEVEL = 0
    MAX_WATER_LEVEL = 100
    MIN_AMOUNT_OF_PLAYERS = 2
    MAX_AMOUNT_OF_PLAYERS = 8
    MIN_MAP_WIDTH = 5
    MAX_MAP_WIDTH = 40
    MIN_MAP_HEIGHT = 5
    MAX_MAP_HEIGHT = 40
    MIN_GAME_SPEED = 0
    MAX_GAME_SPEED = 5
    MIN_ENEMIES_SPEED = 0
    MAX_ENEMIES_SPEED = 5

    def __init__(self, **kw):
        super().__init__(**kw)
        self.game_data = {
            'water_level': 10,
            'player_color': 'red',
            'amount_of_players': 2,
            'map_width': 30,
            'map_height': 20,
            'game_speed': 1,
            'enemies_speed': 1
        }
        if os.path.isfile('pybattle/data/game.npy'):
            self.read_game_settings_data()
            self.update()
        else:
            self.create_game_file()

    def create_game_file(self):
        if not os.path.isdir('pybattle/data'):
            os.mkdir('pybattle/data')
        f = open('pybattle/data/game.npy', 'w+')
        f.close()
        numpy.save('pybattle/data/game.npy', self.game_data)

    def read_game_settings_data(self):
        self.game_data = numpy.load('pybattle/data/game.npy', allow_pickle=True).item()

    def get_new_data_and_save(self, new_water_level, new_player_color, new_amount_of_players, new_map_width,
                              new_map_height, new_game_speed, new_enemies_speed):
        self.game_data['water_level'] = new_water_level
        self.game_data['player_color'] = new_player_color
        self.game_data['amount_of_players'] = new_amount_of_players
        self.game_data['map_width'] = new_map_width
        self.game_data['map_height'] = new_map_height
        self.game_data['game_speed'] = new_game_speed
        self.game_data['enemies_speed'] = new_enemies_speed
        self.save_to_file()

    def update(self):
        settings.game_data = self.game_data

    def save_to_file(self):
        numpy.save('pybattle/data/game.npy', self.game_data)
