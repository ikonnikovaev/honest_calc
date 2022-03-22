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

def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


def check_oper(s):
    if len(s) != 1 or s[0] not in "+-*/":
        return False
    return True

def check(v1, v2, v3, msg_arr):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_arr[7]
    if (v1 == 0 or v2 == 0) and (v3 == "+" or v3 == "-" or v3 == "*"):
        msg += msg_arr[8]
    if len(msg) > 0:
        msg = msg_arr[9] + msg
    print(msg)

def do_oper(x, y, oper):
    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/" and y != 0:
        return x / y
    return None


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? " \
        "Stay focused!"
msg_2 = "Yes ... an interesting math operation. " \
        "You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_arr = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5,
           msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

memory = 0
good_equation = False
while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        #if x.is_integer():
            #x = int(x)
        y = float(y)
        #if y.is_integer():
            #y = int(y)
    except:
        print(msg_1)
        continue

    if not check_oper(oper):
        print(msg_2)
        continue

    check(x, y, oper, msg_arr)
    result = do_oper(x, y, oper)
    if result is None:
        print(msg_3)
        continue
    print(round(result, 1))

    ans_mem = None
    while ans_mem not in ["y", "n"]:
        print(msg_4)
        memorize = True
        ans_mem = input()
        if ans_mem == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index <= 12:
                    print(msg_arr[msg_index])
                    ans_mem_rep = input()
                    if ans_mem_rep == "y":
                        msg_index += 1
                    elif ans_mem_rep == "n":
                        memorize = False
                        break
            if memorize:
                memory = result
    print(msg_5)

    ans = input()
    if ans == "y":
        continue
    if ans == "n":
        break

