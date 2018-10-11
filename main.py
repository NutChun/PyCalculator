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
from GridLayout import *


class Calculator:

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(500, 10)
        self.size = None, None
        self.running = True
        self.mouse = 0, 0
        self.onclickLeft = 0, 0
        self.bgcolor = 0, 0, 0
    
    def setSize(self, width, height):
        """Set window or screen size"""
        self.size = width, height
        self.surface = pygame.display.set_mode(self.size, pygame.VIDEORESIZE)
    
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
        """On app running"""

        onreleaseLeft = 0, 0
        firstPressed = False
        temp = ["0", "", False]
        ctrl = Controller()
        textWidth = 1

        while self.running:
            onkeydown = False
            key = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # make window resizable
                if event.type == pygame.VIDEORESIZE:
                    self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                # set the mouse position at first click
                if not firstPressed and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.onclickLeft = pygame.mouse.get_pos()
                    firstPressed = True
                #  set the position at mouse release
                if firstPressed and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    onreleaseLeft = pygame.mouse.get_pos()
                    firstPressed = False

                # keydown event
                if event.type == pygame.KEYDOWN:
                    key = self.keyDownEvent(event)
            
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
            result_field_height = 100
            input_field_height = 40
            display_field_height = result_field_height + input_field_height

            # set bg for button group panel
            pygame.draw.rect(self.surface, (40, 44, 55), (0, result_field_height, self.surface.get_width(), self.surface.get_height() - result_field_height))
            
            grid = GridLayout(buttons, (0, display_field_height, self.surface.get_width(), self.surface.get_height()), 20)

            for rect in grid.generate():
                if rect is not None:
                    btn = RoundButton(self.surface, self.mouse, self.onclickLeft, onreleaseLeft, onkeydown, borderRadius=10)
                    i, j = grid.getIndex()
                    b = buttons[i][j]
                    btn.setText(b)
                    btn.setRect((rect[0], rect[1], rect[2], rect[3]))

                    if b == "=":
                        btn.setBGColor((51, 235, 145))
                        btn.setSound("sound/buttonclick_big.mp3")
                    elif i == 0 or j == len(buttons[0]) - 1 or j == 0:
                        btn.setBGColor((74, 81, 99))
                        btn.setSound("sound/buttonclick_big.mp3")
                    else:
                        btn.setSound("sound/buttonclick_small.mp3")

                    btn.draw()
                    
                    if b == key:
                        btn.keydown()
                        
                    if btn.onClick():
                        ctrl.addInput(b)
                        temp = ctrl.onHandle()
                    
            # set and draw backspace button
            backspaceButton = ImageButton(self.surface, self.mouse, self.onclickLeft, onreleaseLeft, onkeydown, "icon/outline_backspace_white_18dp.png", "icon/baseline_backspace_white_18dp.png", (40, 44, 55),(self.surface.get_width() - 50, result_field_height + input_field_height / 2 - 15, 36, 36))
            backspaceButton.setSound("sound/buttonclick_big.mp3")
            backspaceButton.draw()

            if key == "del":
                backspaceButton.keydown()

            # when click backspace button, send value to controller
            if backspaceButton.onClick():
                self.text = "del"
                ctrl.addInput("del")
                # temp = " ".join(ctrl.onHandle())
                temp = ctrl.onHandle()
            if onreleaseLeft != (0, 0):
                self.onclickLeft = 0, 0
                onreleaseLeft = 0, 0

            # self.onclickLeft = 0, 0
            # ctrl = Controller()
            # displayInput = Text(self.surface, temp, "Consolas", fontColor=(255, 255, 255), align="right", pos=(self.surface.get_width() - 60, result_field_height + input_field_height / 2 + 4))
            # inputLength = len(displayInput)
            # if inputLength < 22:
            #     displayInput.setFontSize(25)
            # elif inputLength < 50:
            #     displayInput.setFontSize(20)
            # displayInput.draw()

            displayResult = Text(self.surface, temp[0], "Consolas", pos=(self.surface.get_width() - 20, result_field_height / 2), align="right", fontColor=(255, 255, 255))
            resultLength = len(displayResult)
            ctrl.setInputLength(resultLength)
            w = self.surface.get_width() - 40

            # change font size for displayResult if it reach the limit
            if resultLength <= w // 22:
                displayResult.setFontSize(40)
            elif resultLength <= w // 17:
                displayResult.setFontSize(30)
            elif resultLength <= w // 11:
                displayResult.setFontSize(20)
            else: # max 42 chars
                displayResult.setFontSize(20)
                temp[0] = temp[0][:w // 11]
            ctrl.setMaxChar(w // 11)


            # if re < textWidth // resultLength
            
            displayResult.draw()
            textWidth = displayResult.getRect()[2]
            # print(1//2)

            pygame.display.update()
        
        pygame.quit()
        quit()


if __name__ == "__main__":
    # create Calculator object
    app = Calculator()
    # initial size
    app.setSize(500, 600)
    app.setBG((34, 38, 49))
    app.setCaption("PyCalculator")
    app.onExec()
