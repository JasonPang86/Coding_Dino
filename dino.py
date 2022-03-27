import pygame
import sys
import loadSpriteSheet

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Coding")

black = (0,0,0)
#Dino class that created a Dino using loadSpriteSheet
class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, source, speed):
        self.speed = speed
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
        screen.blit(pygame.transform.flip(self.frame, self.flip, False).convert_alpha(), self.rect)
    
    def draw2(self): #a action to draw the Dino
        screen.blit(pygame.transform.flip(self.frame, True , False).convert_alpha(), self.rect)

    def movment(self, moving_left, moving_right):
        x_movment = 0
        y_movment = 0

        #assign movement variables based on input
        if moving_left:
            x_movment = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            x_movment = self.speed
            self.flip = False
            self.direction = 1
        
        self.rect.x += x_movment
        self.rect.y += y_movment
    
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

