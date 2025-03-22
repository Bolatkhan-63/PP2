import pygame


pygame.init()
screen = pygame.display.set_mode((1000,700))

surface = pygame.Surface((100, 100))
image = pygame.image.load("../images/img1.jpeg")

stop = False
white = (255,255,255)
black = (0,0,0)

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    screen.fill(white)
    screen.blit(surface, (50, 50)) 
    screen.blit(image,(200,200)) 

    pygame.display.flip()