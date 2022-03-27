from random import randint
from turtle import clear
import pygame
import sys
import dino

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Define Font
font = pygame.font.SysFont('Times New Roman', 15)

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
Maurice = dino.Dinosaur(250,275,4,'Assets\Berry.png', 3)



def speak():
    run = True
    while run:

        clock.tick(fps)

        #draw background
        draw_bg()

        #draw panel
        draw_panel()

        #Draw text
        addText("Hello, It is I... Maurice... So you have come to challenge the current Coding Dino Kings?!",20,370)
        addText("Well... If you must I will support you, however I will give you some warnings...",20,395)
        addText("Depending on the option you picked at the beginning of the game, the Dino's questiosn will be different!",20,415)
        addText("Make sure to choose your answer using your 1, 2, 3, 4 Keys! Move with caution, they will challenge you as you step into them!",20,435)
        addText("But if you beat the biggest Yellow one, you can roam the forest for free for ever! Now hit ESC and Go!",20,455)


        player.update_animation()
        player.draw()

        Maurice.update_animation()
        Maurice.draw2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


        pygame.display.update()

