import pygame

red = (255,0,0)
green = (0,255,0)
blue= (0,0,255)

colors = [blue,green,red]

repeat = True
i = 0

screen = pygame.display.set_mode((2000,800))
fps = pygame.time.Clock()
while repeat:
    color = colors[i%3]

    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            repeat = False
        
    if i>100:
        i=0
    i+=1

    
    pygame.display.flip()
    fps.tick(10)

