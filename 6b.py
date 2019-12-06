#!/usr/bin/python3


with open('6.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
orbits = list()
for line in lines:
    data = line.split(')')
    orbits.append((data[0], data[1]))
youorbits = list()
sanorbits = list()
for orbit in orbits:
    if orbit[1] == 'YOU':
        objs = orbit
        youorbits.append(objs[0])
        while objs[0] != 'COM':
            for x in orbits:
                if x[1] == objs[0]:
                    objs = x
                    break
            youorbits.append(objs[0])
    if orbit[1] == 'SAN':
        objs = orbit
        sanorbits.append(objs[0])
        while objs[0] != 'COM':
            for x in orbits:
                if x[1] == objs[0]:
                    objs = x
                    break
            sanorbits.append(objs[0])
# print(youorbits)
# print(sanorbits)
# Find where the path diverges
yi = len(youorbits) - 1
si = len(sanorbits) - 1
while youorbits[yi] == sanorbits[si]:
    yi -= 1
    si -= 1
    if (yi == 0) or (si == 0):
        break
# print('Path diverges in :', yi, si)
# print(youorbits[:yi+1])
minorbtransfers = len(youorbits[:yi+1]) + len(sanorbits[:si+1])
print(minorbtransfers)
