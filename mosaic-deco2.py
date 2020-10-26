# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy
import math

w = get_number()
h = get_number()
a = get_number()
b = get_number()
m = get_number()
c = get_number()

if ((w%a) == 0) and ((h%b) == 0):
    total_tiles = (w/a) * (h/b)
    total_cost = (math.ceil(total_tiles / 10) * m)
    print(total_cost)

elif ((w%a) != 0) and ((h%b) != 0):
    res = ((w + h) * c) + m
    print(res)

elif ((w%a) != 0) and ((h%b) == 0):
    ans = ((w - a) * c) + m
    print(ans)

elif ((w%a) == 0) and ((h%b) != 0):
    wss = ((h - b) * c) + m
    print(wss)

"""
SAMPLE INPUT
8 5 3 2 100 3
OUTPUT
139

SAMPLE INPUT
5 2 3 2 100 3
OUTPUT
106

SAMPLE INPUT
98765 43210 1 1 777 1
OUTPUT
331595290005
"""