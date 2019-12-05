#!/usr/bin/python3
import sys


with open('5.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
data = lines[0].split(",")
data = [int(x) for x in data]

ip = 0
while ip >= 0:
    op = data[ip]
    # print(op)
    mode = [0] * 3
    for i in range(3):
        mode[2 - i] = op // pow(10, 4 - i)
        op %= pow(10, 4 - i)

    # Check ops
    if op == 1:
        parm1 = data[ip+1] if mode[0] else data[data[ip+1]]
        parm2 = data[ip+2] if mode[1] else data[data[ip+2]]
        # print('Add ', parm1, parm2)
        sub = parm1 + parm2
        data[data[ip+3]] = sub
        ip += 4
    elif op == 2:
        parm1 = data[ip+1] if mode[0] else data[data[ip+1]]
        parm2 = data[ip+2] if mode[1] else data[data[ip+2]]
        # print('Multiply ', parm1, parm2)
        sub = parm1 * parm2
        data[data[ip+3]] = sub
        ip += 4
    elif op == 3:
        val = int(input('Input: '))
        parm = data[ip+1]
        data[parm] = val
        ip += 2
    elif op == 4:
        parm = data[ip+1] if mode[0] else data[data[ip+1]]
        print('Output:', parm)
        ip += 2
    elif op == 5:
        parm1 = data[ip+1] if mode[0] else data[data[ip+1]]
        parm2 = data[ip+2] if mode[1] else data[data[ip+2]]
        if parm1 != 0:
            ip = parm2
        else:
            ip += 3
    elif op == 6:
        parm1 = data[ip+1] if mode[0] else data[data[ip+1]]
        parm2 = data[ip+2] if mode[1] else data[data[ip+2]]
        if parm1 == 0:
            ip = parm2
        else:
            ip += 3
    elif op == 7:
        parm1 = data[ip+1] if mode[0] else data[data[ip+1]]
        parm2 = data[ip+2] if mode[1] else data[data[ip+2]]
        if parm1 < parm2:
            data[data[ip+3]] = 1
        else:
            data[data[ip+3]] = 0
        ip += 4
    elif op == 8:
        parm1 = data[ip+1] if mode[0] else data[data[ip+1]]
        parm2 = data[ip+2] if mode[1] else data[data[ip+2]]
        if parm1 == parm2:
            data[data[ip+3]] = 1
        else:
            data[data[ip+3]] = 0
        ip += 4
    elif op == 99:
        ip = -1
    else:
        print('Error! Found op value: ', data[ip])
        sys.exit(1)
print('Done!')
