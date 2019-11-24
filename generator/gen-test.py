import random

# SETUP

seed = 42352336
width = 30
height = 20
water = 10 # min, max

# INIT

random.seed(a=seed, version=2)
map = [[0] * height for i in range(width)]

# GENERATE

def set_value(value, x, y, width, height):
    map[x][y] = value
    if value > 0:
        if x%2 == 1:
            nearby = ((x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y), (x+1, y+1))
        else:
            nearby = ((x-1, y-1), (x-1, y), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y))
        for n in nearby:
            if n[0] >= 0 and n[0] < width and n[1] >= 0 and n[1] < height and map[n[0]][n[1]] == 0:
                min_val = value - 2
                if min_val < 0:
                    min_val = 0
                v = random.randrange(min_val, value)
                set_value(v, n[0], n[1], width, height)

for r in range(water):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    set_value(5, x, y, width, height)
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    set_value(3, x, y, width, height)
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    set_value(2, x, y, width, height)


# PRINT

for a in range(40):
    for b in range(15):
        if a%2 == 0:
            print(map[b*2][a//2], "    ", end='')
        else:
            print("   "+str(map[b*2+1][a//2])+"  ", end='')
    print()
