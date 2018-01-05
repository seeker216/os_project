# coding=utf-8
import os
import time
import pyautogui

mou = open("/dev/input/mice", "rb");
width, height = pyautogui.size()
print(width)
print(height)
list = []
lasttime = 0
count = -1


class MouseClick:
    def __init__(self, xp, yp, clickType):
        self.clickTime = time.time()
        self.xp = xp
        self.yp = yp
        self.posStr = "Position:" + xp + ',' + yp
        self.area = area(self.xp, self.yp)
        if clickType == 0:
            if self.area == 1:
                self.clickType = 1
            elif self.area == 2:
                self.clickType = 2
            elif self.area == 3:
                self.clickType = 3
            elif self.area == 4:
                self.clickType = 4
            elif self.area == 5:
                self.clickType = 5
            elif self.area == 6:
                self.clickType = 6
        elif clickType == 1:
            if self.area == 1:
                self.clickType = 7
            elif self.area == 2:
                self.clickType = 8
            elif self.area == 3:
                self.clickType = 9
            elif self.area == 4:
                self.clickType = 10
            elif self.area == 5:
                self.clickType = 11
            elif self.area == 6:
                self.clickType = 12

    def printClick(self):
        if 1 <= self.clickType <=6:
            print('Left:' + self.posStr + ' ' + str(self.area) + ' ' + str(self.clickTime))
        elif 7 <= self.clickType <= 12:
            print('Right:' + self.posStr + ' ' + str(self.area) + ' ' + str(self.clickTime))

    def appendlist(self):
        global lasttime
        global count
        now = int(round(time.time() * 1000))
        if abs(now - lasttime) < 2000:
            list[count].append(self.clickType)
        else:
            temp = [self.clickType]
            list.append(temp)
            count += 1
        print(list)
        lasttime = now


def area(xp, yp):
    x = int(xp)
    y = int(yp)
    if (x < width / 3) and (y <= height / 2):
        a = 1
    elif (width / 3 <= x < width / 3 * 2) and (y <= height / 2):
        a = 2
    elif (width / 3 * 2 <= x < width) and (y <= height / 2):
        a = 3
    elif (x < width / 3) and (height / 2 < y < height):
        a = 4
    elif (width / 3 <= x < width / 3 * 2) and (height / 2 < y < height):
        a = 5
    elif (width / 3 * 2 <= x < width) and (height / 2 < y < height):
        a = 6
    return a


def m_event():
    m = mou.read(3)
    b = ord(m[0])
    bl = b & 0x1
    bm = (b & 0x4) > 0
    br = (b & 0x2) > 0
    x, y = pyautogui.position()
    xp = str(x).rjust(4)
    yp = str(y).rjust(4)
    if bl:
        clickType = 0
        click = MouseClick(xp, yp, clickType)
        click.printClick()
        click.appendlist()
    if br:
        clickType = 1
        click = MouseClick(xp, yp, clickType)
        click.printClick()
        click.appendlist()


while 1:
    m_event()
mou.close();
