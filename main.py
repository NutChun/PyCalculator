# This is the main file
# 
# This calculator can do addition, subtract, multiplication, division, exponent,
# square root, calculate percent
# 
# You can visit my repository at
# https://github.com/nutchun/PyCalculator
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
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_SHIFT:
                        if event.key == pygame.K_8:
                            self.ctrl.addInput("×")
                        elif event.key == pygame.K_EQUALS:
                            self.ctrl.addInput("+")
                        elif event.key == pygame.K_6:
                            self.ctrl.addInput("xʸ")
                        elif event.key == pygame.K_9:
                            self.ctrl.addInput("(")
                        elif event.key == pygame.K_0:
                            self.ctrl.addInput(")")
                    elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        self.ctrl.addInput("0")
                    elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        self.ctrl.addInput("1")
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        self.ctrl.addInput("2")
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        self.ctrl.addInput("3")
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        self.ctrl.addInput("4")
                    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        self.ctrl.addInput("5")
                    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        self.ctrl.addInput("6")
                    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        self.ctrl.addInput("7")
                    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        self.ctrl.addInput("8")
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        self.ctrl.addInput("9")
                    elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                        self.ctrl.addInput(".")
                    elif event.key == pygame.K_KP_PLUS:
                        self.ctrl.addInput("+")
                    elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                        self.ctrl.addInput("-")
                    elif event.key == pygame.K_KP_MULTIPLY:
                        self.ctrl.addInput("×")
                    elif event.key == pygame.K_SLASH or event.key == pygame.K_KP_DIVIDE:
                        self.ctrl.addInput("÷")
                    elif event.key == pygame.K_BACKSPACE:
                        self.ctrl.addInput("del")
                    elif event.key == pygame.K_ESCAPE:
                        self.ctrl.addInput("C")
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_EQUALS:
                        self.ctrl.addInput("=")
                    # self.temp = " ".join(self.ctrl.onHandle())
                    self.temp = self.ctrl.onHandle()

            
            # set background color for the screen
            self.surface.fill(self.bgcolor)

            # update mouse position
            self.mousePos()

            # set text for buttons
            buttons = [["C", "+/-", "%", "÷", "×"],
                       ["(", "7", "8", "9", "-"],
                       [")", "4", "5", "6", "+"],
                       ["xʸ", "1", "2", "3", "="],
                       ["√x", "0", "0", ".", "="]]

            # determine the property of the buttons
            col = 5
            row = 5
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
            drawVert = True
            while i < row:
                j = 0
                while j < col:
                    xstep = gap + (btn_width + gap) * j
                    ystep = gap + (btn_height + gap) * i
                    # lbound = gap + (btn_width + gap) * j
                    # rbound = (btn_width + gap) * (j + 1)
                    # tbound = display_field_height + (btn_height + gap) * i + gap
                    # bbound = display_field_height + (btn_height + gap) * (i + 1)
                    btn = RoundButton(self.surface, self.mouse, self.onclickLeft, self.onreleaseLeft, self.onkeydown, borderRadius=10)
                    if buttons[i][j] == "0":
                        new_btn_width = btn_width * 2 + gap
                        btn.setText(buttons[i][j])
                        btn.setRect((xstep, display_field_height + ystep, new_btn_width, btn_height))
                        j += 1
                    elif buttons[i][j] == "=":
                        if drawVert:
                            new_btn_height = btn_height * 2 + gap
                            btn.setText(buttons[i][j])
                            btn.setRect((xstep, display_field_height + ystep, btn_width, new_btn_height))
                            btn.setBGColor((51, 235, 145))
                            btn.draw()
                            if btn.onClick():
                                self.text = buttons[i][j]
                                self.ctrl.addInput(buttons[i][j])
                                # self.temp = " ".join(self.ctrl.onHandle())
                                self.temp = self.ctrl.onHandle()
                            drawVert = False
                        j += 1
                        continue
                    else:
                        if buttons[i][j] == "C" and self.temp == "0":
                            buttons[i][j] = "AC"
                        elif buttons[i][j] == "AC" and len(self.temp) > 0:
                            buttons[i][j] = "C"
                        btn.setText(buttons[i][j])
                        btn.setRect((xstep, display_field_height + ystep, btn_width, btn_height))
                    if i == 0 or j == col - 1 or j == 0:
                        btn.setBGColor((74, 81, 99))
                    
                    btn.draw()
                    
                    if btn.onClick():
                        self.text = buttons[i][j]
                        self.ctrl.addInput(buttons[i][j])
                        # self.temp = " ".join(self.ctrl.onHandle())
                        self.temp = self.ctrl.onHandle()

                    j += 1
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