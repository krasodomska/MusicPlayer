import pygame
from Mechanics.DirTree import DirTree


class Arrow:
    def __init__(self):
        self.arrowUp = pygame.image.load("Graphic/upArrow.png").convert()
        self.arrowDown = pygame.image.load("Graphic/downArrow.png").convert()
        self.dirTree = DirTree()
        self.buttonLeftShift = 10
        self.buttonTopShift = 440
        self.buttonSize = 15

    def drawButton(self, displaySurf, list, listStep, leftShift, topShift, buttonSize):
        if len(list) > listStep:
            displaySurf.blit(self.arrowUp, (leftShift, topShift))
            displaySurf.blit(self.arrowDown, (leftShift, topShift + buttonSize))
