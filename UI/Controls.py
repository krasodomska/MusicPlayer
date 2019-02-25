import pygame


class Button:
    def __init__(self):
        self.image = None
        self.x = None
        self.y = None
        self.height = 50
        self.width = 50
        self.leftShift = 180
        self.topShift = 425
        self.name = None

    def loadImage(self):
        pass

    def wasClicked(self, mouseX, mouseY):
        if self.x <= mouseX <= self.x + self.width and self.y <= mouseY <= self.y + self.height:
            return self.name

    def drawLocation(self):
        return (self.x, self.y)


class ControlsBox:
    def __init__(self):
        # create object for button
        self.playButton = PlayButton()
        self.pauseButton = PauseButton()
        self.nextButton = PreviousButton()
        self.previousButton = NextButton()

        self.buttonsList = [self.playButton, self.pauseButton, self.nextButton, self.previousButton]

    def loadButtons(self):
        for button in self.buttonsList:
            button.loadImage()

    def drawButtons(self, paused, displaySurf):
        # drawing buttons
        for button in self.buttonsList:
            if paused and button == self.pauseButton:
                continue
            if not paused and button == self.playButton:
                continue
            displaySurf.blit(button.image, button.drawLocation())


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
