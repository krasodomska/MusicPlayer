import pygame


class SongInfo:
    def __init__(self):
        # font
        # initialize font
        self.font = pygame.font.SysFont("Arial", 15)
        self.pointingDotImage = pygame.image.load("Graphic/dot.png").convert()
        self.leftShift = 20
        self.topShift = 490

    def getSongName(self, song):
        return song.songName

    def writeSongTitleAndLength(self, displaySurf, song, topShift):
        songName = self.font.render(song, 10, (255, 255, 255))
        displaySurf.blit(songName, (self.leftShift, topShift))

    def drawPointingDot(self, displaySurf, topShift):
        displaySurf.blit(self.pointingDotImage, (self.leftShift - 18, topShift))

    def drawSongDuration(self, displaySurf, topShift, length):
        myRect = pygame.Rect (5, topShift, length, 10)   #Rect(left, top, width, height)
        pygame.draw.rect(displaySurf, (255,255,255), myRect, 1)

    def writeSongList(self, displaySurf, songList, whichSongIsPlaying, listStart, listStep):
        topShift = self.topShift
        for song in songList:
            self.writeSongTitleAndLength(displaySurf, song.songName, topShift)
            topShift += 18
        if len(songList) > 0:
            dotIndex = whichSongIsPlaying - listStart
            if listStep > dotIndex >= 0:
                self.drawPointingDot(displaySurf, self.topShift + 18*dotIndex)




