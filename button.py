class Button:
    
    def __init__(self, surf, mouse, text="button", color=(225, 225, 225), rect=(0, 0, 100, 50), width=0, borderRadius=0):
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
        if self.borderRadius != 0:
            r = self.borderRadius
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
                r = self.borderRadius
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

