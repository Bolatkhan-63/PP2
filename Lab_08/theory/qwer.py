import pygame
import sys

pygame.init()

# Экран параметрлері
screen = pygame.display.set_mode((800, 600))

# Екі бөлік
canvas1 = pygame.Surface((400, 600))  # Сол жақ "экран"
canvas2 = pygame.Surface((400, 600))  # Оң жақ "экран"

# Бірдей фреймде екеуіне бөлек сурет салу
canvas1.fill((255, 255, 255))  # Ақ
canvas2.fill((220, 220, 220))  # Ашық сұр

# Бас терезеге екеуін blit ету:
screen.blit(canvas1, (0, 0))
screen.blit(canvas2, (400, 0))

# Ойын циклы
while True:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  

    # Экранды тазалау (фонды қара түспен бояу)
    
    pygame.display.update()
