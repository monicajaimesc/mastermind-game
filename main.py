import pygame as py
import math
import random

#palette of colors
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0, 0.5)
YELLOW = (255,255,0)
GRAY = (158, 148, 146)
BLACK = (0, 245, 0)
WHITE = (255, 255, 255)
TRANSPARENCY = (0, 0, 0, 125)

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
    rectangle = py.Surface((0.4 * 800, 0.8 * 600 + 50))
    rectangle.fill(GRAY)
    screen.blit(rectangle, (110, 100))
    #py.draw.rect(screen, GRAY, (110, 100, 0.7 * 800, 0.7 * 600 + 50))
    py.draw.rect(screen, GRAY, (110, 100, 0.7 * 800, 0.7 * 600 + 50))
    # Botton save
    py.draw.circle(screen, RED, (int(0.55 * 800), int(0.90 * 600)), 20)
    positions = []
    for i in range(4):
        layer = []
        for j in range(9):
            layer.append((175 + 60* i, 130 + 50*j))
            py.draw.circle(screen, WHITE, (175 + 60* i, 130 + 50*j), 20)
        positions.append(layer)

    # serie ganadora!!!
    serie_ganadora = correct_number()
    # traspone postion into resutl 
    result = []
    for i in range(len(positions[0])):
        result.append(list(map(lambda x: x[i], positions)))
    # igualations
    positions = result
    #print(positions)
    color_pos = [(80, 120), (80, 170), (80, 220), (80, 270)]
    # game loop
    run = True
    counter = 0
    
    while run:
        dict_result = {}
        for event in py.event.get():
            
            # insert loop here for all layers
            if event.type == py.MOUSEBUTTONUP:
                # print circles
                mouse = py.mouse.get_pos()
                if clickchecker(color_pos, mouse):
                    changeColor()
                    pos=getPos()
                    changeColor()

                elif clickchecker(positions[counter], mouse):
                    #returns the position where to start to draw
                    tupla = clicklayer(positions[counter], mouse)
                    if color is not None:
                        dict_result[str(tupla)] = color
                        switchcolor(tupla)
                elif clickchecker([(int(0.55 * 800), int(0.90 * 600))], mouse):
                    # check if the click it's in save
                    state = send_input(dict_result, serie_ganadora)
                    if state == 'Gano':
                        print('You win!')
                    else:
                        print("Hits: {}, Coincidences: {}".format(state[0], state[1]))
                    counter += 1
                #drawCircle()
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
    # catch the click
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

def drawCircle(r):
    changeColor()
    pos=getPos()
    changeColor()
    py.draw.circle(screen, color, pos, 20)

def clickchecker(layer_fun, click):
    for i in layer_fun:
        if inradius(i, 20, click):
            return True
    return False

def clicklayer(layer_fun, click):
    changeColor()
    pos=getPos()
    changeColor()
    for i in layer_fun:
        if inradius(i, 20, click):
            return i

def switchcolor(tupla):
    py.draw.circle(screen, color, tupla, 20)

def correct_number():
    lista = [RED, BLUE, GREEN, YELLOW]
    serie = {}
    for i in range(4):
        #lista[random.randrange(1, 4)]
        serie[str(i)] = lista[random.randrange(1, 4)]
    return serie

def send_input(dict_layer, serie):
    counter = 0
    hint = 0
    for i in dict_layer.keys():
        print("DEbuggging: {}, {}".format(counter, hint))
        if '130' in i:
            if dict_layer[i] == serie['0']:
                counter += 1
            elif dict_layer[i] in serie.values():
                hint += 1
        elif '180' in i:
            if dict_layer[i] == serie['1']:
                counter += 1
            elif dict_layer[i] in serie.values():
                hint += 1
        # after 230 will be 280 an so on..
        elif '230' in i:
            if dict_layer[i] == serie['2']:
                counter += 1
            elif dict_layer[i] in serie.values():
                hint += 1
        elif '280' in i:
            if dict_layer[i] == serie['3']:
                counter += 1
            elif dict_layer[i] in serie.values():
                hint += 1
    if counter == 4:
        return 'Gano'
    else:
        return (counter, hint)
    



if __name__ == '__main__':
    main()