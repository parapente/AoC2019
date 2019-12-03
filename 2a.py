#!/usr/bin/python3
import sys


with open('2.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
data = lines[0].split(",")
data = [int(x) for x in data]

# Restore gravity assist program
data[1] = 12
data[2] = 2

for pos in range(0, len(data), 4):
    if data[pos] == 1:
        sub = data[data[pos+1]] + data[data[pos+2]]
        data[data[pos+3]] = sub
    elif data[pos] == 2:
        sub = data[data[pos+1]] * data[data[pos+2]]
        data[data[pos+3]] = sub
    elif data[pos] == 99:
        break
    else:
        print('Error! Found op value: ', data[pos])
        sys.exit(1)
print('Done! Result: ', data[0])
