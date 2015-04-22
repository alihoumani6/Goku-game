#Ali Houmani, 2014F
#CST8333 STANLEY PIEDA
#GOKU GAME, Programming Language Research Project
#Last modified, 2014-10-20
#self is the kiblast class, it sets up the gokus main attack
from pygame.locals import *
import pygame

from Sprite import *

class Kiblast(Sprite):
    def __init__(self):
        super(Kiblast, self).__init__()
        self.imageLocation = "blast.png"            
        self.loadImage()

    def move(self):
        self.x += 1
        
    