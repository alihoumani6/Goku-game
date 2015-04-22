# Ali Houmani, 2014F
# CST8333 STANLEY PIEDA
# GOKU GAME, Programming Language Research Project
# Last modified, 2014-10-20
# The game class is the "Main" Class, this is where all the magic happens. 

import pygame
import sys
import pygame.midi
import pygame.mixer
import time
import datetime
import sqlite3
from Character import *
from Asteroid import *
from Kiblast import *
from pygame.locals import *
import random


# Game class
class Game:

    def __init__(self):
     
        pygame.init()
        pygame.mixer.init
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        self.setUp()
        
        # music
        pygame.mixer.music.load('budo3.mp3')
        pygame.mixer.music.play(-1, 0.0)  # first parameter plays it forever, second parameter is when it should start
        kiSound = pygame.mixer.Sound('kisound.wav')
        musicPlaying = True  # set to true to play music and false when you dont
        kiShot = False  #
        
        # score
        # score = 0



    def setUp(self):
        # database creation  
        # ID is a unique identified
        #ID = 34890
        # score is a set value at the moment just as a place holder
        SCORE = 200  
        DATE = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
        
        # connecting to the database
        conn = sqlite3.connect('GameScores4.db')
         
        print "Opened database successfully";
        
        #CODE TO CREATE THE HIGHSCORES TABLE IF IT IS NOT ALREADY CREATED
        conn.execute('''CREATE TABLE IF NOT EXISTS HIGHSCORES 
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  SCORE INT NOT NULL,
                  DATE TEXT NOT NULL);''')
        #print "table created"
        # conn.commit()
        # inserting into database
        conn.execute("INSERT INTO HIGHSCORES (SCORE, DATE) VALUES (?, ?)", (SCORE, DATE))
        # conn.execute("INSERT INTO HIGHSCORES VALUES(?, ?)"), (SCORE,DATE)
         
        conn.commit()
        print "operation successful"
        
        #Exception handling for the I/O
        try:
        #The following writes to the Game text file, saying the game has been started
            f = open("Game.txt","w") #
            f.write("The game has been started.")
        except IOError:
           print "Error: can't find file or read data"
        else:
           print "Written content in the file successfully"
           f.close()    
           
        
        #Opens Game text file
        f = open("Game.txt","r") 
        print(f.read(1))
        print(f.read())
        f.close() 



    
    # MainMenu
    def Intro(self):
        intro = true
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('fresansbold.tff', 115)
        TextSurf, TextRect = text + objects("Goku Game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        
        
        
        
        
        
        
        
    # MainLoop Function
    # most of program built here
    def MainLoop(self):  
        # converted our images and set them to mouse and background
       
        character = Goku()
        
        sprites = [character]
        
        ki = []
        
        asteroids = []
        
        # Screen is the display we built
        screen = pygame.display.set_mode((1000, 400), 0, 32)
        space = "space3.jpg"
         
        background = pygame.image.load(space).convert()
        
        # this will be the real score later
        timer = 0 
       
        while True:  
            # the timer is incremented by 1       
            timer += 1  
            # draw background
            screen.blit(background, (0, 0))
            
            # drawing sprites  
            for sprite in sprites:
               
                screen.blit(sprite.image, (sprite.x, sprite.y))
                
            
            # handle character input 
            for event in pygame.event.get():
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN or event.type == KEYUP:
                    character.fly(event.key, event.type)    
            character.move()    
            
            # Handling the shooting of the ki blast
            #Use of datastructures here, appending the kiblasts
            if character.shoot == True:
               pygame.mixer.Sound('kisound.wav').play()
               kiShot = Kiblast()
               # adds kiShot to ki array using append
               ki.append(kiShot)  
               # adds kiShot(kiblast) to sprites array using append
               sprites.append(kiShot)  
               kiShot.x, kiShot.y = character.x, character.y
               character.shoot = False
            
            for kiShot in ki:
                kiShot.move()
            
            # Handling the asteroids
            #Use of datastructures here, appending the asteroids
            if timer > 1000:
                asteroid = Asteroid()
                asteroids.append(asteroid)
            # appending the asteroid VARIABLE
                sprites.append(asteroid)  
                asteroid.x = 1000
                asteroid.y = random.randint(0, 400)
                timer = 0
            
            
            for asteroid in asteroids:
                asteroid.move()
       
            #Collision check 
            for kishot in ki:
                for asteroid in asteroids:
                    if kishot.collides(asteroid):
                        asteroids.remove(asteroid)
                        sprites.remove(asteroid)
                        ki.remove(kishot)
                        sprites.remove(kishot)
                        
                        
                        
                
       
            # update screen
            pygame.display.update()
    
     
if __name__ == "__main__":    
    MainWindow = Game()
    MainWindow.MainLoop()
