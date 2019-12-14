#!/usr/bin/python3
import math


with open('10.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()

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
detected = dict()
for asteroid in asteroids:
    for asteroid2 in asteroids:
        if asteroid != asteroid2:
            opposite = asteroid2[1] - asteroid[1]
            adjacent = asteroid2[0] - asteroid[0]
            if adjacent == 0:
                tan = opposite * math.inf
            else:
                tan = opposite / adjacent
            quad = 4
            if adjacent >= 0 and opposite >= 0:
                quad = 1
            elif adjacent < 0:
                if opposite >= 0:
                    quad = 2
                else:
                    quad = 3
            detected[(tan, quad)] = 1
    # print(detected)
    if len(detected) > maxdetected:
        maxdetected = len(detected)
        ast_of_max = asteroid
    detected.clear()
print(ast_of_max, maxdetected)
