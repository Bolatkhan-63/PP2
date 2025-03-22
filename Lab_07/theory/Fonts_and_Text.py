import pygame

pygame.init()
screen = pygame.display.set_mode((1200,600))

stop_game = False
clock = pygame.time.Clock()

shrift = pygame.font.SysFont("comicsansms", 72)#pygame.font.SysFont(name, size, bold=False, italic=False)

text_1 = shrift.render("Hello World",False,(0, 128, 0)) #text_surface = font.render(text, antialias, color, background=None)
text_in_screen = False

while not stop_game:
    screen.fill((0,0,0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                text_in_screen = not text_in_screen
        

    if text_in_screen:
        screen.blit(text_1,(400,200))


    pygame.display.flip()
    clock.tick(60)