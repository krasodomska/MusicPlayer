import pygame


class OnClickEvent:
    def __init__(self):
        self.pauseMusic = False;
        self.whatWasClicked = None

    def playMusic(self):
        if self.pauseMusic:
            self.pauseMusic = False
            pygame.mixer.music.unpause()
        else:
            self.pauseMusic = True
            pygame.mixer.music.pause()
