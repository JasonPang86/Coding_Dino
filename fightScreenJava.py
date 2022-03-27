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

storage = [ ["In the Java langauge what is the correct print statment?","Option 1:printf('message')", "Option 2:cout<<'message';", "Option 3:print('message')", "Option 4:System.out.println('message')", "4"],
            ["What is the correct answer for this binary addition 11001 + 1001?","Option 1: 10001", "Option 2: 11000", "Option 3: 1111", "Option 4: none of the above ", "1"],
            ["When we want intialize a String which of the following is correct?","Option 1: name = String", "Option 2: 3 = String", "Option 3: String name = 'name'", "Option 4: String = string string ", "3"],
            ["Can Java be used as a language in objected oriented programming?","Option 1: Maybe?", "Option 2: Yes!", "Option 3: Only in Certain Scenrios", "Option 4: No! ", "2"],
            ["When we want to comment out something in Java what do we use?","Option 1: ##", "Option 2: ^^", "Option 3: /* */", "Option 4: Java is the only language we can't comment anything ", "3"],
            ["In Java what does it mean when we talk about scope?","Option 1: We are talking about Snipers!", "Option 2: when variables can be changed within a region ", "Option 3: Doesn't mean anything ","Option 4: When variables are accessed inside the region they're created in" , "4"],
            ["What does this logical statement mean x <= 8 && x < 10?","Option 1: x is less then and equal to 8 and less then 10", "Option 2: x is less then or equal to 8 and less then 10", "Option 3: x is equal to 8 or less then 10  ","Option 4:  x is greater then 8 and less then 10 " , "2"],
            ["Which of the following can be used as a package?","Option 1: package programming.hackathon ", "Option 2: package hackathon.programming ", "Option 3: package coding.is.cool","Option 4:  all of them!" , "4"]
                ]

def fightJava(id):
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
                        playerHealth = 0 ;
                    
                if event.key == pygame.K_ESCAPE:
                    enemyHealth = 0

        pygame.display.update()

