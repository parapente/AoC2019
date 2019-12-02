#!/usr/bin/python3


with open('1.dat') as f:
    lines = f.read()
modules = lines.split("\n")
modules.pop()
sumfuel = 0
for m in modules:
    partfuel = (int(m) // 3) - 2
    while partfuel > 0:
        sumfuel += partfuel
        partfuel = (partfuel // 3) - 2
print("Sum of fuel: ", sumfuel)
