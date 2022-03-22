# write your code here
import string

def check_int(s):
    for ch in s:
        if not ch in string.digits:
            return False
    return True

def check_float(s):
    for ch in s:
        if not ch in string.digits + ".":
            return False
    return True

def check_oper(s):
    if len(s) != 1 or s[0] not in "+-*/":
        return False
    return True

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? " \
        "Stay focused!"
msg_2 = "Yes ... an interesting math operation. " \
        "You've slept through all classes, haven't you?"

good_equation = False
while not good_equation:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    try:
        x = float(x)
        if x.is_integer():
            x = int(x)
        y = float(y)
        if y.is_integer():
            y = int(y)
    except:
        print(msg_1)
        continue

    if not check_oper(oper):
        print(msg_2)
        continue

    good_equation = True

