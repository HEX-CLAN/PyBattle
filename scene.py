import pyglet
import utils
from grid_hexagon import HexagonalGrid
from pyglet import font
import settings


class GameScene:
    def __init__(self, width, height):
        self.goto = GameScene
        self.grid = HexagonalGrid(width, height, 30, 20)
        self.batch = pyglet.graphics.Batch()
        pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)

    def on_mouse_press(self):
        self.goto = MenuScene

    def on_draw(self):
        points = []
        colors = []
        vertices_count = (self.grid.mapping_grid_height + 1) * (self.grid.mapping_grid_width + 1)
        for y in range(self.grid.mapping_grid_height + 1):
            for x in range(self.grid.mapping_grid_width + 1):
                points.extend(self.grid.get_index_position(x, y))
                colors.extend([255] * 3)

        self.batch.add(vertices_count, pyglet.gl.GL_POINTS, None, ('v2i', points), ('c3B', colors))

        # draw centers

        centers = []
        colors = []
        centers_count = self.grid.map_width * self.grid.map_height
        for y in range(self.grid.map_height):
            for x in range(self.grid.map_width):
                centers.extend(self.grid.get_hex_center(x, y))
                colors.extend([255, 0, 0])

        self.batch.add(centers_count, pyglet.gl.GL_POINTS, None, ('v2i', centers), ('c3B', colors))

        # draw_lines

        for y in range(self.grid.map_height):
            for x in range(self.grid.map_width):
                self.batch.add(12, pyglet.gl.GL_LINES, None, ('v2i', self.grid.get_hex_lines(x, y)),
                               ('c3B', [0, 255, 0] * 12))

        self.batch.draw()


class MenuScene:
    def __init__(self, width, height):
        self.goto = MenuScene
        pyglet.font.add_file("hexagon_cup.ttf")
        pyglet.font.load('HEXAGON cup font')
        self.label = pyglet.text.Label(
            'PyBattle',
            font_name='HEXAGON cup font',
            font_size=50,
            x=width/2,
            y=height-100,
            anchor_x='center',
            color=(255, 255, 255, 255))
        pyglet.gl.glClearColor(0, 0, 0, 0)

    def on_mouse_press(self):
        self.goto = GameScene

    def on_draw(self):
        self.label.draw()
