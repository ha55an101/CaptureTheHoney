#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 

import pygame, os, sys, MenuItem, loader, BasicSprite
from pygame.locals import *  

#Class for game menu 
class MainMenu:

    def __init__(self, screen, menuItems, font):
        pygame.init() 
        self.screen = screen
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        self.font = font
        self.title = font.render("Capture the Honey", 1, (218,165,32))
        #X position of title 
        self.titleX = (self.width / 2) - ((self.title.get_rect().width) / 2)
        #Hornet icon in title screen 
        self.hornet, self.hornetRect = loader.load_image('TitleBee.png', -1)
        #Position of bee sprite in title screen 
        hornetX = (self.width / 2) - (self.hornet.get_rect().width / 2) + 50
        hornetY = ((self.height / 2) + (self.hornet.get_rect().height / 2)) - 200
        self.center = (hornetX, hornetY) 
        
        
        self.clock = pygame.time.Clock()
        #Holds menu choices 
        self.items = []
        #Adding choices to self.items 
        for index, item in enumerate(menuItems):
            menuItem = MenuItem.MenuItem(item, font, 0, 0) 

            x = (self.width / 2) - (menuItem.itemWidth / 2)
            totalHeight = len(menuItems) * menuItem.itemHeight
            y = (self.height / 2) - (totalHeight / 2) + (index * menuItem.itemHeight)
            menuItem.setPos(x, y)

            self.items.append(menuItem)
     
    #Functions for each menu choice
    #Sets text color for whether mouse is hovering over choice
    #Returns "Start" if Start is selected so menu loop can end
    #Closes if Quit is selected 
    def itemFunctions(self):
        for item in self.items:
            if item.mouseSelected(pygame.mouse.get_pos()):
                item.setColor((250,0,0))
                if item.mouseClicked(pygame.mouse) and item.text == "Start":
                    
                    return item.text
                elif item.mouseClicked(pygame.mouse) and item.text == "Quit":
                    pygame.quit()
                    sys.exit() 
                
            else:
                item.setColor((218,165,32)) 
            self.screen.blit(item.menuItem, (item.x,item.y))
         
    #Loop for handling game menu 
    def menuLoop(self):

        while 1:
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #Set screen background color 
            self.screen.fill((0, 120, 0))
            #Show title 
            self.screen.blit(self.title, (self.titleX,0))
            #Show hornet sprite 
            self.hornetSprite = BasicSprite.Sprite(self.center, self.hornet)
            self.titleHornet = pygame.sprite.RenderPlain((self.hornetSprite))
            self.titleHornet.draw(self.screen) 
            
            #Holds text returned by itemFunctions() 
            text = self.itemFunctions()
            
           
            
            pygame.display.flip()
            #If Start is selected return and end loop to main game 
            if text == "Start": return
            
             
              
    
        
