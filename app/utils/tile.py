from kivy.graphics import Color, Ellipse, Line
import numpy as np
from utils import colors
import math
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.instructions import Canvas

tile_colors = [
    colors.GREEN,
    colors.BLUE_LIGHT,
    colors.BLUE_MEDIUM,
    colors.BLUE_DARK,
    colors.BLUE_DARKER,
    colors.BLUE_DARKEST]


class Tile(Canvas):
    def __init__(self, grid_pos):
        super().__init__()
 
        # PARAMETERS

        self.grid_pos = grid_pos
        self.center_pos = (0, 0)
        self.pixel_pos = (0, 0)

        self.depth = 0  # 0-5
        self.base = False
        self.player = None
        self.value = 0

        self.nearby_tiles = [
            {'grid_pos': [grid_pos[0] + 1, int(grid_pos[1]) + int(grid_pos[1]) % 2]},
            {'grid_pos': (grid_pos[0], grid_pos[1] + 1)},
            {'grid_pos': (grid_pos[0] - 1, grid_pos[1] + grid_pos[1] % 2)},
            {'grid_pos': (grid_pos[0] - 1, grid_pos[1] - 1 + grid_pos[1] % 2)},
            {'grid_pos': (grid_pos[0], grid_pos[1] - 1)},
            {'grid_pos': (grid_pos[0] + 1, grid_pos[1] - 1 + grid_pos[1] % 2)},
        ]

        # ELEMENTS

        self.hexagon_color = Color(colors.GREEN[0], colors.GREEN[1], colors.GREEN[2], colors.GREEN[3])
        self.hexagon = Ellipse(angle_start=30, angle_end=390, segments=6)

        self.player_color = None
        self.player_circle = None

        self.base_color = None
        self.base_circle = None

        self.lines = [
            {'line': None, 'line_color': None},
            {'line': None, 'line_color': None},
            {'line': None, 'line_color': None},
            {'line': None, 'line_color': None},
            {'line': None, 'line_color': None},
            {'line': None, 'line_color': None}
        ]

        # DRAW

        self.add(self.hexagon_color)
        self.add(self.hexagon)

    def set_player(self, player):
        self.player = player
        # tu powinno byc tworzenie koła gracza

    def set_base(self):
        # tu powinno byc tworzenie ramki bazy
        pass

    def add_value(self, value=0):
        if value <= 0:
            if self.base:
                self.value += 6
            else:
                self.value += 2
        else:
            self.value += value

    def set_depth(self, depth):
        self.depth = depth
        self.hexagon_color.rgba = tile_colors[depth]

    def set_pos_and_size(self, pos, size):
        self.hexagon.pos = pos
        self.hexagon.size = size
        self.center_pos = (pos[0] + size[0] / 2, pos[1] + size[1] / 2)

        # Te wartosci powinny byc obliczane a nie ustawiane na sztywno
        # self.lines[0]['line'].points = [self.center_pos[0], self.center_pos[1], self.center_pos[0] + 34, self.center_pos[1] + 20]
        # self.lines[1]['line'].points = [self.center_pos[0], self.center_pos[1], self.center_pos[0], self.center_pos[1] + 40]
        # self.lines[2]['line'].points = [self.center_pos[0], self.center_pos[1], self.center_pos[0] - 34, self.center_pos[1] + 20]
        # self.lines[3]['line'].points = [self.center_pos[0], self.center_pos[1], self.center_pos[0] - 34, self.center_pos[1] - 20]
        # self.lines[4]['line'].points = [self.center_pos[0], self.center_pos[1], self.center_pos[0], self.center_pos[1] - 40]
        # self.lines[5]['line'].points = [self.center_pos[0], self.center_pos[1], self.center_pos[0] + 34, self.center_pos[1] - 20]

    def activate_line(self, id):
        if self.lines[id]['line_color'] != None:
            if self.lines[id]['line_color'].a == 0:
                self.lines[id]['line_color'].a = 1
            else:
                self.lines[id]['line_color'].a = 0

    def contains(self, point):
        return util_distance_between_points(self.center_pos, point) <= self.hexagon.size[0] / 2

    def get_side(self, point):
        angle = util_get_angle(self.center_pos, point)
        if angle < 0:
            return int((math.degrees(angle)+360)/60)
        else:
            return int(math.degrees(angle)/60)

def util_distance_between_points(pos1, pos2):
    return np.sqrt((pos1[0] - pos2[0]) * (pos1[0] - pos2[0]) + (pos1[1] - pos2[1]) * (pos1[1] - pos2[1]))


def util_get_closest_tile(tiles, pos):
    if len(tiles) == 0:
        return None
    min_dist = util_distance_between_points(tiles[0].pixel_pos, pos)
    min_tile = tiles[0]

    for tile in tiles:
        dist = util_distance_between_points(tile.pixel_pos, pos)
        if dist < min_dist:
            min_dist = dist
            min_tile = tile
    return min_tile


def util_get_angle(pos1, pos2):
    tan = (pos2[1] - pos1[1]) / (pos2[0] - pos1[0])
    if pos2[0] > pos1[0]:
        return np.arctan(tan)
    else:
        if pos2[1] > pos1[1]:
            return np.pi + np.arctan(tan)
        else:
            return -np.pi + np.arctan(tan)
