# This is the main file
# 
# This calculator can do addition, subtract, multiplication, division, exponent,
# square root, calculate percent
# 
# You can visit my repository at
# https://github.com/nutchun/PyCalculator
# 
# Sound effects by https://picturetosound.com
# Youtube: https://www.youtube.com/c/picturetosound
# 
# This project is a part of Software Development Practice 1 course
#
# Developed by Nuttakan Chuntra
# Computer Engineering student at KMUTNB
# Student ID: 5901012630032
# Bangkok, Thailand
# Email: nut.ch40@gmail.com

import pygame
from Button import *
from Text import *
from Controller import *


class Calculator:

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(500, 10)
        self.size = None, None
        self.running = True
        self.mouse = 0, 0
        self.onclickLeft = 0, 0
        self.onreleaseLeft = 0, 0
        self.firstPressed = False
        self.onkeydown = False
        self.bgcolor = 0, 0, 0
        self.temp = "0"
        self.ctrl = Controller()
    
    def setSize(self, width, height):
        """Set window or screen size"""
        self.size = width, height
        self.surface = pygame.display.set_mode(self.size)
    
    def setBG(self, color):
        """Set screen background color"""
        self.bgcolor = color

    def setCaption(self, caption):
        """Set window caption"""
        pygame.display.set_caption(caption)
    
    def mousePos(self):
        """Update mouse position"""
        self.mouse = pygame.mouse.get_pos()

    def getSurf(self):
        """Return current window surface"""
        return self.surface

    def getMousePos(self):
        """Return current mouse position"""
        return self.mouse

    def onClick(self):
        return self.onclickLeft
    
    def keyDownEvent(self, event):
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_SHIFT:
            if event.key == pygame.K_8:
                return "×"
            elif event.key == pygame.K_EQUALS:
                return "+"
            elif event.key == pygame.K_6:
                return "xʸ"
            elif event.key == pygame.K_9:
                return "("
            elif event.key == pygame.K_0:
                return ")"
        elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
            return "0"
        elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
            return "1"
        elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
            return "2"
        elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
            return "3"
        elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
            return "4"
        elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
            return "5"
        elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
            return "6"
        elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
            return "7"
        elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
            return "8"
        elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
            return "9"
        elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
            return "."
        elif event.key == pygame.K_KP_PLUS:
            return "+"
        elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
            return "-"
        elif event.key == pygame.K_KP_MULTIPLY:
            return "×"
        elif event.key == pygame.K_SLASH or event.key == pygame.K_KP_DIVIDE:
            return "÷"
        elif event.key == pygame.K_BACKSPACE:
            return "del"
        elif event.key == pygame.K_ESCAPE:
            return "C"
        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_EQUALS:
            return "="

    def onExec(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # set the mouse position at first click
                if not self.firstPressed and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.onclickLeft = pygame.mouse.get_pos()
                    self.firstPressed = True
                #  set the position at mouse release
                if self.firstPressed and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.onreleaseLeft = pygame.mouse.get_pos()
                    self.firstPressed = False

                # keydown event
                if event.type == pygame.KEYDOWN:
                    key = self.keyDownEvent(event)
                    self.ctrl.addInput(key)
                    # self.temp = " ".join(self.ctrl.onHandle())
                    self.temp = self.ctrl.onHandle()

            
            # set background color for the screen
            self.surface.fill(self.bgcolor)

            # update mouse position
            self.mousePos()

            # set text for buttons
            buttons = [["C",  "+/-", "%", "÷", "×"],
                       ["(",   "7",  "8", "9", "-"],
                       [")",   "4",  "5", "6", "+"],
                       ["xʸ",  "1",  "2", "3", "="],
                       ["√x",  "0",  "0", ".", "="]]

            # determine the property of the buttons
            col = len(buttons[0])
            row = len(buttons)
            result_field_height = 140
            input_field_height = 40
            display_field_height = result_field_height + input_field_height
            gap = 5
            btn_width = (self.size[0] - gap * (col + 1)) / col
            btn_height = (self.size[1] - display_field_height - gap * (row + 1)) / row

            # set bg for button group panel
            pygame.draw.rect(self.surface, (40, 44, 55), (0, result_field_height, self.size[0], self.size[1] - result_field_height))
            
            # draw the buttons and send value to controller
            i = 0
            while i < row:
                j = 0
                while j < col:
                    
                    b = buttons[i][j]

                    if i > 0 and buttons[i - 1][j] == b:
                        j += 1
                        continue
                    
                    xstep = gap + (btn_width + gap) * j
                    ystep = gap + (btn_height + gap) * i
                    rowspan = 1
                    colspan = 1

                    for csp in range(j + 1, col):
                        if buttons[i][csp] != b:
                            break
                        colspan += 1
                    
                    for rsp in range(i + 1, row):
                        if buttons[rsp][j] != b:
                            break
                        rowspan += 1
                    
                    new_btn_width = btn_width * colspan + gap * (colspan - 1)
                    new_btn_height = btn_height * rowspan + gap * (rowspan - 1)

                    btn = RoundButton(self.surface, self.mouse, self.onclickLeft, self.onreleaseLeft, self.onkeydown, borderRadius=10)
                    btn.setText(b)
                    btn.setRect((xstep, display_field_height + ystep, new_btn_width, new_btn_height))

                    if b == "=":
                        btn.setBGColor((51, 235, 145))
                        btn.setSound("sound/buttonclick_big.mp3")
                    elif i == 0 or j == col - 1 or j == 0:
                        btn.setBGColor((74, 81, 99))
                        btn.setSound("sound/buttonclick_big.mp3")
                    else:
                        btn.setSound("sound/buttonclick_small.mp3")

                    # if b == "C" and self.temp == "0":
                    #     buttons[i][j] = "AC"
                    # elif b == "AC" and len(self.temp) > 0:
                    #     buttons[i][j] = "C"

                    btn.draw()
                    
                    if btn.onClick():
                        self.text = b
                        self.ctrl.addInput(b)
                        self.temp = self.ctrl.onHandle()

                    j += colspan
                i += 1
                    
            # set and draw backspace button
            backspaceButton = ImageButton(self.surface, self.mouse, self.onclickLeft, self.onreleaseLeft, self.onkeydown, "icon/outline_backspace_white_18dp.png", "icon/baseline_backspace_white_18dp.png", (40, 44, 55),(self.size[0] - 50, result_field_height + input_field_height / 2 - 15, 36, 36))
            backspaceButton.draw()

            # when click backspace button, send value to controller
            if backspaceButton.onClick():
                self.text = "del"
                self.ctrl.addInput("del")
                # self.temp = " ".join(self.ctrl.onHandle())
                self.temp = self.ctrl.onHandle()
            if self.onreleaseLeft != (0, 0):
                self.onclickLeft = 0, 0
                self.onreleaseLeft = 0, 0

            # self.onclickLeft = 0, 0
            # ctrl = Controller()
            # displayInput = Text(self.surface, self.temp, "Consolas", fontColor=(255, 255, 255), align="right", pos=(self.size[0] - 60, result_field_height + input_field_height / 2 + 4))
            # inputLength = len(displayInput)
            # if inputLength < 22:
            #     displayInput.setFontSize(25)
            # elif inputLength < 50:
            #     displayInput.setFontSize(20)
            # displayInput.draw()

            if self.temp == "":
                self.temp = "0"

            displayResult = Text(self.surface, self.temp, "Consolas", pos=(self.size[0] - 20, result_field_height / 2), align="right", fontColor=(255, 255, 255))
            resultLength = len(displayResult)
            self.ctrl.setInputLength(resultLength)

            # change font size for displayResult if it reach the limit
            if resultLength < 22:
                displayResult.setFontSize(40)
            elif resultLength < 28:
                displayResult.setFontSize(30)
            elif resultLength < 43:
                displayResult.setFontSize(20)
            else: # max 42 chars
                displayResult.setFontSize(20)
                self.temp = self.temp[:42]
            
            displayResult.draw()

            self.onkeydown = False
            pygame.display.update()
        
        pygame.quit()
        quit()


if __name__ == "__main__":
    # create Calculator object
    app = Calculator()
    app.setSize(500, 600)
    app.setBG((34, 38, 49))
    app.setCaption("PyCalculator")
    app.onExec()
