#!/usr/bin/python3
import sys


with open('13.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
data = lines[0].split(",")
data = [int(x) for x in data]

# Let's give our computer +1MB of memory
memory = [0] * (1024 * 1024)
data[0] = 2  # Free to play
data.extend(memory)
ip = 0
relbase = 0
outcount = 0
outx = 0
outy = 0
outtile = 0
maxx = 0
maxy = 0
screen = dict()
ballpos = [0, 0]
balldir = 1
paddlepos = [0, 0]
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
        # print screen
        # print(chr(27) + "[2J")
        for y in range(maxy + 1):
            for x in range(maxx + 1):
                tileid = screen[(x, y)]
                if tileid == 0:
                    tile = ' '
                if tileid == 1:
                    tile = '+'
                if tileid == 2:
                    tile = '#'
                if tileid == 3:
                    tile = '='
                if tileid == 4:
                    tile = 'o'
                print(tile, end='')
            print()
        print('Score:', screen[(-1, 0)])
        # screen.clear()
        val = 0
        if balldir == 1 and (screen[(ballpos[0] + 1, ballpos[1])] != 0):
            balldir = -1
        if balldir == -1 and (screen[(ballpos[0] - 1, ballpos[1])] != 0):
            balldir = 1
        if balldir == 1:  # Right
            if ballpos[1] == (paddlepos[1] - 1):
                if ballpos[0] == (paddlepos[0] + 1):
                    val = 1
                else:
                    val = 0
            else:
                if ballpos[0] + balldir < paddlepos[0]:
                    val = -1
                if ballpos[0] + balldir == paddlepos[0]:
                    val = 0
                if ballpos[0] + balldir > paddlepos[0]:
                    val = 1
        else:  # Left
            if ballpos[1] == (paddlepos[1] - 1):
                if ballpos[0] == (paddlepos[0] - 1):
                    val = -1
                else:
                    val = 0
            else:
                if ballpos[0] + balldir < paddlepos[0]:
                    val = -1
                if ballpos[0] + balldir == paddlepos[0]:
                    val = 0
                if ballpos[0] + balldir > paddlepos[0]:
                    val = 1
        print('Suggestion:', val)
        # val = int(input('Input: '))
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
        if outcount == 0:
            outx = parm
            if outx > maxx:
                maxx = outx
        if outcount == 1:
            outy = parm
            if outy > maxy:
                maxy = outy
        if outcount == 2:
            outtile = parm
            screen[(outx, outy)] = outtile
            if outtile == 3:
                paddlepos = [outx, outy]
            elif outtile == 4:
                ballpos = [outx, outy]
        outcount = (outcount + 1) % 3
        # print(outx, outy, outtile)
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
# print('Done!')
