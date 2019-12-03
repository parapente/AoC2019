#!/usr/bin/python3


with open('3.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
wires = list()
for line in lines:
    x = 0
    y = 0
    wire = dict()
    line = line.split(',')
    for cmd in line:
        if cmd[0] == 'U':
            num = int(cmd[1:])
            for i in range(num):
                y += 1
                wire[(x, y)] = 1
        if cmd[0] == 'D':
            num = int(cmd[1:])
            for i in range(num):
                y -= 1
                wire[(x, y)] = 1
        if cmd[0] == 'L':
            num = int(cmd[1:])
            for i in range(num):
                x -= 1
                wire[(x, y)] = 1
        if cmd[0] == 'R':
            num = int(cmd[1:])
            for i in range(num):
                x += 1
                wire[(x, y)] = 1

    wires.append(wire)

mindist = -1
minpos = (0, 0)
for i, wire in enumerate(wires):
    for pos in wire:
        for j, owire in enumerate(wires):
            if j > i:
                if pos in owire:
                    dist = abs(pos[0]) + abs(pos[1])
                    if (mindist == -1) or (dist < mindist):
                        mindist = dist
                        minpos = pos
print(mindist)
print(minpos)
