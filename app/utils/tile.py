from kivy.graphics import Color, Ellipse, Line 
import numpy as np

colors = [
    (181 / 255, 209 / 255, 100 / 255, 1),
    ( 70 / 255, 132 / 255, 200 / 255, 1),
    ( 60 / 255, 116 / 255, 197 / 255, 1),
    ( 50 / 255,  99 / 255, 193 / 255, 1),
    ( 40 / 255,  82 / 255, 189 / 255, 1),
    ( 30 / 255,  65 / 255, 185 / 255, 1)
]


class Tile(Ellipse):
    def __init__(self,index):
        super().__init__(angle_start=30, angle_end=390, segments=6, pos=(0, 0), size=(0, 0))
        self.depth = 0 # 0-5
        self.color = Color(181 / 255, 209 / 255, 100 / 255, 1)
        self.index = index # position on grid
        self.center = (0,0) # position of Tile center in pixels

        self.nearby = [
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0), 'tile_index': [index[0] + 1, int(index[1]) + int(index[1]) % 2] },
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0), 'tile_index': (index[0], index[1] + 1) },
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0), 'tile_index': (index[0] - 1, index[1] + index[1] % 2) },
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0), 'tile_index': (index[0] - 1, index[1] - 1 + index[1] % 2)},
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0), 'tile_index': (index[0], index[1] - 1) },
            {'line': Line(width=2), 'line_color': Color(0, 0, 0, 0), 'tile_index': (index[0] + 1, index[1] - 1 + index[1] % 2)},
        ]

    def set_depth(self, depth):
        if depth < 0 or depth > 5:
            print("ERROR: WRONG DEPTH !!!")
        else:
            self.depth = depth
            self.color.rgba = colors[depth]

    def set_pos_and_size(self, pos, size):
        self.pos = pos
        self.size = size
        self.center = (pos[0] + size[0] / 2, pos[1] + size[1] / 2)

        # Te wartosci powinny byc obliczane a nie ustawiane na sztywno
        self.nearby[0]['line'].points = [self.center[0], self.center[1], self.center[0]+34, self.center[1]+20]
        self.nearby[1]['line'].points = [self.center[0], self.center[1], self.center[0], self.center[1]+40]
        self.nearby[2]['line'].points = [self.center[0], self.center[1], self.center[0]-34, self.center[1]+20]
        self.nearby[3]['line'].points = [self.center[0], self.center[1], self.center[0]-34, self.center[1]-20]
        self.nearby[4]['line'].points = [self.center[0], self.center[1], self.center[0], self.center[1]-40]
        self.nearby[5]['line'].points = [self.center[0], self.center[1], self.center[0]+34, self.center[1]-20]

    def activate_line(self, id):
        if self.nearby[id]['line_color'].a == 0:
            self.nearby[id]['line_color'].a = 1
        else:
            self.nearby[id]['line_color'].a = 0

    def contains(self,point):
        return util_euk(self.center, point) <= self.size[0] / 2

    def get_side(self,point):
        angle = util_get_angle(self.center, point)

        if angle >=0 and angle < np.pi/3:
            return 0
        elif angle >= np.pi/3 and angle < 2*np.pi/3:
            return 1
        elif angle >= 2*np.pi/3:
            return 2
        elif angle < 0 and angle >= -np.pi/3:
            return 5
        elif angle < -np.pi/3 and angle >= -2*np.pi/3:
            return 4
        else:
            return 3


def util_euk(pos1,pos2):
    return np.sqrt((pos1[0]-pos2[0])*(pos1[0]-pos2[0])+(pos1[1]-pos2[1])*(pos1[1]-pos2[1]))

def util_get_closest_tile(tiles,pos):
    if len(tiles) == 0 :
        return None
    min_dist = util_euk(tiles[0].pos,pos)
    min_tile = tiles[0]

    for tile in tiles:
        dist = util_euk(tile.pos,pos)
        if dist < min_dist:
            min_dist = dist
            min_tile = tile

    return min_tile

def util_get_angle(pos1,pos2):
    tan = (pos2[1]-pos1[1])/(pos2[0]-pos1[0])
    if pos2[0]>pos1[0]:
        return np.arctan(tan)
    else:
        if pos2[1]>pos1[1]:
            return np.pi + np.arctan(tan)
        else:
            return -np.pi + np.arctan(tan)