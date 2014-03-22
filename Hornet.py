#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import os,sys, pygame, BasicSprite 
from pygame.locals import *

#Hornet class for player 
class Hornet(pygame.sprite.Sprite):
    def __init__(self, center, image):
        BasicSprite.Sprite.__init__(self, center, image)
        #Whether player is hit
        self.hit = 0
        #Whether current level is done
        self.levelDone = 0
        #Amount for movement in x and y directions 
        self.xMove = 0
        self.yMove = 0
    #Movement for when direction keys are held down
    def keyDown(self, key):
        if key == K_RIGHT:
            self.xMove += -5
        elif key == K_LEFT:
            self.xMove += 5
        elif key == K_UP:
            self.yMove += 5
        elif key == K_DOWN:
            self.yMove += -5 
    #Stop current movement when key is let go 
    def keyUp(self, key):
        if key == K_RIGHT:
            self.xMove += 5
        elif key == K_LEFT:
            self.xMove += -5
        elif key == K_UP:
            self.yMove += -5
        elif key == K_DOWN:
            self.yMove += 5
    #Called if player is hit 
    def stung(self):
        if self.hit == 0:
            self.hit = 1
    #Called if player completess level 
    def levelComplete(self):
        self.levelDone = 1
    #Returns status of levelDone 
    def getLevel(self):
        return self.levelDone 

    def update(self, trees, bees, hive):
        
        self.rect.move_ip(-self.xMove, -self.yMove)
        #If player hits trees, stop further movement in current direction
        if pygame.sprite.spritecollide(self, trees, False):
            self.rect.move_ip(self.xMove, self.yMove)
        #If player hits an enemy, update self.hit
        elif pygame.sprite.spritecollide(self,bees,False):
            self.stung()
        #If player reaches hive, update levelDone 
        elif pygame.sprite.collide_rect(self, hive):
            self.levelComplete() 
