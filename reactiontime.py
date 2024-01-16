import pygame
import time
import random
import sys

pygame.init()
#global variables
game_is_running = True
#screen properties
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("My First Game using PyGame: Reaction Time")
#font
font = pygame.font.SysFont("Arial",30)

#start
start = font.render("START", True ,"black")
start_rect = start.get_rect(center=(300,300))
#title
title = font.render("How fast is your reaction time?", True ,"black")
title_rect = title.get_rect(center=(300,100))
#wait
wait = font.render("GET READY...", True ,"white")
wait_rect = wait.get_rect(center=(300,300))
#click
click = font.render("CLICK!", True ,"black")
click_rect = click.get_rect(center=(300,300))
#result
result = font.render("Score: 2000 ms", True ,"black")
result_rect = result.get_rect(center=(300,300))
game_state = "Start"
start_time, click_time = 0 , 0
#start the program
#wait before
#click
#time
#main game loop
while game_is_running == True:
    #to exit pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "Start":
                game_state = "Wait"
            elif game_state == "Wait":
                game_state = "Click"
            elif game_state == "Click":
                end_time = time.time()
                game_state = "Result"
            elif game_state == "Result":
                game_state = "Start"
    screen.fill("blue")
    if game_state == "Start":
        screen.blit(title,title_rect)
        screen.blit(start,start_rect)
        pygame.draw.circle(screen,(0,0,0),(300,300),75, width =5)
    elif game_state == "Wait":
        screen.fill("black")
        screen.blit(wait,wait_rect)
        pygame.display.update()
        delay_time = random.uniform(2,12)
        time.sleep(delay_time)
        game_state = "Click"
        start_time = time.time()
    elif game_state == "Click":
        screen.fill("red")
        screen.blit(click,click_rect)
    elif game_state == "Result":
        reaction_time = end_time - start_time
        score = font.render(f'Reaction Time: {round(reaction_time, 3)} ms', True ,"black")
        score_rect = score.get_rect(center=(300,300))
        screen.blit(score,score_rect)
        
    pygame.display.update()