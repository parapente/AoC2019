#!/usr/bin/python3
import sys


with open('11.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
data = lines[0].split(",")
data = [int(x) for x in data]

# Let's give our computer +1MB of memory
memory = [0] * (1024 * 1024)
data.extend(memory)
ip = 0
relbase = 0

robotpos = (0, 0)  # x, y
robothead = 0  # heading (0 - up, 1 - right, 2 - down, 3 - left)
painted = dict()
outcount = 0
while ip >= 0:
    op = data[ip]
    # print(op)
    mode = [0] * 3
    for i in range(3):
        mode[2 - i] = op // pow(10, 4 - i)
        op %= pow(10, 4 - i)

    # Check ops
    if op == 1:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm1 = data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        if mode[1] == 2:
            offset = relbase
        else:
            offset = 0
        parm2 = data[ip+2] if mode[1] == 1 else data[data[ip+2] + offset]
        # print('Add ', parm1, parm2)
        sub = parm1 + parm2
        if mode[2] == 2:
            offset = relbase
        else:
            offset = 0
        data[data[ip+3] + offset] = sub
        ip += 4
    elif op == 2:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm1 = data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        if mode[1] == 2:
            offset = relbase
        else:
            offset = 0
        parm2 = data[ip+2] if mode[1] == 1 else data[data[ip+2] + offset]
        # print('Multiply ', parm1, parm2)
        sub = parm1 * parm2
        # print('Write to:', data[ip+3])
        if mode[2] == 2:
            offset = relbase
        else:
            offset = 0
        data[data[ip+3] + offset] = sub
        ip += 4
    elif op == 3:
        try:
            val = painted[robotpos]
        except KeyError:
            val = 0
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm = data[ip+1] + offset
        data[parm] = val
        ip += 2
    elif op == 4:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm = data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        print('Output:', parm)
        outcount += 1
        color = 0
        if outcount == 1:
            color = parm
            painted[robotpos] = color
        else:
            # Rotate
            if parm:
                robothead = (robothead - 4) if robothead < 4 else 0
            else:
                robothead = (robothead - 1) if robothead else 3
            # Move one step
            if robothead == 0:
                robotpos = (robotpos[0], robotpos[1] + 1)
            elif robothead == 1:
                robotpos = (robotpos[0] + 1, robotpos[1])
            elif robothead == 2:
                robotpos = (robotpos[0], robotpos[1] - 1)
            else:
                robotpos = (robotpos[0] - 1, robotpos[1])
            outcount = 0
        ip += 2
    elif op == 5:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm1 = data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        if mode[1] == 2:
            offset = relbase
        else:
            offset = 0
        parm2 = data[ip+2] if mode[1] == 1 else data[data[ip+2] + offset]
        if parm1 != 0:
            ip = parm2
        else:
            ip += 3
    elif op == 6:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm1 = data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        if mode[1] == 2:
            offset = relbase
        else:
            offset = 0
        parm2 = data[ip+2] if mode[1] == 1 else data[data[ip+2] + offset]
        if parm1 == 0:
            ip = parm2
        else:
            ip += 3
    elif op == 7:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm1 = data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        if mode[1] == 2:
            offset = relbase
        else:
            offset = 0
        parm2 = data[ip+2] if mode[1] == 1 else data[data[ip+2] + offset]
        if mode[2] == 2:
            offset = relbase
        else:
            offset = 0
        if parm1 < parm2:
            data[data[ip+3] + offset] = 1
        else:
            data[data[ip+3] + offset] = 0
        ip += 4
    elif op == 8:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        parm1 = data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        if mode[1] == 2:
            offset = relbase
        else:
            offset = 0
        parm2 = data[ip+2] if mode[1] == 1 else data[data[ip+2] + offset]
        if mode[2] == 2:
            offset = relbase
        else:
            offset = 0
        if parm1 == parm2:
            data[data[ip+3] + offset] = 1
        else:
            data[data[ip+3] + offset] = 0
        ip += 4
    elif op == 9:
        if mode[0] == 2:
            offset = relbase
        else:
            offset = 0
        relbase += data[ip+1] if mode[0] == 1 else data[data[ip+1] + offset]
        ip += 2
    elif op == 99:
        ip = -1
    else:
        print('Error! Found op value: ', data[ip])
        sys.exit(1)
print('Done!')
print('Painted panels:', len(painted))
