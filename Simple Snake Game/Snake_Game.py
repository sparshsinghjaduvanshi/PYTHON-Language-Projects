import pygame
import random
import os
pygame.init()

#Colors
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#Defining width and height of the window
screen_width = 900
screen_height = 600

#setting the window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Setting the caption of the window
pygame.display.set_caption("SnakeWithSparsh")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,(x,y))
    
    
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, black, (x, y, snake_size, snake_size))   
    

def Welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcomes to Snakes!",black, 260, 250)
        text_screen("Press Spacebar to Play!",black, 230, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game_Loop()
                
        pygame.display.update()
        clock.tick(60)
        
#Game Loop
def Game_Loop():
    
    #Game Specific Variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    score = 0
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    fps = 30

    snake_list = []
    snake_length = 1
    food_x = random.randint(20,screen_width//2)
    food_y = random.randint(20,screen_height//2)

    #check if the highscore file exists
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highScore = f.read()
        
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highScore))
                
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter to Start Again.", red, 100, 250)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()   
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity 
                        velocity_y = 0 
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity  
                        velocity_y = 0 
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0 
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0 
                        
            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score+=10
                food_x = random.randint(20,screen_width//2)
                food_y = random.randint(20,screen_height//2)
                snake_length += 5
                if score > int(highScore):
                    highScore = score
            
            gameWindow.fill(white)
            text_screen("Score : "+str(score) + "  High Score : "+str(highScore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, (food_x, food_y, snake_size, snake_size))     
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0] 
                
            if head in snake_list[:-1]:
                game_over = True
                
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                print("Game over")
                
            # pygame.draw.rect(gameWindow, black, (snake_x, snake_y, snake_size, snake_size))   
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
        

    pygame.quit()
    quit()
    
# Game_Loop()
Welcome()