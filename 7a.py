#!/usr/bin/python3
import sys
from itertools import permutations


def amplifier(prog, inp_list):
    retval = 0
    ip = 0
    while ip >= 0:
        op = prog[ip]
        # print(op)
        mode = [0] * 3
        for i in range(3):
            mode[2 - i] = op // pow(10, 4 - i)
            op %= pow(10, 4 - i)

        # Check ops
        if op == 1:
            parm1 = prog[ip+1] if mode[0] else prog[prog[ip+1]]
            parm2 = prog[ip+2] if mode[1] else prog[prog[ip+2]]
            # print('Add ', parm1, parm2)
            sub = parm1 + parm2
            prog[prog[ip+3]] = sub
            ip += 4
        elif op == 2:
            parm1 = prog[ip+1] if mode[0] else prog[prog[ip+1]]
            parm2 = prog[ip+2] if mode[1] else prog[prog[ip+2]]
            # print('Multiply ', parm1, parm2)
            sub = parm1 * parm2
            prog[prog[ip+3]] = sub
            ip += 4
        elif op == 3:
            val = inp_list.pop()
            parm = prog[ip+1]
            prog[parm] = val
            ip += 2
        elif op == 4:
            parm = prog[ip+1] if mode[0] else prog[prog[ip+1]]
            retval = parm
            ip += 2
        elif op == 5:
            parm1 = prog[ip+1] if mode[0] else prog[prog[ip+1]]
            parm2 = prog[ip+2] if mode[1] else prog[prog[ip+2]]
            if parm1 != 0:
                ip = parm2
            else:
                ip += 3
        elif op == 6:
            parm1 = prog[ip+1] if mode[0] else prog[prog[ip+1]]
            parm2 = prog[ip+2] if mode[1] else prog[prog[ip+2]]
            if parm1 == 0:
                ip = parm2
            else:
                ip += 3
        elif op == 7:
            parm1 = prog[ip+1] if mode[0] else prog[prog[ip+1]]
            parm2 = prog[ip+2] if mode[1] else prog[prog[ip+2]]
            if parm1 < parm2:
                prog[prog[ip+3]] = 1
            else:
                prog[prog[ip+3]] = 0
            ip += 4
        elif op == 8:
            parm1 = prog[ip+1] if mode[0] else prog[prog[ip+1]]
            parm2 = prog[ip+2] if mode[1] else prog[prog[ip+2]]
            if parm1 == parm2:
                prog[prog[ip+3]] = 1
            else:
                prog[prog[ip+3]] = 0
            ip += 4
        elif op == 99:
            ip = -1
        else:
            print('Error! Found op value: ', prog[ip])
            sys.exit(1)
    return retval


with open('7.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
data = lines[0].split(",")
data = [int(x) for x in data]

testsets = list(permutations(range(5)))
phase_seq = list()
ampinput = 0
maxsignal = 0
maxsig_seq = list()
for testset in testsets:
    phase_seq = testset
    ampinput = 0
    for phase in phase_seq:
        ampinput = amplifier(data, [ampinput, phase])
    # print(ampinput)
    if ampinput > maxsignal:
        maxsignal = ampinput
        maxsiq_seq = testset[:]

print('Done!')
print('Max signal:', maxsignal)
print('Sequence:', maxsiq_seq)
