#Imports
import pygame,sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

#Colors
BLUE = (0,0,255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Informations
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0
speed_coin = 4

#Information about text
font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font.render("Game Over", True,BLACK)

#image in background
background = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/doroga.jpg")

#Display settings
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


#Class Enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/red_car.png")#Create enemy image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)# Enemy's move
        if (self.rect.top > 600): 
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Class Coin
class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08/images/coin.png").convert_alpha()#Coin's image
        self.image = pygame.transform.scale(self.image,(60,60)) #Transform coin's image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        global COIN
        self.rect.move_ip(0,speed_coin)# Coin's move
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

#Class player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/blue_car.png")#Create player image
        self.image = pygame.transform.scale(self.image,(78.3,112.4))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)# First position is palyer

    #Player's moves
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Objects
P1 = Player()
E1 = Enemy()
coin_1 = coin()

# Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group()
coins_group.add(coin_1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin_1)


# Code for move every second
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)




while True:
    # For quit button and move every second
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # First display settings
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0,0))
    
    # Move every elements in game
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        
    # Write numbers about score and coins
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    coins = font_small.render(str(COIN), True, BLACK)
    DISPLAYSURF.blit(coins, (380,10))


    # Loop for game over
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\sounds\sound.mp3').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))

        result = font.render(f"Score: {SCORE}",True,BLUE)
        DISPLAYSURF.blit(result,(60,300))

        result = font.render(f"Coins: {COIN}",True,BLUE)
        DISPLAYSURF.blit(result,(60,360))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()       


    #loop for collect coin
    if pygame.sprite.spritecollideany(P1, coins_group): 
        COIN+=1
        coin_1.rect.top = 0
        coin_1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
         

    pygame.display.flip()
    FramePerSec.tick(FPS)