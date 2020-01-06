import numpy
from kivy.uix.screenmanager import Screen
from utils.map import Map
from utils import settings
from utils.player import Player


class GameScene(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.map = Map()
        self.canvas.add(self.map.canvas)

        self.amount_of_players = int(settings.game_data['amount_of_players'])
        self.main_player = Player(self.map, main=True)
        self.other_players = []
        for x in range(self.amount_of_players - 1):
            self.other_players.append(Player(self.map, main=False))

    def on_update(self):

        self.main_player.update()
        for x in range(self.amount_of_players - 1):
            self.other_players.update()

        # gra aktualizuje się co pewną ilość sekund
        # podczas jednej aktualizacji AI wykonuje pewną ilość ruchów


    def on_enter(self):
        self.map.update_canvas(x=0, y=0, w = self.width, h = self.height)

    def on_touch_down(self, touch):
        self.map.click(position = (touch.x, touch.y))

