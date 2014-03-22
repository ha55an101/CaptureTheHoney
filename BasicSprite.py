#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import pygame
#Creates sprites for game assets 
class Sprite(pygame.sprite.Sprite):
    def __init__(self, center, picture):
        pygame.sprite.Sprite.__init__(self)
        self.image = picture
        self.rect = picture.get_rect()
        self.rect.center = center 
        
