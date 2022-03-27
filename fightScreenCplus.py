from random import randint
from turtle import clear
import pygame
import sys
import dino

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Define Font
font = pygame.font.SysFont('Times New Roman', 26)

#game window
bottom_panel = 150
screen_width = 900
screen_height = 350 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


#load images
#background image
background_img = pygame.image.load('Assets/Forest.png').convert_alpha()
#panel image
panel_img = pygame.image.load('Assets/panel.png').convert_alpha()


#function for drawing background
def draw_bg():
    screen.blit(background_img, (0, -425))


#function for drawing panel
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))


def Question1_Python():
    print("In the python langauge what is the correct print statment?")
    print("Option 1:printf('message')")
    print("Option 2:cout<<'message';")
    print("Option 3:print('message')")
    print("Option 4:System.out.println('message')")
    
    correct_answer = 3 


def addText(text,x,y):
    screen.blit(font.render(text, True, (0,0,0)), (x, y))

player = dino.Dinosaur(125, 275, 4, 'Assets\mort.png', 3)
Blue = dino.Dinosaur(775,250,8,'Assets\Gary.png',3)
Green = dino.Dinosaur(775,250,8,'Assets\Larry.png',3)
Yellow = dino.Dinosaur(775,250,10,'Assets\Berry.png',3)

storage = [ ["Which is the correct print statment for C?", "Option 1:printf('message')", "Option 2:cout<<'message';", "Option 3:print('message')", "Option 4:System.out.println('message')", "1"],
            ["What is the correct answer for this binary addition 00000 + 10001?", "Option 1: 1000100000","Option 2: 10101", "Option 3: 10001", "Option 4: 11111", "3"],
            ["What is the correct base 2 conversion of this number 111111?", "Option 1: 101", "Option 2: 63", "Option 3: 119", "Option 4: 1111", "2"],
            ["Is C be used as a language in objected oriented programming", "Option 1: Maybe?","Option 2: Yes!", "Option 3: Only in Certain Scenarios", "Option 4: No!", "4"],
            ["Which is the correct way to use an if else statment in C?","Option 1: if...else...elif", "Option 2: if...else...else", "Option 3: else if...if...else","Option 4: else...if...if","2"],
            ["Which of the following is needed at the top before coding in the language C?","Option 1: #include <stdio.h>", "Option 2: include <stdio.h>", "Option 3: #include <studio.h>", "Option 4: #include stdio.h", "1"],
            ["What is a pointer?", "Option 1: someone that points at someone", "Option 2: a variable that points at another variable", "Option 3: a variable that stores the address of another variable", "Option 4: this symbol (*) but doesn't have meaning", "3"],
            ["When performing function calls which one of the following is correct?", "Option 1: var(1) = int sum", "Option 2: int var = sum(1)", "Option 3: int var = sum 4", "Option 4: int var = sum(var2,var3)", "4"]    ]

def fightC(id):
    run = True
    enemyHealth = 2;
    playerHealth = 100;
    i = randint(1,5)
    while (enemyHealth != 0):

        clock.tick(fps)

        #draw background
        draw_bg()

        #draw panel
        draw_panel()

        #Draw text
        addText(storage[i][0],70,370)
        addText(storage[i][1],70,395)
        addText(storage[i][2],70,415)
        addText(storage[i][3],70,435)
        addText(storage[i][4],70,455)
        answer = storage[i][5];


        player.update_animation()
        player.draw()
        if id == "Blue":
            Blue.update_animation()
            Blue.draw2()
        if id == "Green":
            Green.update_animation()
            Green.draw2()
        if id == "Yellow":
            Yellow.update_animation()
            Yellow.draw2()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if answer == "1":
                        enemyHealth -= 1;
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1;
                if event.key == pygame.K_2:
                    if answer == "2":
                        enemyHealth -= 1;
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1 ;
                if event.key == pygame.K_3:
                    if answer == "3":
                        enemyHealth -= 1;
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1;
                if event.key == pygame.K_4:
                    if answer == "4":
                        enemyHealth -= 1;
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1 ;
                    
                if event.key == pygame.K_ESCAPE:
                    enemyHealth = 0

        pygame.display.update()

