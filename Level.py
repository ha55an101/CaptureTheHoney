#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import os,sys, pygame, BasicSprite, loader

class Level():
    #init method 
    def __init__(self):
        #values representing each type of sprite 
        self.TREE = 1
        self.HORNET = 2
        self.BEE = 3
        self.LARVA = 4
        self.QUEEN = 5 
        self.HIVE = 6
         
    #Returns one of three levels based on values in arrays
    #as well as level number passed in
    def getLevel(self, levelNumber):
         firstLevel = [[0,0,0,0,0,0,0,0,0,0,0,0,0],\
                 [0,0,0,0,0,0,0,0,0,0,0,0,0],\
                 [0,1,1,1,1,1,6,1,1,1,1,1,0],\
                 [0,1,3,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,0,1,1,1,0,1,1,1,0,1,0],\
                 [0,1,0,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,1,0,1,1,1,1,1,0,1,1,0],\
                 [0,1,1,0,0,0,1,0,0,0,1,1,0],\
                 [0,1,1,1,1,0,1,0,1,1,1,1,0],\
                 [0,1,1,0,0,0,0,0,0,0,1,1,0],\
                 [0,1,1,0,1,1,1,1,1,0,1,1,0],\
                 [0,1,0,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,0,1,0,0,0,0,0,1,3,1,0],\
                 [0,1,0,1,0,1,1,1,0,1,0,1,0],\
                 [0,1,0,1,0,0,0,0,0,1,0,1,0],\
                 [0,1,0,0,0,0,2,0,0,0,0,1,0],\
                 [0,1,1,1,1,1,1,1,1,1,1,1,0]]

         secondLevel = [[0,0,0,0,0,0,0,0,0,0,0,0,0],\
                 [0,0,0,0,0,0,0,0,0,0,0,0,0],\
                 [0,1,6,1,1,1,1,1,1,1,1,1,0],\
                 [0,1,4,0,0,0,4,0,0,0,0,1,0],\
                 [0,1,1,1,0,0,0,0,0,1,1,1,0],\
                 [0,1,0,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,1,1,1,0,0,0,1,1,1,1,0],\
                 [0,1,1,0,0,0,0,0,0,0,1,1,0],\
                 [0,1,1,1,1,0,0,0,1,1,1,1,0],\
                 [0,1,0,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,0,1,1,0,1,0,1,1,0,1,0],\
                 [0,1,0,1,0,0,0,0,0,1,0,1,0],\
                 [0,1,0,1,0,1,0,1,0,1,0,1,0],\
                 [0,1,0,0,0,1,0,1,0,0,4,1,0],\
                 [0,1,0,1,1,1,0,1,1,1,0,1,0],\
                 [0,1,2,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,1,1,1,1,1,1,1,1,1,1,0]]

         thirdLevel = [[0,0,0,0,0,0,0,0,0,0,0,0,0],\
                 [0,0,0,0,0,0,0,0,0,0,0,0,0],\
                 [0,1,1,1,1,1,1,1,1,6,1,1,0],\
                 [0,1,0,0,0,0,0,0,0,5,0,1,0],\
                 [0,1,0,0,0,1,0,1,0,0,0,1,0],\
                 [0,1,1,1,1,0,0,0,1,1,1,1,0],\
                 [0,1,1,1,1,0,0,0,1,1,1,1,0],\
                 [0,1,1,1,1,0,0,0,1,1,1,1,0],\
                 [0,1,0,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,1,1,1,0,0,0,1,1,1,1,0],\
                 [0,1,1,1,1,0,1,0,1,1,1,1,0],\
                 [0,1,1,1,1,0,0,0,1,1,1,1,0],\
                 [0,1,0,0,0,0,0,0,0,0,0,1,0],\
                 [0,1,0,1,0,0,0,0,0,1,0,1,0],\
                 [0,1,0,1,1,0,0,0,1,1,0,1,0],\
                 [0,1,0,0,0,0,2,0,0,0,0,1,0],\
                 [0,1,1,1,1,1,1,1,1,1,1,1,0]]

         if levelNumber == 1:
             self.levelReturned = firstLevel
         elif levelNumber == 2:
            self.levelReturned = secondLevel
         elif levelNumber == 3:
            self.levelReturned = thirdLevel 
         
         return self.levelReturned 
        
    #Loads and returns sprites for game 
    def returnSprites(self):
        tree, rec = loader.load_image('tree.png',-1)
        hornet, rect = loader.load_image('hornet.png',-1)
        bee, rect = loader.load_image('bee.png',-1)
        larva, rect = loader.load_image('larva.png', -1) 
        queen, rect = loader.load_image('queen2.png', -1) 
        hive, rect = loader.load_image('beehive2.png',-1)
        return [tree, hornet, bee, larva, queen, hive] 
