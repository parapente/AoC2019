#!/usr/bin/python3
import math


def scan(pos):
    detected = dict()
    for asteroid2 in asteroids:
        if pos != asteroid2:
            opposite = pos[1] - asteroid2[1]
            adjacent = pos[0] - asteroid2[0]
            if adjacent == 0:
                tan = opposite * math.inf
            else:
                tan = opposite / -adjacent
            quad = 4
            if adjacent > 0:
                if opposite > 0:
                    quad = 1
                else:
                    quad = 2
            else:
                if opposite < 0:
                    quad = 3
            try:
                oldpos = detected[(tan, quad)]
                newdist = abs(opposite) + abs(adjacent)
                olddist = abs(oldpos[1] - pos[1]) + abs(oldpos[0] - pos[0])
                if newdist < olddist:
                    detected[(tan, quad)] = asteroid2
            except KeyError:
                detected[(tan, quad)] = asteroid2
    return detected.copy()


with open('10.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
# print(lines)

asteroids = list()
for i, line in enumerate(lines):
    offset = 0
    j = line.find('#', offset)
    while j != -1:
        asteroids.append((j, i))
        offset = j + 1
        j = line.find('#', offset)

# print(asteroids)
maxdetected = 0
ast_of_max = (0, 0)
maxdetected_dict = dict()
seen = dict()
for asteroid in asteroids:
    # print(detected)
    seen = scan(asteroid)
    if len(seen) > maxdetected:
        maxdetected = len(seen)
        ast_of_max = asteroid
        maxdetected_dict = seen.copy()
    seen.clear()
# print(ast_of_max, maxdetected)
# print(maxdetected_dict)
asteroid_list = list(maxdetected_dict.items())
asteroid_list = sorted(asteroid_list, key=lambda e: (e[0][1], e[0][0]),
                       reverse=True)
# for i, item in enumerate(asteroid_list):
#     print(i, item)
bet = asteroid_list[199][1]
print(bet, bet[0] * 100 + bet[1])
# print(asteroid_list)
