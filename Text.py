# Text class is used to create text element or object
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

class Text:
    """Draw text element"""

    def __init__(self, surface, text, fontName="Consolas", fontSize=25, fontColor=(0, 0, 0), align="left", pos=(0, 0), textArea=-1):
        self.surface = surface
        self.text = text
        self.fontName = fontName
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.align = align
        self.pos = pos
        self.textArea = textArea
        self.bold = 0
        self.italic = 0

    def __len__(self):
        """Return the length of text"""
        return len(self.text)
    
    def setFontSize(self, size):
        self.fontSize = size
    
    def textDecor(self, bold=0, italic=0):
        self.bold = bold
        self.italic = italic

    def draw(self):
        self.label = pygame.font.SysFont(self.fontName, self.fontSize, self.bold, self.italic)
        self.labelSurf = self.label.render(self.text, True, self.fontColor)
        self.labelRect = self.labelSurf.get_rect()
        
        height = self.labelRect.h
        if self.align == "left":
            self.labelRect.top = self.pos[1] - height / 2
            self.labelRect.left = self.pos[0]
        elif self.align == "center":
            self.labelRect.center = (self.pos[0], self.pos[1])
        elif self.align == "right":
            self.labelRect.top = self.pos[1] - height / 2
            self.labelRect.right = self.pos[0]
        if self.textArea != -1:
            self.labelRect = self.textArea
        self.surface.blit(self.labelSurf, self.labelRect)
