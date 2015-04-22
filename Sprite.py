#Ali Houmani, 2014F
#CST8333 STANLEY PIEDA
#GOKU GAME, Programming Language Research Project
#Last modified, 2014-10-20
#this is the class we use to set up the sprites. 
import pygame
class Sprite(object):
    
    def __init__(self):
        screen = pygame.display.set_mode((1000, 400), 0, 32)
        self.imageLocation = ""
        self.image = None
        self.height = 0
        self.width = 0
        self.x, self.y = 0, 0   
        
    def collides(self, asteroid):
        return (asteroid.x < self.x + self.width) & (asteroid.y < self.y + self.height) & (asteroid.x + asteroid.width > self.x) & (asteroid.y + asteroid.height > self.y)
    
    #Collision detection function
    
    def loadImage(self):
        self.image = pygame.image.load(self.imageLocation).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()