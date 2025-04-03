#Imports
import pygame
import color
import random,time


pygame.init()

#Informations 
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((960, 660))
CELL = 30
Game_Over = False
LEVEL = 1
SCORE = 0
Next_level = 5
len_snake = 0

font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font.render("Game Over", True,color.colorGREEN)

apple_image = pygame.image.load("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\images/apple.png").convert_alpha()
apple_image = pygame.transform.scale(apple_image,(30,30))

game_over_sound = pygame.mixer.Sound("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\sounds\sound2.mp3")



#Draw rects
def draw_wall():
    for i in range(32):
        pygame.draw.rect(screen, color.colorBLUE, ( 0, i* CELL, CELL, CELL))
        pygame.draw.rect(screen, color.colorBLUE, ( 21 * CELL, i* CELL, CELL, CELL))
    for i in range(1,21):
        pygame.draw.rect(screen, color.colorBLUE, (i* CELL, 0, CELL, CELL))
        pygame.draw.rect(screen, color.colorBLUE, (i* CELL, 21 * CELL, CELL, CELL))

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, color.colorGRAY, ((i+1) * CELL, (j+1) * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [color.colorWHITE, color.colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], ((i+1) * CELL, (j+1) * CELL, CELL, CELL))


#Class point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

#Class Food
class Food:
    def __init__(self):
        self.pos = Point(9, 9)# Default food position

    #Draw food
    def draw(self):
        global apple_image
        screen.blit(apple_image, (self.pos.x * CELL, self.pos.y * CELL))

    # Generate next food
    def generate_random_pos(self,snake_body):
        while True:
            x = random.randint(1, WIDTH // CELL) 
            y = random.randint(1, HEIGHT // CELL) 
            new_Pos = Point(x,y)
            true_1 = True
              
            for i in range(len_snake):
                if new_Pos.x == snake_body[i].x and new_Pos.y == snake_body[i].y:
                    true_1 = False

            if true_1 :
                self.pos = new_Pos
                break


# Class snake
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]# Default snake
        self.dx = 1
        self.dy = 0

    #snake moves
    def move(self):
        global Game_Over
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > WIDTH // CELL:
            Game_Over = True
        # checks the left border
        if self.body[0].x < 1:
            Game_Over = True
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL:
            Game_Over = True
        # checks the top border
        if self.body[0].y < 1:
            Game_Over = True

    #Snake 
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, color.colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, color.colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

#Checking
    def check_collision(self, food, snake_body):
        global SCORE
        global Next_level
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            SCORE += 1
            Next_level -= 1
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(snake_body)




FPS = 5
clock = pygame.time.Clock()

#Objects
food = Food()
snake = Snake()
food.generate_random_pos(snake.body)


#Loop for game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# For quit the game
            running = False
        if event.type == pygame.KEYDOWN:# For moving snake
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1; snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1; snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0; snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0; snake.dy = -1


    screen.fill(color.colorBLACK)

    draw_grid_chess()# Draw rects in the game
    draw_wall()

    #Draw texts
    screen.blit(font_small.render(f"Level: {LEVEL}",True,color.colorBLUE),(670,230))
    screen.blit(font_small.render(f"SCORE: {SCORE}",True,color.colorBLUE),(670,40))
    screen.blit(font_small.render(f"To next level: {Next_level}",True,color.colorBLUE),(670,260))

    len_snake = len(snake.body)
    # Functions for game
    snake.move()

    #Checking snake head
    head = snake.body[0]
    for segment in snake.body[1:]:
        if head.x == segment.x and head.y == segment.y:
            Game_Over = True

    snake.check_collision(food,snake.body)

    snake.draw()
    food.draw()

    #for next level
    if Next_level==0:
        LEVEL+=1
        FPS+=1
        Next_level=5

    #Code about game over
    if Game_Over:
        screen.fill(color.colorBLACK)
        screen.blit(game_over,(260,220))

        game_over_sound.play()
        time.sleep(1)
        screen.blit(font.render(f"Your score is: {SCORE}",True,color.colorGRAY),(190,290))
        pygame.display.update()
        time.sleep(4)
        running = False

        
    


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

