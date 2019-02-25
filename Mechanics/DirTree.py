import os
import re
import pygame


class DirTree:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 15)
        self.root = "C:\\Users"
        self.folderNameLeftShift = 625
        self.placeForFolderName = 10
        self.startListIndex = 0
        self.finishListIndex = 25
        self.listStep = 25

        # button info
        self.buttonLeftShift = 600
        self.buttonTopShift = 30
        self.buttonSize = 15

    def dirList(self, root):
        mp3List = []
        for fileName in next(os.walk(root))[2]:
            if re.search('.mp3', fileName):
                mp3List.append(fileName)
        return [".."] + next(os.walk(root))[1] + mp3List

    def writeDirList(self, displaySurf):
        placeForFolderName = self.placeForFolderName
        if len(self.dirList(self.root)) > 25:
            printedFolderList = self.dirList(self.root)[self.startListIndex:self.finishListIndex]
        else:
            printedFolderList = self.dirList(self.root)

        for folderName in printedFolderList:
            folder = self.font.render(folderName, 10, (255, 255, 255))
            displaySurf.blit(folder, (self.folderNameLeftShift, placeForFolderName))
            nameHeight = folder.get_rect().bottom
            placeForFolderName += nameHeight

    def whatWasClicked(self, mauseX, mauseY):                               # MOUSE not MAUSE
        placeForFolderName = self.placeForFolderName                        # change to "folderNameTopShift"
        if len(self.dirList(self.root)) > self.listStep:
            printedFolderList = self.dirList(self.root)[self.startListIndex:self.finishListIndex]
        else:
            printedFolderList = self.dirList(self.root)
        for folderName in printedFolderList:
            folder = self.font.render(folderName, 10, (255, 255, 255))
            nameHeight = folder.get_rect().bottom
            nameWidth = folder.get_rect().right
            if self.folderNameLeftShift < mauseX < self.folderNameLeftShift + nameWidth \
                    and placeForFolderName < mauseY < placeForFolderName + nameHeight:
                return folderName
            placeForFolderName += nameHeight

        return ""

    def goToClicked(self, name):
        if re.search('.mp3', name):
            return [(self.root + "\\" + name), name]
        if name != "" and not re.search('.mp3', name):
            self.root += "\\" + name

    def nextPrevPartList(self, mauseX, mauseY):
        if len(self.dirList(self.root)) > self.finishListIndex:
            if self.buttonLeftShift < mauseX < self.buttonLeftShift + self.buttonSize \
                    and self.buttonTopShift + self.buttonSize < mauseY < self.buttonTopShift + 2 * self.buttonSize:
                self.startListIndex += self.listStep
                self.finishListIndex += self.listStep
        if self.startListIndex > 0:
            if self.buttonLeftShift < mauseX < self.buttonLeftShift + self.buttonSize \
                    and self.buttonTopShift < mauseY < self.buttonTopShift + self.buttonSize:
                self.startListIndex -= self.listStep
                self.finishListIndex -= self.listStep
