from numpy import sqrt, floor, round


class HexagonalGrid:

    mapping_grid_cell_ratio = sqrt(3)/2

    def __init__(self, window_width, window_height, map_width, map_height):
        self.map_height = map_height
        self.map_width = map_width

        self.window_height = window_height
        self.window_width = window_width

        self.mapping_grid_width = map_width * 6 + 2
        self.mapping_grid_height = map_height * 4 + 2

        self.mapping_grid_cell_height = floor(self.window_height/self.mapping_grid_height)
        self.mapping_grid_cell_width = round(self.mapping_grid_cell_height*self.mapping_grid_cell_ratio)

        self.horizontal_padding = self.window_width - self.mapping_grid_width*self.mapping_grid_cell_width
        self.vertical_padding = self.window_height - self.mapping_grid_height*self.mapping_grid_cell_height

        if not self.is_padding_valid():
            self.mapping_grid_cell_width = floor(self.window_width/self.mapping_grid_width)
            self.mapping_grid_cell_height = round(self.mapping_grid_cell_width/self.mapping_grid_cell_ratio)

            self.horizontal_padding = self.window_width - self.mapping_grid_width * self.mapping_grid_cell_width
            self.vertical_padding = self.window_height - self.mapping_grid_height * self.mapping_grid_cell_height

    def is_padding_valid(self):
        return self.horizontal_padding >= 0 and self.vertical_padding >=0


def mapping_test(args):
    grid = HexagonalGrid(args[0], args[1], args[2], args[3])
    print("Window %ix%i" % (grid.window_width,grid.window_height))
    print("Grid: %ix%i" % (grid.map_width,grid.map_height))
    print("sqrt(3)/2 = %f" % grid.mapping_grid_cell_ratio)
    print("Map: %i, %i" % (grid.mapping_grid_width,grid.mapping_grid_height))
    print("Map cell: %ix%i" % (grid.mapping_grid_cell_width,grid.mapping_grid_cell_height))
    print("Map cell ratio: %f" % (grid.mapping_grid_cell_width/grid.mapping_grid_cell_height))
    print("Game scene: %ix%i" % (grid.mapping_grid_width*grid.mapping_grid_cell_width,
                                 grid.mapping_grid_height*grid.mapping_grid_cell_height))
    print("Horizontal padding: %i" % grid.horizontal_padding)
    print("Vertical padding: %i" % (grid.window_height - grid.mapping_grid_height*grid.mapping_grid_cell_height))


mapping_test([1366, 768, 20, 2])
print()
mapping_test([768, 1366, 20, 2])
print()
mapping_test([1366, 768, 2, 20])
print()
mapping_test([768, 1366, 2, 20])