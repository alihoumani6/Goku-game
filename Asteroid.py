#Ali Houmani, 2014F
#CST8333 STANLEY PIEDA
#GOKU GAME, Programming Language Research Project
#Last modified, 2014-10-20
#In the asteroid class is where we set up gokus main "enemy", the aseroids. 
from pygame.locals import *
from Sprite import *
import pygame


class Asteroid(Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.imageLocation = "asteroid.png"
        self.loadImage()
    
    def move(self):
        self.x -= 1