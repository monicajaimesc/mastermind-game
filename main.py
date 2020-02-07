import pygame as py
import math

#palette of colors
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)

def main():
    global run, screen, circleRed, circleGreen, circleYellow, circleBlue

    # Initialize the pygame
    py.init()

    # create the screen
    screen = py.display.set_mode((800, 600))

    #title and icon
    py.display.set_caption("Master Mind!")
    icon = py.image.load('brain.png')
    py.display.set_icon(icon)

    # game loop
    run = True
    while run:
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONUP:
                drawCircle()
                py.display.update()
            if event.type == py.QUIT:
                run = False
        circleRed = py.draw.circle(screen, RED, (80, 120), 20)
        circleBlue = py.draw.circle(screen, BLUE, (80, 170), 20)
        circleGreen = py.draw.circle(screen, GREEN, (80, 220), 20)
        circleYellow = py.draw.circle(screen, YELLOW, (80, 270), 20)
        py.display.update()

def inradius(point, radius):
    dif = ()

def changeColor():
    global color
    mouse = py.mouse.get_pos()
    posRed = (80, 120)
    tuRed = (posRed[0] - mouse[0], posRed[1] - mouse[1])
    hRed = math.sqrt(tuRed[0] * tuRed[0] + tuRed[1] * tuRed[1])
    posBlue = (80, 170)
    tuBlue = (posBlue[0] - mouse[0], posBlue[1] - mouse[1])
    hBlue = math.sqrt(tuBlue[0] * tuBlue[0] + tuBlue[1] * tuBlue[1])
    posGreen = (80, 220)
    tuGreen = (posGreen[0] - mouse[0], posGreen[1] - mouse[1])
    hGreen = math.sqrt(tuGreen[0] * tuGreen[0] + tuGreen[1] * tuGreen[1])
    posYellow = (80, 270)
    tuYellow = (posYellow[0] - mouse[0], posYellow[1] - mouse[1])
    hYellow = math.sqrt(tuYellow[0] * tuYellow[0] + tuYellow[1] * tuYellow[1])
    if hRed < 20:
        color = RED
    elif hBlue < 20:
        color = BLUE
    elif hGreen < 20:
        color = GREEN
    elif hYellow < 20:
        color = YELLOW

def getPos():
    pos = py.mouse.get_pos()
    return pos

def drawCircle():
    changeColor()
    pos=getPos()
    changeColor()
    py.draw.circle(screen, color, pos, 20)

if __name__ == '__main__':
    main()