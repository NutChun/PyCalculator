import pygame
import operator

pygame.init()

dp_width = 400
dp_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 255)
blue = (0, 0, 255)
navblue1 = (101, 95, 255)
navblue2 = (78, 115, 255)
navblue3 = (53, 152, 254)
navblue4 = (56, 205, 226)

gameDP = pygame.display.set_mode((dp_width, dp_height))
pygame.display.set_caption("Calculator")

clock = pygame.time.Clock()
crashed = False
op = [0]
operands = ["+", "-", "x", "/"]
result = ""
print(op)


def get_opers(oper):
    return {
        "+": operator.add,
        "-": operator.sub,
        "x": operator.mul,
        "/": operator.truediv
    }[oper]


def cal(op1, oper, op2):
    return get_opers(oper)(int(op1), int(op2))


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if mods & pygame.KMOD_SHIFT:
                if event.key == pygame.K_8:
                    if op[-1] in operands:
                        op[-1] = "x"
                    else:
                        op.append("x")
                elif event.key == pygame.K_EQUALS:
                    if op[-1] in operands:
                        op[-1] = "+"
                    else:
                        op.append("+")
            elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(0)
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(1)
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(2)
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(3)
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(4)
            elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(5)
            elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(6)
            elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(7)
            elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(8)
            elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                if len(op) == 1 and op[0] == 0:
                    op = []
                op.append(9)
            elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                if "." not in op:
                    op.append(".")
            elif event.key == pygame.K_KP_PLUS:
                if op[-1] in operands:
                    op[-1] = "+"
                else:
                    op.append("+")
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                if op[-1] in operands:
                    op[-1] = "-"
                else:
                    op.append("-")
            elif event.key == pygame.K_KP_MULTIPLY:
                if op[-1] in operands:
                    op[-1] = "x"
                else:
                    op.append("x")
            elif event.key == pygame.K_SLASH or event.key == pygame.K_KP_DIVIDE:
                if op[-1] in operands:
                    op[-1] = "/"
                else:
                    op.append("/")
            elif event.key == pygame.K_BACKSPACE:
                op = op[:-1]
                if len(op) == 0:
                    op = [0]
            elif event.key == pygame.K_ESCAPE:
                op = [0]
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                print(cal(*(result.split())))
            # print(op)
            res = ""
            for i in op:
                if i in operands:
                    res += " " + str(i) + " "
                else:
                    res += str(i)
            result = res
            print(result)

    gameDP.fill((255, 255, 255))
    buttons = ("C", "()", "%", "÷",
               "7", "8", "9", "×",
               "4", "5", "6", "-",
               "1", "2", "3", "+",
               "±", "0", ".", "=")
    mouse = pygame.mouse.get_pos()
    col = 4
    row = 5
    input_field_height = 150
    gap = 0.5
    btn_width = (dp_width - gap * (col + 1)) / col
    btn_height = (dp_height - input_field_height - gap * (row + 1)) / row
    # button bg
    pygame.draw.rect(gameDP, (0, 169, 224), (0, input_field_height - gap, dp_width, dp_height - input_field_height))
    for i in range(row):
        for j in range(col):
            xslice = gap + (btn_width + gap) * j
            yslice = gap + (btn_height + gap) * i
            lbound = gap + (btn_width + gap) * j
            rbound = (btn_width + gap) * (j + 1)
            tbound = input_field_height + (btn_height + gap) * i + gap
            bbound = input_field_height + (btn_height + gap) * (i + 1)
            pygame.draw.rect(gameDP, (255, 255, 255), (xslice, input_field_height + yslice, btn_width, btn_height))
            if lbound < mouse[0] < rbound and tbound < mouse[1] < bbound:
                # button hover color
                pygame.draw.rect(gameDP, pygame.Color(0, 169, 224, 255), (xslice, input_field_height + yslice, btn_width, btn_height))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
