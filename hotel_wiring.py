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

t = get_number()

for ts in range(t):
    m = get_number()
    n = get_number()
    k = get_number()
    
    no_of_rooms = (m * n)
    temp = []
    
    for floor in range(m):
        temp.append(get_number())
    nTemp = sorted(temp)
    new_room = []
   
    if k == 1:
        small_floor = nTemp.pop(0)
        on_room = n - small_floor
        print(on_room + sum(nTemp))

    else:
        small_floors = nTemp[0:k]
        nTemp2 = nTemp[k:]
        for i in small_floors:
            nr = n - i
            new_room.append(nr)
        print(sum(new_room) + sum(nTemp2))

"""
SAMPLE INPUT
2
2 2 1
2
0
2 4 2
0
3

OUTPUT
4
5
"""