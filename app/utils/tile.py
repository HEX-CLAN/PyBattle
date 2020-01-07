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

        self.map = None
        self.player = None

        self.depth = 0  # 0-5
        self.base = False
        self.value = 0
        self.change = 0 # added to value in every game step

        self.nearby_tiles = [
            {'x': grid_pos[0] + 1, 'y': int(grid_pos[1]) + int(grid_pos[1]) % 2},
            {'x': grid_pos[0], 'y': grid_pos[1] + 1},
            {'x': grid_pos[0] - 1, 'y': grid_pos[1] + grid_pos[1] % 2},
            {'x': grid_pos[0] - 1, 'y': grid_pos[1] - 1 + grid_pos[1] % 2},
            {'x': grid_pos[0], 'y': grid_pos[1] - 1},
            {'x': grid_pos[0] + 1, 'y': grid_pos[1] - 1 + grid_pos[1] % 2},
        ]

        # ELEMENTS

        self.hexagon_color = Color(colors.GREEN[0], colors.GREEN[1], colors.GREEN[2], colors.GREEN[3])
        self.hexagon = Ellipse(angle_start=30, angle_end=390, segments=6)

        self.player_color = None
        self.player_circle = None

        self.base_color = None
        self.base_circle = None

        self.lines = [
            {'line': None, 'line_color': Color(0, 0, 0, 1), 'a': 34, 'b': 20}, # a i b sa tymczasowe
            {'line': None, 'line_color': Color(0, 0, 0, 1), 'a': 0, 'b': 40},
            {'line': None, 'line_color': Color(0, 0, 0, 1), 'a': -34, 'b': 20},
            {'line': None, 'line_color': Color(0, 0, 0, 1), 'a': -34, 'b': -20},
            {'line': None, 'line_color': Color(0, 0, 0, 1), 'a': 0, 'b': -40},
            {'line': None, 'line_color': Color(0, 0, 0, 1), 'a': 34, 'b': -20},
        ]

        # DRAW

        self.add(self.hexagon_color)
        self.add(self.hexagon)

    def set_player(self, player):
        self.player = player

        self.player_color = player.color
        self.player_circle = Ellipse(size=(50,50), pos=self.pixel_pos)

        self.add(self.player_color)
        self.add(self.player_circle)
        self.change += 2 # total 2 passive increase


    def set_base(self, val):
        self.base_color = Color(0, 0, 0, 1)
        self.base_circle = Line(width=1.5, circle=(self.center_pos[0], self.center_pos[1], self.hexagon.size[0] * 0.3))
        self.add(self.base_color)
        self.add(self.base_circle)
        self.change += 4 # total 6 passive increase


    def add_value(self, value=None):
        if value is None:
            self.value += self.change
        else:
            self.value += value

        if self.value > 100:
            self.value = 100

        value_pixels = self.hexagon.size[0] * 0.006 * self.value
        self.player_circle.size = (value_pixels, value_pixels)
        self.player_circle.pos = (self.center_pos[0] - value_pixels / 2, self.center_pos[1] - value_pixels / 2)
        if self.base_circle is not None:
            self.base_circle.circle=(self.center_pos[0], self.center_pos[1], self.hexagon.size[0] * 0.34)

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

    def change_line(self, player, side):

        if self.lines[side]['line'] is None:
            self.lines[side]['line_color'] = Color(0, 0, 0, 1)
            self.lines[side]['line'] = Line(width=1.5, points=[self.center_pos[0], self.center_pos[1],
                self.center_pos[0]+self.lines[side]['a'], self.center_pos[1]+self.lines[side]['b']])
            self.add(self.lines[side]['line_color'])
            self.add(self.lines[side]['line'])

            near_tile = self.map.tile[self.nearby_tiles[side]['x']][self.nearby_tiles[side]['y']]
            if near_tile.player is None:
                near_tile.set_player(player)
                player.tiles.append(near_tile)
                #near_tile.add_value(0)

        else:
            self.remove(self.lines[side]['line'])
            self.remove(self.lines[side]['line_color'])
            self.lines[side]['line_color'] = None
            self.lines[side]['line'] = None



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
    if pos2[0] == pos1[0] and pos2[1] > pos1[1]:
        return np.pi/2
    elif pos2[0] == pos1[0] and pos2[1] < pos1[1]:
        return -np.pi/2
    elif pos2[0] == pos1[0] and pos2[1] == pos1[1]:
        return 0.0
    else:
        tan = (pos2[1] - pos1[1]) / (pos2[0] - pos1[0])
        if pos2[0] > pos1[0]:
            return np.arctan(tan)
        else:
            if pos2[1] > pos1[1]:
                return np.pi + np.arctan(tan)
            else:
                return -np.pi + np.arctan(tan)
