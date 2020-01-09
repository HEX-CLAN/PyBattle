import numpy
from kivy.uix.screenmanager import Screen
from pybattle.utils.map import Map
from pybattle.utils import settings
from pybattle.utils.player import Player
from kivy.clock import Clock
from pybattle.utils.map import util_get_closest_tile


class Game(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)


        

    def on_update(self,delta_time):

        self.main_player.update()
        for x in range(self.amount_of_players - 1):
            self.other_players[x].update()
        print("Update")

        # gra aktualizuje się co pewną ilość sekund
        # podczas jednej aktualizacji AI wykonuje pewną ilość ruchów


    def on_enter(self):
    
        self.map = Map()
        self.canvas.add(self.map.canvas)

        self.amount_of_players = int(settings.game_data['amount_of_players'])
        self.main_player = Player(self.map, main=True)
        self.other_players = []
        for x in range(self.amount_of_players - 1):
            self.other_players.append(Player(self.map, main=False))


        self.map.update_canvas(x=0, y=0, w = self.width, h = self.height)
        Clock.schedule_interval(self.on_update, 0.1)

    def on_touch_down(self, touch):
        position = (touch.x, touch.y)
        tiles = []
        for x in range(self.map.width):
            for y in range(self.map.height):
                if self.map.tile[x][y].contains(position):
                    tiles.append(self.map.tile[x][y])

        tile = util_get_closest_tile(tiles, position)
        if tile is not None:
            side = tile.get_side(position)
            print(f"{tile.grid_pos} {side}")
            if tile in self.main_player.tiles:
                tile.change_line(self.main_player, side)
                print("TAK! TWOJE!")
            #tile.activate_line(side)
        else:
            print("Poza")


