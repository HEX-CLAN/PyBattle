import math

def calc_hex(x, y, radius):

    #     b    c
    #               
    #  a          d
    #
    #     f    e

    a = [x - radius, y]
    b = [x - radius//2, y - radius*3//4] # to correct
    c = [x + radius//2, y - radius*3//4] # to correct
    d = [x + radius, y]
    e = [x + radius//2, y + radius*3//4] # to correct
    f = [x - radius//2, y + radius*3//4] # to correct

    return a + b + c + d + e + f