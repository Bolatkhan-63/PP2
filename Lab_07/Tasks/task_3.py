import pygame

#Base code for game
pygame.init()
screen = pygame.display.set_mode((1000,600))
QUIT = False

x=500
y=300

clock = pygame.time.Clock()

while not QUIT:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x>50:
                x-=20
            elif event.key == pygame.K_RIGHT and x<950:
                x+=20
            elif event.key == pygame.K_UP and y>50:
                y-=20
            elif event.key == pygame.K_DOWN and y<550:
                y+=20

    pygame.draw.circle(screen, (255,0,0), (x,y),25)
    

    pygame.display.flip()
    clock.tick(60)
