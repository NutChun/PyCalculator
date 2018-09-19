# In this program supports three types of button
# normal rectangular, rounded corner rectangular and image icon buttons
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
from Text import *
from main import *

class Button:

    def __init__(self, surface, mouse, onclick, onrelease, onKeyDown, rect=(0, 0, 50, 100)):
        self.surface = surface
        self.mouse = mouse
        self.onclick = onclick
        self.onrelease = onrelease
        self.onKeyDown = onKeyDown

    def onClick(self):
        lbound = self.rect[0]
        rbound = lbound + self.rect[2]
        tbound = self.rect[1]
        bbound = tbound + self.rect[3]
        if lbound < self.onclick[0] < rbound and tbound < self.onclick[1] < bbound and lbound < self.onrelease[0] < rbound and tbound < self.onrelease[1] < bbound or self.onKeyDown:
            # alpha surface when click
            s = pygame.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
            s.fill((0, 0, 0, 64))
            self.surface.blit(s, (lbound,tbound))
            return True
        return False
    

class RectButton(Button):
    """Normal rectangular button"""
    
    def __init__(self, surface, mouse, onclick, onrelease, onKeyDown, text="button", bgColor=(51, 57, 73), rect=(0, 0, 50, 100), width=0):
        Button.__init__(self, surface, mouse, onclick, onrelease, onKeyDown, rect=(0, 0, 50, 100))
        self.text = text
        self.bgColor = bgColor
        self.width = width
    
    def setText(self, text):
        self.text = text
    
    def setBGColor(self, color):
        self.bgColor = color

    def setRect(self, rect):
        self.rect = rect
    
    @property
    def buttonWidth(self, width):
        return self.width

    @buttonWidth.setter
    def buttonWidth(self, width):
        self.width = width

    @property
    def buttonSize(self):
        return (self.rect[2], self.rect[3])

    @buttonSize.setter
    def buttonSize(self, size):
        self.rect[2], self.rect[3] = size[0], size[1]
    
    def draw(self):
        pygame.draw.rect(self.surface, self.bgColor, self.rect, self.width)
        self.onHover()
        txt = Text(self.surface, self.text, "Consolas", 30, (255, 255, 255), "center", (self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2))
        txt.draw()

    def onHover(self):
        lbound = self.rect[0]
        rbound = lbound + self.rect[2]
        tbound = self.rect[1]
        bbound = tbound + self.rect[3]
        if lbound < self.mouse[0] < rbound and tbound < self.mouse[1] < bbound:
            pygame.draw.rect(self.surface, self.bgColor, self.rect, self.width)
            
            # alpha surface when hover
            s = pygame.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
            s.fill((0, 0, 0, 128))
            self.surface.blit(s, (lbound,tbound))


class RoundButton(Button):
    """Rectangular button with rounded corner"""

    def __init__(self, surface, mouse, onclick, onrelease, onKeyDown, text="button", bgColor=(51, 57, 73), rect=(0, 0, 50, 100), borderRadius=10):
        Button.__init__(self, surface, mouse, onclick, onrelease, onKeyDown, rect=(0, 0, 50, 100))
        self.borderRadius = borderRadius
        self.text = text
        self.bgColor = bgColor
        self.borderRadius = borderRadius

    def setText(self, text):
        self.text = text

    def setBGColor(self, color):
        self.bgColor = color

    def setRect(self, rect):
        self.rect = rect

    def setBorderRadius(self, radius):
        self.borderRadius = radius

    def draw(self):
        r = self.borderRadius
        rect = tuple(int(i) for i in self.rect)
        if r > min(rect[2], rect[3]) // 2: r = min(rect[2], rect[3]) // 2
        pygame.draw.rect(self.surface, self.bgColor, (rect[0], rect[1] + r, rect[2], rect[3] - 2 * r))
        pygame.draw.rect(self.surface, self.bgColor, (rect[0] + r, rect[1], rect[2] - 2 * r, rect[3]))
        pygame.draw.circle(self.surface, self.bgColor, (rect[0] + r, rect[1] + r), r)
        pygame.draw.circle(self.surface, self.bgColor, (rect[0] + rect[2] - r, rect[1] + r), r)
        pygame.draw.circle(self.surface, self.bgColor, (rect[0] + rect[2] - r, rect[1] + rect[3] - r), r)
        pygame.draw.circle(self.surface, self.bgColor, (rect[0] + r, rect[1] + rect[3] - r), r)
        self.onHover()
        txt = Text(self.surface, self.text, "Consolas", 30, (255, 255, 255), "center", (self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2))
        txt.draw()
    
    def onHover(self):
        lbound = self.rect[0]
        rbound = lbound + self.rect[2]
        tbound = self.rect[1]
        bbound = tbound + self.rect[3]
        if lbound < self.mouse[0] < rbound and tbound < self.mouse[1] < bbound:
            r = self.borderRadius
            rect = tuple(int(i) for i in self.rect)
            if r > min(rect[2], rect[3]) // 2: r = min(rect[2], rect[3]) // 2
            pygame.draw.rect(self.surface, self.bgColor, (rect[0], rect[1] + r, rect[2], rect[3] - 2 * r))
            pygame.draw.rect(self.surface, self.bgColor, (rect[0] + r, rect[1], rect[2] - 2 * r, rect[3]))
            pygame.draw.circle(self.surface, self.bgColor, (rect[0] + r, rect[1] + r), r)
            pygame.draw.circle(self.surface, self.bgColor, (rect[0] + rect[2] - r, rect[1] + r), r)
            pygame.draw.circle(self.surface, self.bgColor, (rect[0] + rect[2] - r, rect[1] + rect[3] - r), r)
            pygame.draw.circle(self.surface, self.bgColor, (rect[0] + r, rect[1] + rect[3] - r), r)

            # draw alpha surface when hover
            s = pygame.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
            s.fill((0, 0, 0, 64))
            self.surface.blit(s, (lbound,tbound))


class ImageButton(Button):
    """Rectangular button with image icon"""

    def __init__(self, surface, mouse, onclick, onrelease, onKeyDown, image, imageh, bgColor, rect=(0, 0, 50, 100)):
        Button.__init__(self, surface, mouse, onclick, onrelease, onKeyDown, rect=(0, 0, 50, 100))
        self.image = image
        self.imageh = imageh
        self.bgColor = bgColor
        self.icon = pygame.image.load(self.image)
        self.iconh = pygame.image.load(self.imageh)
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.surface, self.bgColor, self.rect)
        self.surface.blit(self.icon, (self.rect[0], self.rect[1]))
        self.onHover()
    
    def onHover(self):
        """Change icon when hover"""

        lbound = self.rect[0]
        rbound = lbound + self.rect[2]
        tbound = self.rect[1]
        bbound = tbound + self.rect[3]
        if lbound < self.mouse[0] < rbound and tbound < self.mouse[1] < bbound:
            pygame.draw.rect(self.surface, self.bgColor, self.rect)
            self.surface.blit(self.iconh, (self.rect[0], self.rect[1]))
