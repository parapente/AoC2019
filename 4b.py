#!/usr/bin/python3


with open('4.dat') as f:
    lines = f.read()
lines = lines.split("\n")
lines.pop()
numrange = lines[0].split("-")
passwords = 0
for i in range(int(numrange[0]), int(numrange[1])):
    digits = list()
    num = i
    for place in range(6):
        digits.append(num // (pow(10, 5 - place)))
        num %= pow(10, 5 - place)

    # Check for password
    if digits[0] != 0:  # Six digit number
        same = 0
        lowtohigh = True
        prev = -1
        double = False
        for digit in digits:
            if digit != prev:
                if same == 1:
                    double = True
                same = 0
            if digit < prev:
                lowtohigh = False
            if digit == prev:
                same += 1
            prev = digit
        if same == 1:
            double = True
        if double and lowtohigh:
            print('Password:', i)
            passwords += 1
print('Total passwords:', passwords)
