#Imports
import pygame
import color
import random,time


pygame.init()

#Informations 
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((900, 600))
CELL = 30
Game_Over = False
LEVEL = 1
SCORE = 0
Next_level = 5

font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font.render("Game Over", True,color.colorGREEN)



#Paint rects
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, color.colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [color.colorWHITE, color.colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


#Class point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

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
        if self.body[0].x > WIDTH // CELL - 1:
            Game_Over = True
        # checks the left border
        if self.body[0].x < 0:
            Game_Over = True
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            Game_Over = True
        # checks the top border
        if self.body[0].y < 0:
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

#Class Food
class Food:
    def __init__(self):
        self.pos = Point(9, 9)# Default food position

    #Draw food
    def draw(self):
        pygame.draw.rect(screen, color.colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    # Generate next food
    def generate_random_pos(self,snake_body):
        while True:
            x = random.randint(0, WIDTH // CELL - 1) 
            y = random.randint(0, HEIGHT // CELL - 1) 
            new_Pos = Point(x,y)
            if new_Pos not in snake_body:
                self.pos = new_Pos
                break




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
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    screen.fill(color.colorBLACK)

    draw_grid_chess()# Draw rects in the game

    #Draw texts
    screen.blit(font_small.render(f"Level: {LEVEL}",True,color.colorBLUE),(620,200))
    screen.blit(font_small.render(f"SCORE: {SCORE}",True,color.colorBLUE),(620,10))
    screen.blit(font_small.render(f"To next level: {Next_level}",True,color.colorBLUE),(620,230))


    # Functions for game
    snake.move()
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

        pygame.mixer.Sound("C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_08\sounds\sound2.mp3").play()
        time.sleep(1)
        screen.blit(font.render(f"Your score is: {SCORE}",True,color.colorGRAY),(190,290))
        pygame.display.update()
        time.sleep(4)
        running = False

    

        


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

