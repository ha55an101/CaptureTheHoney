#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import os,sys, pygame, BasicSprite 
from pygame.locals import *
#Class for queen bee enemy NPC
class Queen(pygame.sprite.Sprite):
    def __init__(self, center, image):
        BasicSprite.Sprite.__init__(self, center, image)
        #Amount to move in x and y directions 
        self.xMove = 5
        self.yMove = 5
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self, trees, hive):
        motion = self.rect.move((self.xMove, self.yMove))
        
        if not self.area.contains(motion):
            #If sprite hits right or left side of screen
            #Bounce off and reverse direction and flip the sprite
            if (self.rect.left < self.area.left or
                self.rect.right > self.area.right):
                self.xMove = -self.xMove
                motion = self.rect.move((self.xMove, self.yMove))
                self.image = pygame.transform.flip(self.image, 1, 0)
            #If sprite hits top or bottom of screen
            #Bounce off and reverse direction 
            if(self.rect.top > self.area.top or
               self.rect.bottom < self.area.bottom):
                self.yMove = -self.yMove
                motion = self.rect.move((self.xMove, self.yMove))
        self.rect = motion 
