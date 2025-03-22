import pygame
import pygame.display

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,700))

stop_game = False

musics = [
    "../music/task_2_musics/music_1.mp3",
    "../music/task_2_musics/music_2.mp3",
    "../music/task_2_musics/music_3.mp3",
    "../music/task_2_musics/music_4.mp3"
    ]

fotos = [
    "../images/raim.png",
    "../images/sadr.png",
    "../images/kanat.png",
    "../images/zat.png",
    "../images/red_str.png",
    "../images/str.png",
    "../images/str2.png",
    "../images/pause.jpg",
    "../images/start.jpg",
    "../images/start.jpg"
]

index_music = 0
pause = True

corr_red_str_x = 850
corr_red_str_y = 0
index_pause = 9

def play_music():
    pygame.mixer.music.load(musics[index_music])
    pygame.mixer.music.play()



while not stop_game:
    screen.fill((0, 0, 0))

    screen.blit(pygame.image.load(fotos[0]),(100,0))
    screen.blit(pygame.image.load(fotos[1]),(100,125))
    screen.blit(pygame.image.load(fotos[2]),(100,260))
    screen.blit(pygame.image.load(fotos[3]),(100,380))

    screen.blit(pygame.image.load(fotos[4]),(corr_red_str_x,corr_red_str_y))
    screen.blit(pygame.image.load(fotos[6]),(50,500))
    screen.blit(pygame.image.load(fotos[5]),(500,500))
    screen.blit(pygame.image.load(fotos[index_pause]),(250,500))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:  # Ойнату/Пауза
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    pause = True
                    index_pause+=1
                else:
                    if pause:  
                        pygame.mixer.music.unpause()
                        pause = False
                        index_pause-=1
                    else:  
                        play_music()
                        corr_red_str_x-=300
                        index_pause-=1


            if event.key == pygame.K_RIGHT:
                index_music = (index_music + 1) % len(musics)
                if corr_red_str_y<389:
                    corr_red_str_y+= 130
                else:
                    corr_red_str_y=0
                play_music()

            if event.key == pygame.K_LEFT:
                index_music = (index_music - 1) % len(musics)
                if corr_red_str_y<1:
                    corr_red_str_y=390
                else:
                    corr_red_str_y-=130
                play_music()

    pygame.display.flip()

    
    
