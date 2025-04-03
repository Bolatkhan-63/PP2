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

LEVEL = 1
next_level = 10
current_index = 0

coin_image = [
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin_2.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin_3.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin_4.png",
    "C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_09\images/coin_5.png"
]

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
        self.update_image()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    def update_image(self):
        global current_index
        current_index = random.randint(0, len(coin_image) - 1) #choose index coin's image
        random_path = coin_image[current_index]
        self.image = pygame.image.load(random_path).convert_alpha()#Coin's image
        self.image = pygame.transform.scale(self.image, (60, 60))#Transform coin's image

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
        
    #Calculate next level
    if next_level <= 0:
        SPEED += 2
        LEVEL += 1
        next_level = 10


    # Write numbers about score and coins
    scores = font_small.render(f"Score: {str(SCORE)}", True, WHITE)
    DISPLAYSURF.blit(scores, (10,10))

    coins = font_small.render(f"Coin: {str(COIN)}", True, WHITE)
    DISPLAYSURF.blit(coins, (300,10))

    level = font_small.render(f"Level: {str(LEVEL)}", True, WHITE)
    DISPLAYSURF.blit(level, (300,30))


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


    #loop for collect coin and calculate next level
    if pygame.sprite.spritecollideany(P1, coins_group):

        #Calculate coin 
        if current_index<=4 and current_index>=0:
            COIN += 1
        elif current_index == 5:
            COIN += 2
        elif current_index == 6:
            COIN += 3
        elif current_index == 7:
            COIN += 4
        elif current_index == 8:
            COIN += 5

        #Calculate next level
        if current_index<=4 and current_index>=0:
            next_level -= 1
        elif current_index == 5:
            next_level -= 2
        elif current_index == 6:
            next_level -= 3
        elif current_index == 7:
            next_level -= 4
        elif current_index == 8:
            next_level -= 5
        coin_1.update_image()
        
        #Position next coin
        coin_1.rect.top = 0
        coin_1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
         

    pygame.display.flip()
    FramePerSec.tick(FPS)