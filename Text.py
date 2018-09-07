import pygame

class Text:

    def __init__(self, surface, text, fontName="Leelawadee UI", fontSize=25, align="left", pos=(0, 0)):
        self.surface = surface
        self.text = text
        self.fontName = fontName
        self.fontSize = fontSize
        self.align = align
        self.pos = pos
        self.label = pygame.font.SysFont(self.fontName, self.fontSize)
        self.labelSurf = self.label.render(self.text, True, (0, 0, 0))
        self.labelRect = self.labelSurf.get_rect()
    
    def draw(self):
        if self.align == "left":
            self.labelRect.top = self.pos[1]
            self.labelRect.left = self.pos[0]
        elif self.align == "center":
            self.labelRect.center = (self.pos[0], self.pos[1])
        elif self.align == "right":
            self.labelRect.top = self.pos[1]
            self.labelRect.right = self.pos[0]
        self.surface.blit(self.labelSurf, self.labelRect)
