from numpy import sqrt, floor, round


class HexagonalGrid:

    mapping_grid_cell_ratio = 2/sqrt(3)

    def __init__(self, window_width, window_height, map_width, map_height):
        print(str([window_width, window_height, map_width, map_height]))
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