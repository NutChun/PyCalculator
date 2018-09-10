import pygame

class Controller:

    def __init__(self, temp):
        self.temp = temp
        self.equation = []
    
    @property
    def temp(self):
        return self.temp
    
    @temp.setter
    def temp(self, temp):
        self.temp = temp

ctrl = Controller("0")
print(ctrl.temp)
ctrl.temp = "123"
print(ctrl.temp)
