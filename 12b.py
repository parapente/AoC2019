#!/usr/bin/python3
import re


with open('12.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
moons = list()
moonspeed = list()
for line in lines:
    m = re.match(r'<x=(-*\d+), y=(-*\d+), z=(-*\d+)\>', line)
    moons.append([int(m.group(1)), int(m.group(2)), int(m.group(3))])
    moonspeed.append([0, 0, 0])
steps = 0
# print(steps, moons, moonspeed)
posveldict = dict()
key = list()
for i, _ in enumerate(moons):
    for j in range(3):
        key.append(moons[i][j])
        key.append(moonspeed[i][j])
key = tuple(key)
print(0, key)
posveldict[key] = 1
found = False
while not found:
    steps += 1
    for i, moon in enumerate(moons):
        for j, moon2 in enumerate(moons):
            if i != j:
                for k in range(3):
                    if moon[k] > moon2[k]:
                        moonspeed[i][k] -= 1
                    if moon[k] < moon2[k]:
                        moonspeed[i][k] += 1
    key = list()
    for i, _ in enumerate(moons):
        for j in range(3):
            moons[i][j] += moonspeed[i][j]
            key.append(moons[i][j])
            key.append(moonspeed[i][j])
    key = tuple(key)
    print(steps, key)
    try:
        print('Found after', steps, '!', key, posveldict[key])
        found = True
    except KeyError:
        posveldict[key] = 1
    # print(steps, moons, moonspeed)
