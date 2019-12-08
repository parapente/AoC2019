#!/usr/bin/python3


with open('8.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
data = lines[0]
data = [int(x) for x in data]

layerlen = 25 * 6
layers = list()
i = 0
for _ in range(0, len(data), layerlen):
    layers.append(data[i * layerlen:(i + 1) * layerlen])
    i += 1
minzero = 25 * 6
minzerolayer = list()
for layer in layers:
    zeros = sum(1 for x in layer if x == 0)
    if minzero > zeros:
        minzero = zeros
        minzerolayer = layer[:]

print(minzerolayer)
ones = sum(1 for x in minzerolayer if x == 1)
twos = sum(1 for x in minzerolayer if x == 2)
print(ones * twos)
