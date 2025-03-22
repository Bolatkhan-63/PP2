import pygame

pygame.init()
screen = pygame.display.set_mode((1200,600))

stop = True

while stop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = False
            pygame.quit()

    #Төртбұрыш
    pygame.draw.rect(screen, (100,255,244), pygame.Rect(500, 200, 100, 150),40) #pygame.draw.rect(screen, color, (x, y, width, height), thickness)

    #Үшбұрыш
    pygame.draw.polygon(screen, (100,255,244), [(50,50), (100,70), (70, 120)])#pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2), (x3, y3)], thickness)

    #Шеңбер
    pygame.draw.circle(screen,  (100,255,244), (900,300),50) #pygame.draw.circle(screen, color, (x, y), radius, thickness)

    #Бір сызық
    pygame.draw.line(screen, (100,150,200), (300,500), (500, 500),50)#pygame.draw.line(screen, color, (x1, y1), (x2, y2), thickness)
    #Көп сызық салу үшін
    pygame.draw.lines(screen, (100,150,200),True, [(450,200), (150,530), (900, 500)])#pygame.draw.lines(screen, color, closed, [(x1, y1), (x2, y2), (x3, y3)], thickness)



    pygame.display.flip()