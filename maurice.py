import pygame
from dino import Dinosaur
import loadSpriteSheet
from fightScreen import *
from mauriceInfo import speak

pygame.init()

screenWidth = 900
screenHeight = 500
run = True
BG = (50,50,50)
black = (0,0,0)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dino Coding")

clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False

scroll_thresh = 200
screen_scroll = 0
bg_scroll = 0

background = pygame.image.load("Assets\Forest.png")
background = pygame.transform.scale(background, (screenWidth, screenHeight))

def draw_bg(rel_x):
    screen.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < screenWidth:
        screen.blit(background, (rel_x, 0))

#Dino class that created a Dino using loadSpriteSheet
class Dino(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, source, speed, char_type):
        self.alive = True
        self.speed = speed
        self.char_type = char_type
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        for i in range (4):
            sprite_sheet_image = pygame.image.load(source).convert_alpha()  #load the png
            sprite_sheet = loadSpriteSheet.SpriteSheet(sprite_sheet_image)  #send the png to loadSpriteSheet
            frame = sprite_sheet.get_image(i, 24, 24, scale, black)    #return frame
            temp_list.append(frame) 
        self.animation_list.append(temp_list)

        temp_list = []
        for i in range (5, 10):
            sprite_sheet_image = pygame.image.load(source).convert_alpha()  #load the png
            sprite_sheet = loadSpriteSheet.SpriteSheet(sprite_sheet_image)  #send the png to loadSpriteSheet
            frame = sprite_sheet.get_image(i, 24, 24, scale, black)    #return frame
            temp_list.append(frame) 
        self.animation_list.append(temp_list)  

        self.frame = self.animation_list[self.action][self.frame_index]
        self.rect = self.frame.get_rect()   #created a rectangle that we can move around 
        self.rect.center = (x, y)   #rectangle starting position
        
    
    def draw(self): #a action to draw the Dino
        if self.char_type == 'Berry':
            # screen.blit(self.frame, self.rect)
            screen.blit(pygame.transform.flip(self.frame, self.flip, False).convert_alpha(), self.rect)
        if self.char_type == 'player':
            screen.blit(pygame.transform.flip(self.frame, self.flip, False).convert_alpha(), self.rect)

    def movment(self, moving_left, moving_right):
        x_movment = 0

        #assign movement variables based on input
        if moving_left:
            x_movment = -self.speed
            self.flip = True
            self.direction += 2
        if moving_right:
            x_movment = self.speed
            self.flip = False
            self.direction -= 2

        if self.char_type == "Berry":
            self.rect.x += x_movment
        
    
    def update_animation(self):
        animation_time = 100
        self.frame = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_time:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        #check if the new action is different
        if new_action != self.action:
            self.action = new_action
            #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

player = Dino(440, 450, 4, 'Assets\mort.png', 3, 'player')
Maurice = Dino(600, 450, 4, 'Assets\Berry.png', 3, 'Berry')
Berry = Dino(3000, 400, 8, 'Assets\Berry.png', 3, 'Berry')
Gary = Dino(1200, 425, 6, 'Assets\Gary.png', 3, 'Berry')
KingJulian = Dino(2200,425,6, 'Assets\Larry.png',3,'Berry')

x = 0

def gamePlay():
    run = True
    moving_left = False
    moving_right = False
    bFought = 1
    yFought = 1
    gFought = 1
    while run:
        
        clock = pygame.time.Clock()
        FPS = 60

        clock.tick(FPS)

        draw_bg(player.direction % background.get_rect().width)
        
        player.draw()
        player.update_animation()   

        Maurice.draw()
        Maurice.update_animation()
        
        Berry.draw()
        Berry.update_animation()

        Gary.draw()
        Gary.update_animation()

        KingJulian.draw()
        KingJulian.update_animation()

        if player.alive:
            if moving_left or moving_right:
                player.update_action(1) #1 means run
            else:
                player.update_action(0) #0 mean idle
            player.movment(moving_left, moving_right)
            Berry.movment(moving_right, moving_left)
            Gary.movment(moving_right,moving_left)
            KingJulian.movment(moving_right,moving_left)
            Maurice.movment(moving_right,moving_left)

        for event in pygame.event.get():
            #quit game when x is hit
            if event.type == pygame.QUIT:
                run = False
            #keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_ESCAPE:
                    run = False
            
            #keyboard release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
            if pygame.sprite.collide_rect(player,Maurice):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        speak()
            if pygame.sprite.collide_rect(player, Berry):
                while yFought:
                    fight("Yellow")
                    yFought = 0
            if pygame.sprite.collide_rect(player, Gary):
                while bFought:
                    fight("Blue")
                    bFought = 0
            if pygame.sprite.collide_rect(player, KingJulian):
                while gFought:
                    fight("Green")
                    gFought = 0

        pygame.display.update()
