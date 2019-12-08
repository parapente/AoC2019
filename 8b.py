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
i = 0
image = list()
while i < layerlen:
    for layer in layers:
        if layer[i] != 2:
            image.append(layer[i])
            break
    i += 1

for i in range(6):
    for j in range(25):
        if image[i * 25 + j] == 1:
            char = '*'
        else:
            char = ' '
        print(char, end='')
    print()
