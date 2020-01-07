from utils import settings
from kivy.graphics import Color


class Player:
    def __init__(self, map, main=False):
        self.main = main
        self.map = map

        if main == True:
            self.color_name = settings.game_data['player_color']
            self.color = Color(0.8, 0, 0, 1)
        else:
            self.color_name = "inny"
            self.color = Color(0, 0, 0.8, 1)

        first_tile = self.map.random_free_tile()
        first_tile.set_player(self)
        first_tile.set_base(True)
        first_tile.add_value(10)

        self.tiles = [first_tile]



    def update(self):

        if not self.main:
            # tutaj wykonuje sie ruch sztucznej inteligencji
            pass

        # 1. obliczenie gdzie ile dodac punktow

        for t in self.tiles:
            t.add_value() # auto value





        # 2. dodanie punktow
        pass
