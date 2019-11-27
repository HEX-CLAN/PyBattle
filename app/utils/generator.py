import random
import tile

# SETUP

# seed = 42352336
# width = 30
# height = 20
# water = 10 # min, max

# INIT

# random.seed(a=seed, version=2)
# map = [[0] * height for i in range(width)]

# RANDOM GENERATOR

def set_value(map, value, x, y, width, height, max_diff):
    map[x][y].set_depth(value)
    if value > 0:
        if x%2 == 1:
            nearby = ((x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y), (x+1, y+1))
        else:
            nearby = ((x-1, y-1), (x-1, y), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y))
        for n in nearby:
            if n[0] >= 0 and n[0] < width and n[1] >= 0 and n[1] < height and map[n[0]][n[1]].depth == 0:
                v = random.randrange(value-max_diff, value)
                if v < 0: 
                    v = 0
                set_value(map, v, n[0], n[1], width, height, max_diff)


def generate_map(width, height, seed, water, max_diff):
    random.seed(a=seed, version=2)
    grid = [[0] * height for i in range(width)]

    for x in range(width):
        for y in range(height):
            grid[x][y] = tile.Tile()

    for r in range(water):
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        set_value(grid, 5, x, y, width, height, max_diff)
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        set_value(grid, 3, x, y, width, height, max_diff)
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        set_value(grid, 2, x, y, width, height, max_diff)
    return grid


# PRINT

# for a in range(40):
#     for b in range(15):
#         if a%2 == 0:
#             print(map[b*2][a//2], "    ", end='')
#         else:
#             print("   "+str(map[b*2+1][a//2])+"  ", end='')
#     print()
