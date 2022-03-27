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

storage = [ ["In the python langauge what is the correct print statment?","Option 1: printf('message')","Option 2: cout<<'message';", "Option 3: print('message')", "Option 4:System.out.println('message')","3"], 
            ["What is the correct answer for this binary addition 1001 + 1001?", "Option 1:10011001", "Option 2:1111", "Option 3:10101", "Option 4:none of the above", "4"], 
            ["What is the correct base 2 conversion for this binary number 110100101?","Option 1:10011001","Option 2:1111","Option 3:10101", "Option 4:none of the above", "2"],    
            ["What are the 4 elements of OOP?" , "Option 1: Inheritance, Encapsulation, Polymorphism and Abstraction","Option 2: Classes, Encapsulation, Polymorphism and Abstraction","Option 3: Classes and Objects, Inheritance, Encapsulation, Polymorphism", "Option 4:none of the above", "1"],    
            ["Which is the correct way to use if,else and elif in python?","Option 1: if... elif...else","Option 2: if...else...elif","Option 3: else...elif...if..","Option 4: elif...if...else", "1"],    
            ["Which is the correct syntax to use for a for loop in python?","Option 1: for i in range [1,10]","Option 2: for i in range {1,10}","Option 3: range i in for (1,10)","Option 4: for i in range (1,10)","4"],
            ["For this while loop: i = 0, while i < 6: print(i) i += 2 what is the correct output?","Option 1: [1,2,3,4,5]","Option 2: [0,2,4]","Option 3: [2,4,6]","Option 4: [0,2,4,6]","2"],    
            ["When we want to intialize and array in python which of the following is the correct way to do it?","Option 1:  array = ()","Option 2: [] = array","Option 3:  array = '{x'}","Option 4: array = []","4"] ]

def fight(id):
    run = True
    enemyHealth = 2
    playerHealth = 100
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
        answer = storage[i][5]


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
                        enemyHealth -= 1
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1
                if event.key == pygame.K_2:
                    if answer == "2":
                        enemyHealth -= 1
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1 
                if event.key == pygame.K_3:
                    if answer == "3":
                        enemyHealth -= 1
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1
                if event.key == pygame.K_4:
                    if answer == "4":
                        enemyHealth -= 1
                        i = randint(0,len(storage)-1)
                    else:
                        playerHealth -= 1

        pygame.display.update()

