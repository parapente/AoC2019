#!/usr/bin/python3


with open('6.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
orbits = list()
for line in lines:
    data = line.split(')')
    orbits.append((data[0], data[1]))
numoforbits = 0
for orbit in orbits:
    objs = orbit
    numoforbits += 1
    while objs[0] != 'COM':
        for x in orbits:
            if x[1] == objs[0]:
                objs = x
                break
        numoforbits += 1
print(numoforbits)
