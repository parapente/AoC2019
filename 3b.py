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

intersections = list()
for i, wire in enumerate(wires):
    for pos in wire:
        for j, owire in enumerate(wires):
            if j > i:
                if pos in owire:
                    intersections.append((i, j, pos))
beststeps = -1
print(intersections)
for intersection in intersections:
    steps1 = 0
    print(intersection)
    line1 = lines[intersection[0]].split(',')
    x = 0
    y = 0
    for cmd in line1:
        if cmd[0] == 'U':
            num = int(cmd[1:])
            for i in range(num):
                y += 1
                steps1 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
        if cmd[0] == 'D':
            num = int(cmd[1:])
            for i in range(num):
                y -= 1
                steps1 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
        if cmd[0] == 'L':
            num = int(cmd[1:])
            for i in range(num):
                x -= 1
                steps1 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
        if cmd[0] == 'R':
            num = int(cmd[1:])
            for i in range(num):
                x += 1
                steps1 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
    steps2 = 0
    line2 = lines[intersection[1]].split(',')
    x = 0
    y = 0
    for cmd in line2:
        if cmd[0] == 'U':
            num = int(cmd[1:])
            for i in range(num):
                y += 1
                steps2 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
        if cmd[0] == 'D':
            num = int(cmd[1:])
            for i in range(num):
                y -= 1
                steps2 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
        if cmd[0] == 'L':
            num = int(cmd[1:])
            for i in range(num):
                x -= 1
                steps2 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
        if cmd[0] == 'R':
            num = int(cmd[1:])
            for i in range(num):
                x += 1
                steps2 += 1
                if (x, y) == intersection[2]:
                    break
            if (x, y) == intersection[2]:
                break
    print(steps1, steps2)
    if beststeps == -1 or beststeps > (steps1 + steps2):
        beststeps = steps1 + steps2
print(beststeps)
