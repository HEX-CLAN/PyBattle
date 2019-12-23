from kivy.graphics import Color, Ellipse
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
        self.depth = 0
        self.color = Color(rgba=(181 / 255, 209 / 255, 100 / 255, 1))
        self.index = index

        pass

    def set_depth(self, depth):
        if depth < 0 or depth > 5:
            print("ERROR: WRONG DEPTH !!!")
        else:
            self.depth = depth
            self.color.rgba = colors[depth]
  
    def center(self):
        return self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]/2

    def contains(self,point):
        return util_euk(self.center(),point) <= self.size[0]/2

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