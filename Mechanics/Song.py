class Song:
    def __init__(self, songName, songPath):
        self.songName = songName
        self.songPath = songPath
        self.songLength = 3.50


class SongsList:
    def __init__(self):
        self.songList = []
        self.printedSongList = []
        self.startListIndex = 0
        self.finishListIndex = 5
        self.listStep = 5

        self.buttonTopShift = 440
        self.buttonLeftShift = 10
        self.buttonSize = 15

    def addSongToList(self, songName, songPath):
        self.songList.append(Song(songName, songPath))

    def nextPrevPartList(self, mauseX, mauseY):                         # german MAUSER was a powerful weapon
        if len(self.songList) > self.listStep:
            self.printedSongList = self.songList[self.startListIndex:self.finishListIndex]
        else:
            self.printedSongList = self.songList

        if len(self.songList) > self.finishListIndex:
            if self.buttonLeftShift < mauseX < self.buttonLeftShift + self.buttonSize \
                    and self.buttonTopShift + self.buttonSize < mauseY < self.buttonTopShift + 2 * self.buttonSize:
                self.startListIndex += self.listStep
                self.finishListIndex += self.listStep
                print("next")
        if self.startListIndex > 0:
            if self.buttonLeftShift < mauseX < self.buttonLeftShift + self.buttonSize \
                    and self.buttonTopShift < mauseY < self.buttonTopShift + self.buttonSize:
                self.startListIndex -= self.listStep
                self.finishListIndex -= self.listStep

        if len(self.songList) > self.listStep:
            self.printedSongList = self.songList[self.startListIndex:self.finishListIndex]
        else:
            self.printedSongList = self.songList
