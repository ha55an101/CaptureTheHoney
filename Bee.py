#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import os,sys, pygame, BasicSprite 
from pygame.locals import *

#Class for bee enemy NPC
class Bee(pygame.sprite.Sprite):
    def __init__(self, center, image):
        BasicSprite.Sprite.__init__(self, center, image)
        #Amount to move in x direction
        self.xMove = 5
        screen = pygame.display.get_surface() 
        self.area = screen.get_rect() 
    
    def update(self, trees, hive):
        #Move sprite side to side
        x = self.rect.move((self.xMove, 0))
        #If sprite hits either side of screen, reverse direction
        if not self.area.contains(x):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.xMove = -self.xMove
                x = self.rect.move((self.xMove, 0))
        self.rect = x 
