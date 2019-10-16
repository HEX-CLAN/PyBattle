from numpy import sqrt, floor, round
import pyglet

# mapping grid utils and constants
mapping_grid_cell_ratio = 2/sqrt(3)
line_color = [255]*4


def get_index_position(x, y,mapping_grid_cell_width,mapping_grid_cell_height):
    return x * mapping_grid_cell_width, y * mapping_grid_cell_height


def get_hex_center(x, y,mapping_grid_cell_width,mapping_grid_cell_height):
    x_index, y_index = get_hex_center_index(x, y)
    return get_index_position(x_index, y_index,mapping_grid_cell_width,mapping_grid_cell_height)


def get_hex_center_index(x, y):
    center_x = 2 + 3 * x
    if x % 2 == 0:
        center_y = 4 + 4 * y
    else:
        center_y = 2 + 4 * y
    return center_x, center_y


class Cell:
    line_offsets = [
        [-1, 2],
        [1, 2],
        [2, 0],
        [1, -2],
        [-1, -2],
        [-2, 0]
    ]

    def __init__(self, x, y, grid):
        self.grid_x = x
        self.grid_y = y
        self.grid = grid

        self.center_x_index, self.center_y_index = get_hex_center_index(x, y)
        self.center_x_pos, self.center_y_pos = get_index_position(
            self.center_x_index,
            self.center_y_index,
            self.grid.mapping_grid_cell_width,
            self.grid.mapping_grid_cell_height
        )

        self.lines = self.get_lines()
        self.dirty = 1

    def on_draw(self):
        #if self.dirty:
        col = [y for y in line_color for x in range(int(len(self.lines)/2))]
        self.grid.batch.add(int(len(self.lines)/2), pyglet.gl.GL_LINES, None, ('v2i', self.lines), ('c4B', col))
        #self.dirty = 0

    def on_update(self):
        self.dirty = 1

    def get_lines(self):
        lines = []
        for i in range(6):
            lines.extend(get_index_position(
                self.center_x_index + Cell.line_offsets[i][0],
                self.center_y_index + Cell.line_offsets[i][1],
                self.grid.mapping_grid_cell_width,
                self.grid.mapping_grid_cell_height
            ))
            lines.extend(get_index_position(
                self.center_x_index + Cell.line_offsets[(i + 1) % 6][0],
                self.center_y_index + Cell.line_offsets[(i + 1) % 6][1],
                self.grid.mapping_grid_cell_width,
                self.grid.mapping_grid_cell_height
            ))

        return lines


class Grid:
    def __init__(self, window_width, window_height, map_width, map_height):
        self.map_height, self.map_width = map_height, map_width
        self.window_height, self.window_width = window_height, window_width

        self.mapping_grid_width, self.mapping_grid_height = self.get_mapping_grid_size()
        self.mapping_grid_cell_width, self.mapping_grid_cell_height = self.get_mapping_cell_size_v()

        self.horizontal_padding, self.vertical_padding = self.get_padding()

        if not self.is_padding_valid():
            self.mapping_grid_cell_width, self.mapping_grid_cell_height = self.get_mapping_cell_size_h()
            self.horizontal_padding, self.vertical_padding = self.get_padding()

        self.cells = self.create_cells()
        self.batch = None

    def get_mapping_grid_size(self):
        return self.map_width * 3 + 1, self.map_height * 4 + 2

    def get_mapping_cell_size_v(self):
        y = int(floor(self.window_height / self.mapping_grid_height))
        x = int(round(y * mapping_grid_cell_ratio))
        return x, y

    def get_mapping_cell_size_h(self):
        x = int(floor(self.window_width / self.mapping_grid_width))
        y = int(round(x / mapping_grid_cell_ratio))

        return x, y

    def create_cells(self):
        cells = []
        for y in range(self.map_height):
            for x in range(self.map_width):
                cells.append(Cell(x, y, self))
        return cells

    def get_padding(self):
        return self.window_width - self.mapping_grid_width * self.mapping_grid_cell_width,\
               self.window_height - self.mapping_grid_height * self.mapping_grid_cell_height

    def is_padding_valid(self):
        return self.horizontal_padding >= 0 and self.vertical_padding >= 0

    def on_draw(self):
        self.batch = pyglet.graphics.Batch()
        for cell in self.cells:
            cell.on_draw()
        self.batch.draw()

    def on_update(self):
        for cell in self.cells:
            cell.on_update()
