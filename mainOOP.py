import pygame

class Calculator:

    def __init__(self):
        pygame.init()
        self.surface = None
        self.size = None, None
        self.running = True
        self.mouse = 0, 0
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

    def onExec(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
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
            input_field_height = 150
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
                    btn = Button(self.surface, self.mouse, text=buttons[i][j], borderRadius=(20, 20, 20, 20))
                    btn.setRect((xslice, input_field_height + yslice, btn_width, btn_height))
                    btn.draw()
            
            displayText = Text(self.surface, "0", pos=(self.size[0] - 20, input_field_height / 2), align="right", fontSize=40).draw()

            pygame.display.update()
        
        pygame.quit()
        quit()


class Button:
    
    def __init__(self, surf, mouse, text="button", color=(225, 225, 225), rect=(0, 0, 100, 50), width=0, borderRadius=(0, 0, 0, 0)):
        self.surf = surf
        self.mouse = mouse
        self.text = text
        self.color = color
        self.rect = rect
        self.width = width
        self.borderRadius = borderRadius
        self.label = pygame.font.SysFont("Leelawadee UI", 25)
        self.labelSurf = self.label.render(self.text, True, (0, 0, 0))
        self.labelRect = self.labelSurf.get_rect()
    
    def setText(self, text):
        self.text = text
    
    def setColor(self, color):
        self.color = color

    def setRect(self, rect):
        self.rect = rect
    
    def setWidth(self, width):
        self.width = width

    def getButtonSize(self):
        return (self.rect[2], self.rect[3])
    
    def draw(self):
        if 0 not in self.borderRadius:
            r = self.borderRadius[0]
            rect = tuple(int(i) for i in self.rect)
            if r > min(rect[2], rect[3]) // 2: r = min(rect[2], rect[3]) // 2
            pygame.draw.rect(self.surf, self.color, (rect[0], rect[1] + r, rect[2], rect[3] - 2 * r))
            pygame.draw.rect(self.surf, self.color, (rect[0] + r, rect[1], rect[2] - 2 * r, rect[3]))
            pygame.draw.circle(self.surf, self.color, (rect[0] + r, rect[1] + r), r)
            pygame.draw.circle(self.surf, self.color, (rect[0] + rect[2] - r, rect[1] + r), r)
            pygame.draw.circle(self.surf, self.color, (rect[0] + rect[2] - r, rect[1] + rect[3] - r), r)
            pygame.draw.circle(self.surf, self.color, (rect[0] + r, rect[1] + rect[3] - r), r)
            self.onHover("round")
        else:
            pygame.draw.rect(self.surf, self.color, self.rect, self.width)
            self.onHover()
        self.labelRect.center = (self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2)
        self.surf.blit(self.labelSurf, self.labelRect)

    def onHover(self, type="normal"):
        lbound = self.rect[0]
        rbound = lbound + self.rect[2]
        tbound = self.rect[1]
        bbound = tbound + self.rect[3]
        if lbound < self.mouse[0] < rbound and tbound < self.mouse[1] < bbound:
            self.setColor((200, 200, 200))
            if type == "round":
                r = self.borderRadius[0]
                rect = tuple(int(i) for i in self.rect)
                if r > min(rect[2], rect[3]) // 2: r = min(rect[2], rect[3]) // 2
                pygame.draw.rect(self.surf, self.color, (rect[0], rect[1] + r, rect[2], rect[3] - 2 * r))
                pygame.draw.rect(self.surf, self.color, (rect[0] + r, rect[1], rect[2] - 2 * r, rect[3]))
                pygame.draw.circle(self.surf, self.color, (rect[0] + r, rect[1] + r), r)
                pygame.draw.circle(self.surf, self.color, (rect[0] + rect[2] - r, rect[1] + r), r)
                pygame.draw.circle(self.surf, self.color, (rect[0] + rect[2] - r, rect[1] + rect[3] - r), r)
                pygame.draw.circle(self.surf, self.color, (rect[0] + r, rect[1] + rect[3] - r), r)
            else:
                pygame.draw.rect(self.surf, self.color, self.rect, self.width)
    
    # def onClick(self, ):


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


if __name__ == "__main__":
    app = Calculator()
    app.setSize(400, 600)
    app.setBG((255, 255, 255))
    app.setCaption("PyCalculator")
    app.onExec()