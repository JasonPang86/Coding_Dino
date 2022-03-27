import pygame
import sys
from maurice import *
from test import * 

pygame.init()


#FPS LIMITER
mainClock = pygame.time.Clock();

#Font
font = pygame.font.SysFont(None, 20)

#Game Window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

#Screen Settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Coding")

# Setting Background Image
backimg = pygame.image.load('Assets\Forest.png').convert_alpha()

def draw_bg():
    screen.blit(backimg, (0,-200))

# Rendering the title
titleimg = pygame.image.load('Assets\Title.png').convert_alpha()
def draw_title():
    screen.blit(titleimg, (0,-50))
    
playimg = pygame.image.load('Assets\Playbutton.png').convert_alpha();

# making the button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ( int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clickstatus = False

    def draw(self):
        # Mouse Position
        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clickstatus == False:
                self.clickstatus = True
                print("Gameplay in Progress")
                gamePlay()
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clickstatus = False
        
        screen.blit(self.image, (self.rect.x,self.rect.y))

playButton = Button(350,300,playimg,0.25)

run = True

while run: 

    draw_bg()
    draw_title()
    playButton.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()