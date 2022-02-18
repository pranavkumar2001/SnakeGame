# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:10:43 2021

@author: kumar
"""

import pygame
import random
import os
import sys

pygame.init()
from pygame import mixer


#colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)

#Game display size
screen_width=800
screen_height=600
fps=30

gameWindow=pygame.display.set_mode((screen_width,screen_height))

bgimg=pygame.image.load("img3.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
icon=pygame.image.load("icon1.png")


#Game Title
pygame.display.set_caption("Pranav's Snake game")
pygame.display.set_icon(icon)
pygame.display.update()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)

def text_screen(text,colour,x,y):
    screen_text=font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,colour,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,colour,[x,y,snake_size,snake_size])
        
def plot_food(x,y):
    food=pygame.image.load("apple.png")
    food=pygame.transform.scale(food,(24,24)).convert_alpha()
    gameWindow.blit(food,(x,y))
        

def welcome():
    game_exit=False
    while not game_exit:
        gameWindow.fill(white)
        gameWindow.blit(bgimg,(0,0))
        text_screen("Welcome to Snake game",red,100,250)
        text_screen("Designed by Pranav",red,100,300)
        text_screen("Press Enter to begin",red,100,350)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()
                    

        pygame.display.update()
        clock.tick(fps)

#Game loop
def gameloop():
    #Game variables
    game_exit=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=15
    velocity_x=0
    velocity_y=0
    score=0
    init_velocity=4
    fps=30
    food_x=random.randint(100,screen_width/2)
    food_y=random.randint(100,screen_height/2)
    snk_list=[]
    snk_len=1
    pygame.mixer.music.load('song1.mp3')
    pygame.mixer.music.play()
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore=f.read()
    while not game_exit:
         if game_over:
             with open("highscore.txt","w") as f:
                 f.write(str(highscore))
             gameWindow.fill(white)
             gameWindow.blit(bgimg,(0,0))

             text_screen("Game over!Press Enter to continue",red,100,250)
             for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_RETURN:
                         gameloop()
         else:
             for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                 if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x-=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                       velocity_y-=init_velocity
                       velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
             if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                bell=mixer.Sound("bell.mp3")
                bell.play()
                score+=10
                snk_len+=5
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                if score>int(highscore):
                    highscore=score
             snake_x+=velocity_x
             snake_y+=velocity_y


             gameWindow.fill(red)
             gameWindow.blit(bgimg,(0,0))
             text_screen("Score:"+str(score)+"  Highscore:"+str(highscore),white,10,10)
             #pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
             plot_food(food_x,food_y)
             head=[]
             head.append(snake_x)
             head.append(snake_y)
             snk_list.append(head)

             if len(snk_list)>snk_len:
                 del snk_list[0]

             if head in snk_list[:-1]:
                  game_over=True
                  pygame.mixer.music.load('song2.mp3')
                  pygame.mixer.music.play()

             if snake_x>screen_width or snake_x<0 or snake_y>screen_height or snake_y<0:
                game_over=True
                pygame.mixer.music.load('song2.mp3')
                pygame.mixer.music.play()
             plot_snake(gameWindow,green,snk_list,snake_size)
         pygame.display.update()
         clock.tick(fps)

welcome()
pygame.quit()
