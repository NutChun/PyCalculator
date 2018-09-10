import pygame
from Button import *
from Text import *

class Calculator:

    def __init__(self):
        pygame.init()
        self.surface = None
        self.size = None, None
        self.running = True
        self.mouse = 0, 0
        self.onclick = 0, 0
        self.bgcolor = (0, 0, 0)
    
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
        return self.onclick

    def onExec(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.onclick = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_SHIFT:
                        pass
                elif event.type == pygame.K_0 or event.key == pygame.K_KP0:
                    pass

            
            # set background color for screen
            self.surface.fill(self.bgcolor)
            # update mouse position
            self.mousePos()

            # set text for buttons
            buttons = (("C", "( )", "%", "del"),
                       ("7", "8", "9", "÷"),
                       ("4", "5", "6", "×"),
                       ("1", "2", "3", "-"),
                       (".", "0", "=", "+"))

            # determine the property of the buttons
            col = 4
            row = 5
            input_field_height = 300
            gap = 5
            btn_width = (self.size[0] - gap * (col + 1)) / col
            btn_height = (self.size[1] - input_field_height - gap * (row + 1)) / row

            # draw the buttons
            for i in range(row):
                for j in range(col):
                    xslice = gap + (btn_width + gap) * j
                    yslice = gap + (btn_height + gap) * i
                    lbound = gap + (btn_width + gap) * j
                    rbound = (btn_width + gap) * (j + 1)
                    tbound = input_field_height + (btn_height + gap) * i + gap
                    bbound = input_field_height + (btn_height + gap) * (i + 1)
                    btn = Button(self.surface, self.mouse, self.onclick, text=buttons[i][j], borderRadius=100)
                    btn.setRect((xslice, input_field_height + yslice, btn_width, btn_height))
                    btn.draw()

            self.onclick = 0, 0
            displayText = Text(self.surface, "0", pos=(self.size[0] - 20, input_field_height / 2), align="right", fontSize=40).draw()

            pygame.display.update()
        
        pygame.quit()
        quit()


if __name__ == "__main__":
    app = Calculator()
    app.setSize(400, 600)
    app.setBG((255, 255, 255))
    app.setCaption("PyCalculator")
    app.onExec()