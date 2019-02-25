import pygame
import math
import random


class Animation:
    def __init__(self):
        self.pointingDotImage = pygame.image.load("Graphic/dot.png").convert()

        # frame info
        self.frameWidth = 550
        self.frameHeight = 400
        self.frameLeftShift = 5
        self.frameTopShift = 5
        # followers
        self.dotList = []
        self.chaoticDotList = []
        self.secondChaoticDotList = []
        self.listOfFolowingDotLists = []

    def drawFrame(self, displaySurf):
        myRect = pygame.Rect(self.frameLeftShift, self.frameTopShift, self.frameWidth,
                             self.frameHeight)  # Rect(left, top, width, height)
        pygame.draw.rect(displaySurf, (255, 255, 255), myRect, 1)

        for dot in self.dotList:
            pygame.draw.circle(displaySurf, dot.rgb, (dot.x, dot.y), 5, 0)

        for list in self.listOfFolowingDotLists:
            for dot in list:
                if dot.x < self.frameWidth + self.frameTopShift and dot.y < self.frameHeight + self.frameLeftShift:
                    pygame.draw.circle(displaySurf, dot.rgb, (dot.x, dot.y), 5, 0)
                else:
                    continue

    def mainCircleMove(self):
        n = 0
        for dot in self.dotList:
            dot.circlePath()
        self.trackCircle(self.dotList[0], self.chaoticDotList)
        self.trackCircle(self.chaoticDotList[0], self.secondChaoticDotList)
        for list in self.listOfFolowingDotLists:
            self.trackCircle(self.dotList[n], list)
            n += 1

    def addNFollowers(self, n):
        color = 255
        arcAlpha = (math.pi / 180) * 5
        while n > 0:
            self.dotList.append(Circle(color, color, color, arcAlpha))
            n -= 1
            color -= 20
            arcAlpha -= (math.pi / 180) * 10

    def addNChaoticFollowers(self, n, listName, color):
        while n > 0:
            listName.append(Circle(color, color, color, 0))
            n -= 1
        for dot in listName:
            dot.y = random.randint(10, self.frameHeight)
            dot.x = random.randint(10, self.frameWidth)

    def addNList(self):
        n = len(self.dotList)
        while n > 0:
            self.listOfFolowingDotLists.append([])
            n -= 1
        for listOfFolowingDot in self.listOfFolowingDotLists:
            self.addNChaoticFollowers(10, listOfFolowingDot, self.dotList[n].red)
            n += 1

    def trackCircle(self, baseDot, movingList):
        x = baseDot.x
        for dot in movingList:
            if self.frameWidth > dot.x > 5 and self.frameHeight > dot.y > 5:
                dot.shiftY = dot.y
                dot.shiftX = dot.x
                if dot.x - x <= 0:
                    dot.x = int(math.cos(dot.arcAlpha) * 5 + dot.shiftX)
                else:
                    dot.x = int(-math.cos(dot.arcAlpha) * 5 + dot.shiftX)
                dot.y = int(-math.sin(dot.arcAlpha) * 5 + dot.shiftY)
            else:
                dot.x = random.randint(10, 300)
                dot.y = random.randint(10, 550)

    def indexForChaoticCircle(self, baseDot, movingList):
        x = baseDot.x
        y = baseDot.y
        for dot in movingList:
            vectorLength = math.sqrt(math.pow(dot.x - x, 2) + math.pow(dot.y - y, 2))
            if vectorLength == 0:
                continue
            dot.arcAlpha = math.asin((dot.y - y) / vectorLength) + random.randint(0, 50) * math.pi / 180


class Circle:
    def __init__(self, r, g, b, arcAlpha):
        self.x = 400
        self.y = 10
        self.red = r
        self.green = g
        self.blue = b
        self.rgb = (self.red, self.green, self.blue)
        self.arcAlpha = arcAlpha
        self.shiftX = 0
        self.shiftY = 0

    def circlePath(self):
        self.y = int(math.sin(self.arcAlpha) * 350 * math.cos(self.arcAlpha)) + int(400 / 2) - int(
            math.cos(self.arcAlpha) * math.sin(self.arcAlpha) * 100)
        self.x = int(math.cos(self.arcAlpha) * 250) + int(550 / 2) + int(
            math.cos(self.arcAlpha) * math.sin(self.arcAlpha) * 100)
        self.arcAlpha += math.pi / 180

    def trackDot(self):
        return math.sin(self.arcAlpha)

    def goStraight(self, index):
        self.y = int(index * self.x) + self.shiftY
