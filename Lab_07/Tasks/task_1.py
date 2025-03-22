import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800,600))

stop_game = False
clock = pygame.time.Clock()

miki_clock = pygame.image.load("../images/clock.png")
min_hand = pygame.image.load("../images/min_hand.png")
sec_hand = pygame.image.load("../images/sec_hand.png")

angle_sec = 0
angle_min = 0

clock_rect = miki_clock.get_rect(center=(400, 300))



start_time = time.time()

while not stop_game:
    screen.fill((255, 255, 255)) 
    screen.blit(miki_clock, clock_rect.topleft) 
    
    
    elapsed_time = time.time() - start_time
    seconds = int(elapsed_time % 60)
    minutes = int((elapsed_time // 60) % 60)

    angle_sec = -seconds * 6  
    angle_min = -minutes * 6 


    rotated_image = pygame.transform.rotate(sec_hand, angle_sec) 
    new_rect = rotated_image.get_rect(center=(400,300))  
    screen.blit(rotated_image, new_rect.topleft) 

    rotated_image = pygame.transform.rotate(min_hand, angle_min) 
    new_rect = rotated_image.get_rect(center=(400,300))  
    screen.blit(rotated_image, new_rect.topleft) 

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game = True
            pygame.quit()

    pygame.display.flip()
    clock.tick(60)