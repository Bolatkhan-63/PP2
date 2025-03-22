import pygame

#Base code for game
pygame.init()
screen = pygame.display.set_mode((1200,700))
QUIT = False

is_blue = True

x = 300
y = 300

clock = pygame.time.Clock()

while not QUIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_blue = not is_blue
    #Drawing Something
    # Add this somewhere after the event pumping and before the display.flip()
            #pygame.draw.rect(screen,(0,128,255),pygame.Rect(30,30,60,60))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    

    #Interactivity
    screen.fill((0, 0, 0))
    if is_blue:
        color = (0,128,255)
    else:
        color = (255, 100, 0)

    pygame.draw.rect(screen,color,pygame.Rect(x,y,130,140))
    

    pygame.display.flip()
    clock.tick(60)
