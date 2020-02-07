import pygame as py
import math

#palette of colors
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
GRAY = (158, 148, 146)
BLACK = (0, 245, 0)
WHITE = (255, 255, 255)

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
    # create a surface into screen
    rectangle = py.Surface((0.4 * 800, 0.7 * 600 + 50))
    rectangle.fill(GRAY)
    screen.blit(rectangle, (110, 100))
    #py.draw.rect(screen, GRAY, (110, 100, 0.7 * 800, 0.7 * 600 + 50))
    for i in range(4):
        for j in range(9):
            py.draw.circle(screen, WHITE, (175 + 60* i, 130 + 50*j), 20)

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

def inradius(point, radius, mouse):
    dif = (point[0] - mouse[0], point[1] - mouse[1])
    distance = math.sqrt(dif[0]**2 + dif[1]**2)
    if distance < radius:
        return True
    else:
        return False

def changeColor():
    global color
    mouse = py.mouse.get_pos()
    if inradius((80, 120), 20, mouse):
        color = RED
    elif inradius((80, 170), 20, mouse):
        color = BLUE
    elif inradius((80, 220), 20, mouse):
        color = GREEN
    elif inradius((80, 270), 20, mouse):
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