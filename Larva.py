#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import os,sys, pygame, random, BasicSprite 
from pygame.locals import *
#Class for bee larvae enemy NPCs
class Larva(pygame.sprite.Sprite):
    def __init__(self, center, image):
        BasicSprite.Sprite.__init__(self, center, image)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        #Amount to move for x and y directions
        self.xMove = 0
        self.yMove = 0
        #Random direction for sprite to move in 
        self.direction = random.randint(1,4)
        
    def update(self, trees, hive):
        #Choose random direction to move in based on random number
        if self.direction == 1:
            self.xMove = -3
            
        elif self.direction == 2:
            self.yMove = -3
            
        elif self.direction == 3:
            self.xMove = 3
           
        elif self.direction == 4:
            self.yMove = 3
             
        self.rect.move_ip(self.xMove, self.yMove)
        #If larva collides with trees, reverse direction and
        #pick random direction 
        if (pygame.sprite.spritecollide(self, trees, False) or \
            pygame.sprite.collide_rect(self, hive)):
            self.direction = random.randint(1,4) 
            self.rect.move_ip(-self.xMove, -self.yMove)
