from kivy.graphics import Color, Ellipse, Line
import numpy as np
from utils import colors

tile_colors = [
    colors.GREEN,
    colors.BLUE_LIGHT,
    colors.BLUE_MEDIUM,
    colors.BLUE_DARK,
    colors.BLUE_DARKER,
    colors.BLUE_DARKEST]


class Tile(Ellipse):
    def __init__(self, index):
        super().__init__(angle_start=30,
                         angle_end=390,
                         segments=6,
                         pos=(0, 0),
                         size=(0, 0))
        self.depth = 0  # 0-5
        self.color = Color(colors.GREEN[0],
                           colors.GREEN[1],
                           colors.GREEN[2],
                           colors.GREEN[3])
        self.pos_on_grid = index
        self.pos_of_center = (0, 0)  # position of Tile center in pixels

        # TODO: nie każde pole potrzebuje znać sąsiadów i zawierać obiekty Line: np woda. trzeba to ogarnąć np w generatorze
        self.nearby_tiles = [
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0),
             'tile_index': [index[0] + 1, int(index[1]) + int(index[1]) % 2]},
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0),
             'tile_index': (index[0], index[1] + 1)},
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0),
             'tile_index': (index[0] - 1, index[1] + index[1] % 2)},
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0),
             'tile_index': (index[0] - 1, index[1] - 1 + index[1] % 2)},
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0),
             'tile_index': (index[0], index[1] - 1)},
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0),
             'tile_index': (index[0] + 1, index[1] - 1 + index[1] % 2)},
        ]

        # TODO: to będzie kółko w środku Tila, które będzie rosnąć (lub nie będzie istnieć... trzeba to obmyśleć)
        # self.value_color = Color
        # self.value_circle = Ellipse

    def set_depth(self, depth):
        if depth < 0 or depth > 5:
            print("ERROR: WRONG DEPTH !!!")
        else:
            self.depth = depth
            self.color.rgba = tile_colors[depth]

    def set_pos_and_size(self, pos, size):
        self.pos = pos
        self.size = size
        self.pos_of_center = (pos[0] + size[0] / 2, pos[1] + size[1] / 2)

        # Te wartosci powinny byc obliczane a nie ustawiane na sztywno
        self.nearby_tiles[0]['line'].points = [self.pos_of_center[0], self.pos_of_center[1], self.pos_of_center[0] + 34, self.pos_of_center[1] + 20]
        self.nearby_tiles[1]['line'].points = [self.pos_of_center[0], self.pos_of_center[1], self.pos_of_center[0], self.pos_of_center[1] + 40]
        self.nearby_tiles[2]['line'].points = [self.pos_of_center[0], self.pos_of_center[1], self.pos_of_center[0] - 34, self.pos_of_center[1] + 20]
        self.nearby_tiles[3]['line'].points = [self.pos_of_center[0], self.pos_of_center[1], self.pos_of_center[0] - 34, self.pos_of_center[1] - 20]
        self.nearby_tiles[4]['line'].points = [self.pos_of_center[0], self.pos_of_center[1], self.pos_of_center[0], self.pos_of_center[1] - 40]
        self.nearby_tiles[5]['line'].points = [self.pos_of_center[0], self.pos_of_center[1], self.pos_of_center[0] + 34, self.pos_of_center[1] - 20]

    def activate_line(self, id):
        if self.nearby_tiles[id]['line_color'].a == 0:
            self.nearby_tiles[id]['line_color'].a = 1
        else:
            self.nearby_tiles[id]['line_color'].a = 0

    def contains(self, point):
        return util_distance_between_points(self.pos_of_center, point) <= self.size[0] / 2

    def get_side(self, point):
        self.angle = util_get_angle(self.pos_of_center, point)
        if self.is_between_0_and_60():
            return 0
        elif self.is_between_61_and_120():
            return 1
        elif self.is_between_121_and_180():
            return 2
        elif self.is_between_181_and_240():
            return 5
        elif self.is_between_241_and_300():
            return 4
        else:
            return 3

    def is_between_0_and_60(self):
        return 0 <= self.angle < np.pi / 3

    def is_between_61_and_120(self):
        return np.pi / 3 <= self.angle < 2 * np.pi / 3

    def is_between_121_and_180(self):
        return self.angle >= 2 * np.pi / 3

    def is_between_181_and_240(self):
        return 0 > self.angle >= -np.pi / 3

    def is_between_241_and_300(self):
        return -np.pi / 3 > self.angle >= -2 * np.pi / 3


def util_distance_between_points(pos1, pos2):
    return np.sqrt((pos1[0] - pos2[0]) * (pos1[0] - pos2[0]) + (pos1[1] - pos2[1]) * (pos1[1] - pos2[1]))


def util_get_closest_tile(tiles, pos):
    if len(tiles) == 0:
        return None
    min_dist = util_distance_between_points(tiles[0].pos, pos)
    min_tile = tiles[0]

    for tile in tiles:
        dist = util_distance_between_points(tile.pos, pos)
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
