import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_07\music/task_2_musics/music_4.mp3")
pygame.mixer.music.play(-1)

HEIGHT = 500
WIDTH = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))

shrift = pygame.font.SysFont("comicsansms", 72)

one_words = [
    "Game","Next","Lets go","Friend"
]
second_words = [
    "qwerty","name","apple","orange"
]
index_one = 0
index_two = 0


stop_game = False

while not stop_game:
    if index_one>3:
        index_one = 0
    elif index_two>3:
        index_two = 0

    one_w = shrift.render(one_words[index_one],True,(255,255,255))
    two_w = shrift.render(second_words[index_two],True,(255,255,255))

    pygame.draw.rect(screen, (100,255,244), pygame.Rect(380, 140, 280, 150)) 
    pygame.draw.rect(screen, (100,255,244), pygame.Rect(90, 140, 280, 150)) 


    screen.blit(one_w,(100,150))
    
    screen.blit(two_w,(400,150))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                index_two+=1
            elif event.key == pygame.K_2:
                index_one+=1

    if index_one>3:
        index_one = 0
    elif index_two>3:
        index_two = 0

    pygame.display.flip()