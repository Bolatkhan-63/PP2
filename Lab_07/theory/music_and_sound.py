import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800,400))
stop = False


# pygame.mixer.music.load('../music/music1.mp3')
# pygame.mixer.music.play()

# pygame.mixer.music.queue('../music/music2.mp3')

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('../music/music1.mp3')
pygame.mixer.music.play()


while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if event.type == SONG_END:
            print("The end of Music")
    

    pygame.display.flip()     