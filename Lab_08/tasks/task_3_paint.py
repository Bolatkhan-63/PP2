import pygame
import math,color

pygame.init()

WIDTH = 800
HEIGHT = 600

colors = [color.colorBLUE,color.colorGREEN,color.colorRED,color.colorWHITE,color.colorYELLOW]

toolbar_height = 100


choice = 0
run = True

color_choice = 0


screen = pygame.display.set_mode((WIDTH, HEIGHT))
glv_layer = pygame.Surface((WIDTH, HEIGHT))

glv_layer.fill(color.colorBLACK)

rect_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/rect.png")
rect_image = pygame.transform.scale(rect_image,(100,100))


def rect():
    global choice, run, glv_layer,color_choice,colors
    color_figure = colors[color_choice]
    
    clock = pygame.time.Clock()
    LMBpressed = False
    THICKNESS = 5
    currX = currY = prevX = prevY = 0
    running = True

    def calculate_rect(x1, y1, x2, y2):
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

    while running:
        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: choice = 1; running = False
                if event.key == pygame.K_2: choice = 2; running = False
                if event.key == pygame.K_3: choice = 3; running = False
                if event.key == pygame.K_4: choice = 4; running = False
                if event.key == pygame.K_EQUALS: THICKNESS += 1
                if event.key == pygame.K_MINUS: THICKNESS = max(1, THICKNESS - 1)
                if event.key == pygame.K_RIGHT: color_choice+=1
                if event.key == pygame.K_LEFT: color_choice-=1

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                LMBpressed = True
                prevX, prevY = event.pos

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                LMBpressed = False
                currX, currY = event.pos
                pygame.draw.rect(glv_layer, color_figure, calculate_rect(prevX, prevY, currX, currY), THICKNESS)


        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        color_figure = colors[color_choice]

        if LMBpressed:
            currX, currY = pygame.mouse.get_pos()
            screen.blit(glv_layer, (0, 0))
            pygame.draw.rect(screen, color_figure, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
        else:
            screen.blit(glv_layer, (0, 0))
        
        pygame.display.flip()
        clock.tick(60)

def circle():
    global choice, run, glv_layer,color_choice,colors
    color_figure = colors[color_choice]
    

    clock = pygame.time.Clock()
    LMBpressed = False
    THICKNESS = 5
    currX = currY = prevX = prevY = 0
    running = True

    def calculate_circle(x1, y1, x2, y2):
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        r = int(math.hypot(x2 - x1, y2 - y1) / 2)
        return cx, cy, r

    while running:
        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: choice = 1; running = False
                if event.key == pygame.K_2: choice = 2; running = False
                if event.key == pygame.K_3: choice = 3; running = False
                if event.key == pygame.K_4: choice = 4; running = False
                if event.key == pygame.K_EQUALS: THICKNESS += 1
                if event.key == pygame.K_MINUS: THICKNESS = max(1, THICKNESS - 1)
                if event.key == pygame.K_RIGHT: color_choice+=1
                if event.key == pygame.K_LEFT: color_choice-=1

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                LMBpressed = True
                prevX, prevY = event.pos

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                LMBpressed = False
                currX, currY = event.pos
                cx, cy, r = calculate_circle(prevX, prevY, currX, currY)
                pygame.draw.circle(glv_layer, color_figure, (cx, cy), r, THICKNESS)

        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        color_figure = colors[color_choice]

        if LMBpressed:
            currX, currY = pygame.mouse.get_pos()
            cx, cy, r = calculate_circle(prevX, prevY, currX, currY)
            screen.blit(glv_layer, (0, 0))
            pygame.draw.circle(screen, color_figure, (cx, cy), r, THICKNESS)
        else:
            screen.blit(glv_layer, (0, 0))

        pygame.display.flip()
        clock.tick(60)

def pen():
    global choice, run, glv_layer, color_choice, colors
    color_figure = colors[color_choice]
    
    clock = pygame.time.Clock()
    drawing = False
    THICKNESS = 5
    prev_pos = None
    running = True

    while running:
        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: choice = 1; running = False
                if event.key == pygame.K_2: choice = 2; running = False
                if event.key == pygame.K_3: choice = 3; running = False
                if event.key == pygame.K_4: choice = 4; running = False
                if event.key == pygame.K_EQUALS: THICKNESS += 1
                if event.key == pygame.K_MINUS: THICKNESS = max(1, THICKNESS - 1)
                if event.key == pygame.K_RIGHT: color_choice += 1
                if event.key == pygame.K_LEFT: color_choice -= 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
                prev_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False
                prev_pos = None


        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4

        color_figure = colors[color_choice]

        if drawing:
            curr_pos = pygame.mouse.get_pos()
            if prev_pos:
                pygame.draw.line(glv_layer, color_figure, prev_pos, curr_pos, THICKNESS)
            prev_pos = curr_pos

        screen.blit(glv_layer, (0, 0))
        pygame.display.flip()
        clock.tick(60)

def eraser():
    global choice, run, glv_layer
    

    clock = pygame.time.Clock()
    LMBpressed = False
    ERASER_SIZE = 50
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: choice = 1; running = False
                if event.key == pygame.K_2: choice = 2; running = False
                if event.key == pygame.K_3: choice = 3; running = False
                if event.key == pygame.K_4: choice = 4; running = False
                if event.key == pygame.K_EQUALS: ERASER_SIZE += 5
                if event.key == pygame.K_MINUS: ERASER_SIZE = max(5, ERASER_SIZE - 5)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                LMBpressed = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                LMBpressed = False

        if LMBpressed:
            x, y = pygame.mouse.get_pos()
            pygame.draw.circle(glv_layer, color.colorBLACK, (x, y), ERASER_SIZE)

        screen.blit(glv_layer, (0, 0))
        pygame.display.flip()
        clock.tick(60)



while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: choice = 1
            if event.key == pygame.K_2: choice = 2
            if event.key == pygame.K_3: choice = 3
            if event.key == pygame.K_4: choice = 4
    
    if choice == 1:
        rect()
    elif choice == 2:
        circle()
    elif choice == 3:
        pen()
    elif choice == 4:
        eraser()

    if color_choice>4:
        color_choice = 0
    elif color_choice < 0:
        color_choice = 4

    
    color_figure = colors[color_choice]
    

pygame.quit()
