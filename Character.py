#Ali Houmani, 2014F
#CST8333 STANLEY PIEDA
#GOKU GAME, Programming Language Research Project
#Last modified, 2014-10-20
#In the character class we set up gokus movements, sprites and his class 
from pygame.locals import *
from Sprite import *
import pygame


class Character(Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.imageLocation = self.characterStopped
        self.loadImage()

        self.shoot = False
        # KEYUP means not moving, K_{LEFT,RIGHT,UP,DOWN} move in that direction
        self.direction = KEYUP 

#    sets up gokus sprites
    
    def fly(self,key, eventType):            
        # if the keys are pressed down 
        if eventType == KEYDOWN:
            if key==K_LEFT:
                self.imageLocation = self.characterBack  
                self.direction = key  
                self.loadImage()     
            elif key == K_RIGHT:
                self.imageLocation = self.characterFwd 
                self.loadImage()  
                self.direction = key
            elif key == K_UP:
                self.imageLocation = self.characterUp  
                self.direction = key
                self.loadImage()  
            elif key == K_DOWN:
                self.imageLocation = self.characterDown     
                self.direction = key          
                self.loadImage()  
            elif key == K_SPACE:
                self.imageLocation = self.characterAtk
                self.shoot = True
                self.loadImage()              
                   
        # when the user removes their finger 
        elif eventType == KEYUP:
            
            self.imageLocation = self.characterStopped 
            self.loadImage()              

            self.direction = eventType
#sets up gokus movement
    def move(self):
        if self.direction==K_LEFT:
            if self.x > 0:
                self.x -= 1
        elif self.direction == K_RIGHT:
            if self.x < 1000 - self.width:
                self.x += 1
        elif self.direction == K_UP:
            if self.y > 0: 
                self.y -= 1
        elif self.direction == K_DOWN:
            if self.y < 400 - self.height:
                self.y += 1    
#Goku class, inherits character 
class Goku(Character):
    def __init__(self):
        #takes our image files and sets them to variables    
        #png for transparent images  
        self.characterStopped = "goku.png" 
        self.characterBlast = "blast.png"
        self.characterAtk = "atkgoku.png"
        self.characterFwd = "fwdgoku.png"
        self.characterBack = "gokuback.png"
        self.characterUp = "gokuup.png"
        self.characterDown = "gokudown2.png"
        
        super(Goku, self).__init__()
        
        

        
        