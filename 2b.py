#!/usr/bin/python3
import sys


with open('2.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
data = lines[0].split(",")
initstate = [int(x) for x in data]

for noun in range(100):
    for verb in range(100):
        data = initstate[:]
        data[1] = noun
        data[2] = verb

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
        if data[0] == 19690720:
            print('Done! Result:', 100 * noun + verb)
            sys.exit(0)
print('??? Pair not found!')
