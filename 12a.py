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
while steps < 1000:
    steps += 1
    for i, moon in enumerate(moons):
        for j, moon2 in enumerate(moons):
            if i != j:
                for k in range(3):
                    if moon[k] > moon2[k]:
                        moonspeed[i][k] -= 1
                    if moon[k] < moon2[k]:
                        moonspeed[i][k] += 1
    for i, _ in enumerate(moons):
        for j in range(3):
            moons[i][j] += moonspeed[i][j]
    # print(steps, moons, moonspeed)

totalenergy = 0
for i, moon in enumerate(moons):
    potenergy = 0
    kinenergy = 0
    for j in range(3):
        potenergy += abs(moon[j])
        kinenergy += abs(moonspeed[i][j])
    totalenergy += potenergy * kinenergy
print(totalenergy)
