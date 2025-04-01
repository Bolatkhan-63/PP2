import pygame
import math,color

pygame.init()

WIDTH = 800
HEIGHT = 700

colors = [color.colorBLUE,color.colorGREEN,color.colorRED,color.colorWHITE,color.colorYELLOW]


choice = 1
run = True

color_choice = 0
silver_pos = 495


screen = pygame.display.set_mode((WIDTH, HEIGHT))
glv_layer = pygame.Surface((WIDTH, 540))
glv_2_layer = pygame.Surface((WIDTH, 310))

glv_layer.fill(color.colorBLACK)
glv_2_layer.fill(color.colorBLACK)

rect_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/rect.png")
rect_image = pygame.transform.scale(rect_image,(100,100))
circle_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/circle.png")
circle_image = pygame.transform.scale(circle_image,(100,100))
pen_image= pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/pen.png")
pen_image = pygame.transform.scale(pen_image,(100,100))
eraser_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/eraser.png")
eraser_image = pygame.transform.scale(eraser_image,(100,100))

blue_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/blue.png")
blue_image = pygame.transform.scale(blue_image,(50,50))
green_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/green.png")
green_image = pygame.transform.scale(green_image,(50,50))
red_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/red.png")
red_image = pygame.transform.scale(red_image,(50,50))
white_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/white.png")
white_image = pygame.transform.scale(white_image,(50,50))
yellow_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/yellow.png")
yellow_image = pygame.transform.scale(yellow_image,(50,50))
silver_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/silver.png")
silver_image = pygame.transform.scale(silver_image,(60,60))

one_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/one.png")
one_image = pygame.transform.scale(one_image,(20,30))
two_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/two.png")
two_image = pygame.transform.scale(two_image,(20,30))
three_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/three.png")
three_image = pygame.transform.scale(three_image,(20,30))
four_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/four.png")
four_image = pygame.transform.scale(four_image,(20,30))

str_left = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/str2.png")
str_left = pygame.transform.scale(str_left,(70,40))
str_right = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/str.png")
str_right = pygame.transform.scale(str_right,(70,40))
plus_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/plus.png")
plus_image = pygame.transform.scale(plus_image,(30,30))
minus_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/minus.png")
minus_image = pygame.transform.scale(minus_image,(30,30))



def rect():
    global choice, run, glv_layer,color_choice,colors,silver_pos,glv_2_layer
    color_figure = colors[color_choice]
    

    
    clock = pygame.time.Clock()
    LMBpressed = False
    THICKNESS = 5
    currX = currY = prevX = prevY = 0
    running = True

    def calculate_rect(x1, y1, x2, y2):
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

    while running:
        
        screen.blit(glv_2_layer,(0,540))

        pygame.draw.line(glv_2_layer, color.colorWHITE, (0,0), (800, 0), 10)

        glv_2_layer.blit(silver_image,(silver_pos,30))
        glv_2_layer.blit(blue_image,(500,35))
        glv_2_layer.blit(green_image,(560,35))
        glv_2_layer.blit(red_image,(620,35))
        glv_2_layer.blit(white_image,(680,35))
        glv_2_layer.blit(yellow_image,(740,35))

        glv_2_layer.blit(rect_image,(50,10))
        glv_2_layer.blit(circle_image,(160,10))
        glv_2_layer.blit(pen_image,(270,10))
        glv_2_layer.blit(eraser_image,(380,10))
        
        glv_2_layer.blit(one_image,(90,120))
        glv_2_layer.blit(two_image,(200,120))
        glv_2_layer.blit(three_image,(310,120))
        glv_2_layer.blit(four_image,(420,120))

        glv_2_layer.blit(str_left,(550,100))
        glv_2_layer.blit(str_right,(670,100))
        glv_2_layer.blit(plus_image,(10,30))
        glv_2_layer.blit(minus_image,(10,70))
        
        


        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735

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
                if event.key == pygame.K_RIGHT: color_choice+=1; silver_pos+=60; glv_2_layer.fill(color.colorBLACK)
                if event.key == pygame.K_LEFT: color_choice-=1; silver_pos-=60; glv_2_layer.fill(color.colorBLACK)

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
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735

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
    global choice, run, glv_layer,color_choice,colors,silver_pos,glv_2_layer
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

        screen.blit(glv_2_layer,(0,540))

        pygame.draw.line(glv_2_layer, color.colorWHITE, (0,0), (800, 0), 10)

        glv_2_layer.blit(silver_image,(silver_pos,30))
        glv_2_layer.blit(blue_image,(500,35))
        glv_2_layer.blit(green_image,(560,35))
        glv_2_layer.blit(red_image,(620,35))
        glv_2_layer.blit(white_image,(680,35))
        glv_2_layer.blit(yellow_image,(740,35))

        glv_2_layer.blit(rect_image,(50,10))
        glv_2_layer.blit(circle_image,(160,10))
        glv_2_layer.blit(pen_image,(270,10))
        glv_2_layer.blit(eraser_image,(380,10))
        
        glv_2_layer.blit(one_image,(90,120))
        glv_2_layer.blit(two_image,(200,120))
        glv_2_layer.blit(three_image,(310,120))
        glv_2_layer.blit(four_image,(420,120))

        glv_2_layer.blit(str_left,(550,100))
        glv_2_layer.blit(str_right,(670,100))
        glv_2_layer.blit(plus_image,(10,30))
        glv_2_layer.blit(minus_image,(10,70))
        
        


        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735
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
                if event.key == pygame.K_RIGHT: color_choice+=1; silver_pos+=60; glv_2_layer.fill(color.colorBLACK)
                if event.key == pygame.K_LEFT: color_choice-=1; silver_pos-=60; glv_2_layer.fill(color.colorBLACK)

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
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735

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
    global choice, run, glv_layer,color_choice,colors,silver_pos,glv_2_layer
    color_figure = colors[color_choice]
    
    clock = pygame.time.Clock()
    drawing = False
    THICKNESS = 5
    prev_pos = None
    running = True

    while running:

        screen.blit(glv_2_layer,(0,540))

        pygame.draw.line(glv_2_layer, color.colorWHITE, (0,0), (800, 0), 10)

        glv_2_layer.blit(silver_image,(silver_pos,30))
        glv_2_layer.blit(blue_image,(500,35))
        glv_2_layer.blit(green_image,(560,35))
        glv_2_layer.blit(red_image,(620,35))
        glv_2_layer.blit(white_image,(680,35))
        glv_2_layer.blit(yellow_image,(740,35))

        glv_2_layer.blit(rect_image,(50,10))
        glv_2_layer.blit(circle_image,(160,10))
        glv_2_layer.blit(pen_image,(270,10))
        glv_2_layer.blit(eraser_image,(380,10))
        
        glv_2_layer.blit(one_image,(90,120))
        glv_2_layer.blit(two_image,(200,120))
        glv_2_layer.blit(three_image,(310,120))
        glv_2_layer.blit(four_image,(420,120))

        glv_2_layer.blit(str_left,(550,100))
        glv_2_layer.blit(str_right,(670,100))
        glv_2_layer.blit(plus_image,(10,30))
        glv_2_layer.blit(minus_image,(10,70))
        
        
        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735

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
                if event.key == pygame.K_RIGHT: color_choice+=1; silver_pos+=60; glv_2_layer.fill(color.colorBLACK)
                if event.key == pygame.K_LEFT: color_choice-=1; silver_pos-=60; glv_2_layer.fill(color.colorBLACK)

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
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735

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
    global choice, run, glv_layer,color_choice,colors,silver_pos,glv_2_layer
    

    clock = pygame.time.Clock()
    LMBpressed = False
    ERASER_SIZE = 50
    running = True

    while running:

        screen.blit(glv_2_layer,(0,540))

        pygame.draw.line(glv_2_layer, color.colorWHITE, (0,0), (800, 0), 10)

        glv_2_layer.blit(silver_image,(silver_pos,30))
        glv_2_layer.blit(blue_image,(500,35))
        glv_2_layer.blit(green_image,(560,35))
        glv_2_layer.blit(red_image,(620,35))
        glv_2_layer.blit(white_image,(680,35))
        glv_2_layer.blit(yellow_image,(740,35))

        glv_2_layer.blit(rect_image,(50,10))
        glv_2_layer.blit(circle_image,(160,10))
        glv_2_layer.blit(pen_image,(270,10))
        glv_2_layer.blit(eraser_image,(380,10))
        
        glv_2_layer.blit(one_image,(90,120))
        glv_2_layer.blit(two_image,(200,120))
        glv_2_layer.blit(three_image,(310,120))
        glv_2_layer.blit(four_image,(420,120))

        glv_2_layer.blit(str_left,(550,100))
        glv_2_layer.blit(str_right,(670,100))
        glv_2_layer.blit(plus_image,(10,30))
        glv_2_layer.blit(minus_image,(10,70))
        
        
        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735

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
                if event.key == pygame.K_RIGHT: color_choice+=1; silver_pos+=60; glv_2_layer.fill(color.colorBLACK)
                if event.key == pygame.K_LEFT: color_choice-=1; silver_pos-=60; glv_2_layer.fill(color.colorBLACK)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                LMBpressed = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                LMBpressed = False

        if color_choice>4:
            color_choice = 0
        elif color_choice < 0:
            color_choice = 4
        if silver_pos>735:
            silver_pos = 495
        elif silver_pos < 495:
            silver_pos = 735

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



    pygame.display.flip()



pygame.quit()
