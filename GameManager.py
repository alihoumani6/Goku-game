#Ali Houmani, 2014F
#CST8333 STANLEY PIEDA
#GOKU GAME, Programming Language Research Project
#Last modified, 2014-11-24
#This is just a simple start menu class that
import wx
from Game import *
import pygame
import pygame.midi
import pygame.mixer
 
def startGame(self):
    MainWindow = Game()
    MainWindow.MainLoop()
    

def onClose(self, event):
    """"""
    self.Close()    
    
if __name__ == "__main__":     
    app = wx.App(False)  
    frame = wx.Frame(None, wx.ID_ANY, "Goku Game") 
    panel = wx.Panel(frame, wx.ID_ANY)
    pygame.init()
    pygame.mixer.init
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.music.load('Zeldaintro.mid')
    pygame.mixer.music.play(-1, 0.0)  # first parameter plays it forever, second parameter is when it should start    

    #creating the buttons
    startButton = wx.Button(panel, wx.ID_ANY,"Start Game")
        
    #Setting up the layout 
    sizer = wx.FlexGridSizer(1,3,5,5)
    sizer.Add(startButton)
    border = wx.BoxSizer()
    border.Add(sizer, 0, wx.ALL, 15)
    panel.SetSizerAndFit(border)
    
    #Binding to buttons
    startButton.Bind(wx.EVT_BUTTON, startGame )
    frame.Show(True)     # Show the frame.
    app.MainLoop()
    
     
