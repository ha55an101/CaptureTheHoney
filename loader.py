#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import os, sys, pygame
from pygame.locals import * 


#Method for loading images into game 
def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name) 
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print ('Cannot load image:', fullname)
        raise SystemExit(message) 
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
#Method for load sounds into game 
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('assets', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print ('Cannot load sound:', fullname) 
        raise SystemExit(message)
    return sound
