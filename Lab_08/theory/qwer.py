import pygame
import sys

pygame.init()

# Экран параметрлері
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Ойын циклы
while True:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  

    # Экранды тазалау (фонды қара түспен бояу)
    DISPLAYSURF.fill((255, 255, 255))

    pygame.display.update()
