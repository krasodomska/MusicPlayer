import pygame
from pygame.locals import *

class Button:
    def __init__(self):
        self.image = None
        self.x = None
        self.y = None
        self.height = 50
        self.width = 50
        self.leftShift = 0
        self.topShift = 0
        self.name = None

    def loadImage(self):
        pass

    def wasClicked(self, mouseX, mouseY):
        if mouseX >= self.x and mouseX <= self.x + self.width and mouseY >= self.y and self.y + self.height >= mouseY:
            print(self.name)
        return self.name

    def drawLocation(self):
        return (self.x, self.y)

class PlayButton(Button):
    def loadImage(self):
        self.image = pygame.image.load("Graphic/playButton.png").convert()
        self.x = self.leftShift + self.width
        self.y = self.topShift
        self.name = 'play/pause'

class PauseButton(Button):
    def loadImage(self):
        self.image = pygame.image.load("Graphic/pauseButton.png").convert()
        self.x = self.leftShift + self.width
        self.y = self.topShift
        self.name = 'pause'


class PreviousButton(Button):
    def loadImage(self):
        self.image = pygame.image.load("Graphic/previousButton.png").convert()
        self.x = self.leftShift
        self.y = self.topShift
        self.name = 'previous'

class NextButton(Button):
    def loadImage(self):
        self.image = pygame.image.load("Graphic/nextButton.png").convert()
        self.x = self.leftShift + self.width*2
        self.y = self.topShift
        self.name = 'next'
