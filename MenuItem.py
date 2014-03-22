#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import pygame, os, sys
from pygame.locals import *
#Class for each menu choice 
class MenuItem():
    def __init__(self,text, font, x, y):
        self.text = text
        self.font = font
        self.textColor = (218, 165, 32)
        self.menuItem = self.font.render(self.text, 1, self.textColor)
        self.itemWidth = self.menuItem.get_rect().width
        self.itemHeight = self.menuItem.get_rect().height + 20
        self.x = x
        self.y = y
        self.pos = self.x, self.y
        
    #Sets position in menu for each option 
    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)
    #Set color of text 
    def setColor(self, color):
        self.textColor = color
        self.menuItem = self.font.render(self.text, 1, self.textColor)
    #Checks if mouse hovers over 
    def mouseSelected(self, mouse):
        if (mouse[0] >= self.x and mouse[0] <= (self.x + self.itemWidth)) and \
            (mouse[1] >= self.y and mouse[1] <= (self.y + self.itemHeight)):
                return True
            
        return False
    #Checks if mouse clicked option 
    def mouseClicked(self, mouse):
        if mouse.get_pressed()[0]:
            return True

        return False 
        
        
        
        

        
        
        
