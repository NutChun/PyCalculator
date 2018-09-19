import operator
# import pyperclip

def int_float(n):
    if "." in n:
        return float(n)
    return int(n)

def get_opers(oper):
    return {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow
    }[oper]

def cal(op1, oper, op2):
    return get_opers(oper)(int_float(op1), int_float(op2))

def search_cal(oper):
    order = ("^", "/", "*", "-", "+")
    n = 0
    for i in order:
        while n < len(oper):
            if i == oper[n]:
                num1 = oper[n - 1]
                op = oper[n]
                num2 = oper[n + 1]
                result = cal(num1, op, num2)
                # if i == "^" and int_float(num1) < 0 and int_float(num2) % 2 == 0: result *= -1
                oper[n + 1] = str(result)
                oper.pop(n - 1)
                oper.pop(n - 1)
                n = 0
            else:
                n += 1
        n = 0
    return oper[0]

def checkInt(num):
    if num.is_integer():
        return int(num)
    return num

while True:
    # usr_input = "1 ^ 1 + 6 + 6 * -2 - -6"
    # seperate with space
    # --- Support ---
    # Addition, Subtract, Multiplication, Division, Exponent (^) and Parentheses
    usr_input = str(input(": "))
    oper = usr_input.split()

    pointer = -1
    positive = False
    negate = False

    while pointer > -len(oper) - 1:
        if oper[pointer] == ")":
            right = pointer
            while oper[pointer][-1] != "(":
                pointer -= 1
                if oper[pointer] == ")":
                    right = pointer
            if oper[pointer] == "-(":
                negate = True
            left = pointer
            result = search_cal(oper[left + 1:right])
            if negate is True:
                 result = str(int_float(result) * -1)
            for i in range(len(oper[left:right])):
                oper.pop(left + i)
            oper[right] = result
            # positive = False
            # if int_float(result) % 2 == 0 and oper[left - 1] == "^" and oper[left - 2] == ")":
            #     positive = True
            pointer = 0
            negate = False
        pointer -= 1
    if len(oper) == 1:
        # need not to searching for parentheses again
        # print(checkInt(float(oper[0])))
        if float(oper[0]).is_integer():
            print(checkInt(float(oper[0])))
        else:
            print(checkInt(float(oper[0])))
    else:
        # print(checkInt(float(search_cal(oper))))
        if float(search_cal(oper)).is_integer():
            print(checkInt(float(search_cal(oper))))
        else:
            print(checkInt(float(search_cal(oper))))

    # print(pyperclip.paste())
# 46 + 5441540 - 4156 + 5437430

# for i 