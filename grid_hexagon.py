from numpy import sqrt, floor, round
import pyglet


class HexagonalGrid:

    mapping_grid_cell_ratio = 2/sqrt(3)

    def __init__(self, window_width, window_height, map_width, map_height):
        self.map_height = map_height
        self.map_width = map_width

        self.window_height = window_height
        self.window_width = window_width

        self.mapping_grid_width = map_width * 3 + 1
        self.mapping_grid_height = map_height * 4 + 2

        self.mapping_grid_cell_height = int(floor(self.window_height/self.mapping_grid_height))
        self.mapping_grid_cell_width = int(round(self.mapping_grid_cell_height*self.mapping_grid_cell_ratio))

        self.horizontal_padding = self.window_width - self.mapping_grid_width*self.mapping_grid_cell_width
        self.vertical_padding = self.window_height - self.mapping_grid_height*self.mapping_grid_cell_height

        if not self.is_padding_valid():
            self.mapping_grid_cell_width = int(floor(self.window_width/self.mapping_grid_width))
            self.mapping_grid_cell_height = int(round(self.mapping_grid_cell_width/self.mapping_grid_cell_ratio))

            self.horizontal_padding = self.window_width - self.mapping_grid_width * self.mapping_grid_cell_width
            self.vertical_padding = self.window_height - self.mapping_grid_height * self.mapping_grid_cell_height

    def is_padding_valid(self):
        return self.horizontal_padding >= 0 and self.vertical_padding >= 0

    def get_index_position(self,x,y):
        return [x*self.mapping_grid_cell_width,y*self.mapping_grid_cell_height]

    def get_hex_center(self,x,y):

        center_x = 2 + 3 * x

        if x % 2 == 0:
            center_y = 4 + 4 * y
        else:
            center_y = 2 + 4 * y

        return self.get_index_position(center_x,center_y)

    def get_hex_center_index(self,x,y):

        center_x = 2 + 3 * x

        if x % 2 == 0:
            center_y = 4 + 4 * y
        else:
            center_y = 2 + 4 * y

        return [center_x,center_y]

    def get_hex_lines(self,x,y):
        center = self.get_hex_center_index(x,y)

        vertices = []
        vertices.extend(self.get_index_position(center[0] - 1, center[1] + 2))
        vertices.extend(self.get_index_position(center[0] + 1, center[1] + 2))
        vertices.extend(self.get_index_position(center[0] + 1, center[1] + 2))
        vertices.extend(self.get_index_position(center[0] + 2, center[1]))
        vertices.extend(self.get_index_position(center[0] + 2, center[1]))
        vertices.extend(self.get_index_position(center[0] + 1, center[1] - 2))
        vertices.extend(self.get_index_position(center[0] + 1, center[1] - 2))
        vertices.extend(self.get_index_position(center[0] - 1, center[1] - 2))
        vertices.extend(self.get_index_position(center[0] - 1, center[1] - 2))
        vertices.extend(self.get_index_position(center[0] - 2, center[1]))
        vertices.extend(self.get_index_position(center[0] - 2, center[1]))
        vertices.extend(self.get_index_position(center[0] - 1, center[1] + 2))
        return vertices


WIDTH = 1366
HEIGHT = 768
MAP_X = 30
MAP_Y = 15

class TestScene:
    def __init__(self):
        self.goto = TestScene
        self.grid = HexagonalGrid(WIDTH,HEIGHT,MAP_X,MAP_Y)
        self.batch = pyglet.graphics.Batch()

    def on_draw(self):
        print("Window %ix%i" % (self.grid.window_width, self.grid.window_height))
        print("Grid: %ix%i" % (self.grid.map_width, self.grid.map_height))
        print("2/sqrt(3) = %f" % self.grid.mapping_grid_cell_ratio)
        print("Map: %i, %i" % (self.grid.mapping_grid_width, self.grid.mapping_grid_height))
        print("Map cell: %ix%i" % (self.grid.mapping_grid_cell_width, self.grid.mapping_grid_cell_height))
        print("Map cell ratio: %f" % (self.grid.mapping_grid_cell_width / self.grid.mapping_grid_cell_height))
        print("Game scene: %ix%i" % (self.grid.mapping_grid_width * self.grid.mapping_grid_cell_width,
                                     self.grid.mapping_grid_height * self.grid.mapping_grid_cell_height))
        print("Horizontal padding: %i" % self.grid.horizontal_padding)
        print("Vertical padding: %i" % (self.grid.window_height - self.grid.mapping_grid_height * self.grid.mapping_grid_cell_height))
        # draw mapping grid
        points = []
        colors = []
        verticles_count = (self.grid.mapping_grid_height+1)*(self.grid.mapping_grid_width+1)
        for y in range(self.grid.mapping_grid_height+1):
            for x in range(self.grid.mapping_grid_width+1):
                points.extend(self.grid.get_index_position(x,y))
                colors.extend([255]*3)

        self.batch.add(verticles_count, pyglet.gl.GL_POINTS, None, ('v2i', points),('c3B',colors))

        #draw centers
        centers = []
        colors = []
        centers_count = self.grid.map_width*self.grid.map_height
        for y in range(self.grid.map_height):
            for x in range(self.grid.map_width):
                centers.extend(self.grid.get_hex_center(x,y))
                colors.extend([255,0,0])

        self.batch.add(centers_count, pyglet.gl.GL_POINTS, None, ('v2i', centers), ('c3B', colors))
        self.batch.draw()

        #draw_lines

        for y in range(self.grid.map_height):
            for x in range(self.grid.map_width):
                self.batch.add(12, pyglet.gl.GL_LINES, None, ('v2i', self.grid.get_hex_lines(x, y)), ('c3B', [0, 255, 0]*12))
                self.batch.draw()

window = pyglet.window.Window(WIDTH, HEIGHT)
window.scene_o = TestScene()

@window.event
def on_draw():
    window.clear()
    window.scene_o.on_draw()
    window.width = WIDTH
    window.height = HEIGHT

@window.event
def on_mouse_press(x, y, button, modifiers):
    on_draw()

pyglet.app.run()