#Jerry To
#Capture the Honey Game
#Written using Python 3.3.3 and Pygame 
#All art assets are free clip art from www.clker.com
#Sound is from www.soundbible.com 


import os,sys, pygame, BasicSprite, loader, Level, \
       Hornet, Bee, Queen, Larva, MainMenu
from pygame.locals import *
#Size for sprites 
SIZE = 38
class CaptureHoney:
    

    def __init__(self):
        pygame.init()
        #Height and width for game window 
        self.width = 520
        self.height = 650
        #Font for in-game text 
        self.font = pygame.font.Font(None, 30)
        self.font2 = pygame.font.Font(None, 48)
        #Variables for timer 
        self.timer = pygame.time.Clock()
        self.frameRate = 60
        self.frameCount = 0 

        #Initialize game level 
        self.level = 1
        self.screen = pygame.display.set_mode((self.width, self.height))
        #Game sound 
        self.sound = loader.load_sound('Jump-SoundBible.com-1007297584.wav')
        self.menu = MainMenu.MainMenu(self.screen, ('Start', 'Quit'), self.font2) 

    def loadSprites(self, levelNumber):
        #Used for finding centers of sprites 
        x_offset = SIZE / 2
        y_offset = SIZE / 2
        #Get game level, layout and sprites 
        gameLevel = Level.Level()
        self.layout = gameLevel.getLevel(levelNumber)
        sprites = gameLevel.returnSprites()
        #Create group for multiple tree and bee sprites 
        self.treeSprites = pygame.sprite.Group()
        self.beeSprites = pygame.sprite.Group()
         
       
        #Create game levels, objects 
        for y in range(len(self.layout)):
            for x in range(len(self.layout[y])):
                #Finding center point of each sprite 
                center = [(x*SIZE)+x_offset,(y*SIZE+y_offset)]

                if self.layout[y][x] == gameLevel.TREE:
                    tree = BasicSprite.Sprite(center, sprites[gameLevel.TREE-1])
                    self.treeSprites.add(tree)
                elif self.layout[y][x] == gameLevel.HORNET:
                    self.hornet = Hornet.Hornet(center, sprites[gameLevel.HORNET-1])

                elif self.layout[y][x] == gameLevel.HIVE:
                    self.hive = BasicSprite.Sprite(center, sprites[gameLevel.HIVE-1])

                elif self.layout[y][x] == gameLevel.BEE:
                    bee = Bee.Bee(center, sprites[gameLevel.BEE-1])
                    self.beeSprites.add(bee)
                elif self.layout[y][x] == gameLevel.QUEEN:
                    queen = Queen.Queen(center, sprites[gameLevel.QUEEN-1])
                    self.beeSprites.add(queen)
                elif self.layout[y][x] == gameLevel.LARVA:
                    larva = Larva.Larva(center, sprites[gameLevel.LARVA-1])
                    self.beeSprites.add(larva) 
                    
                    
        #Rendering hornet and hive sprite 
        self.hornetSprite = pygame.sprite.RenderPlain((self.hornet))
        self.hiveSprite = pygame.sprite.RenderPlain((self.hive))  
        
        

    def main(self):
        self.menu.menuLoop() 

        self.loadSprites(self.level)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,120,0))

        self.treeSprites.draw(self.background)
        
        #Main game loop 
        while 1: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
                #Handles event when player holds key down
                elif event.type == KEYDOWN:
                    if (event.key == K_RIGHT
                    or event.key == K_LEFT
                    or event.key == K_UP
                    or event.key == K_DOWN):

                        self.hornet.keyDown(event.key)
                        self.sound.play(-1)
                        
                    
                #Handles event when player lets go of key 
                elif event.type == KEYUP:
                    if (event.key == K_RIGHT
                    or event.key == K_LEFT
                    or event.key == K_UP
                    or event.key == K_DOWN):

                        self.hornet.keyUp(event.key)
                        self.sound.stop() 
                         

            #Calculating time for timer and formatting  
            totalSeconds = self.frameCount // self.frameRate
            minutes = totalSeconds // 60
            seconds = totalSeconds % 60
            time = "TIME:  {0:02}:{1:02}".format(minutes, seconds)
            #Run game while player is alive and level not complete 
            if self.hornet.hit == 0 and self.hornet.getLevel() == 0:
                self.beeSprites.update(self.treeSprites, self.hive)
                
                self.hornetSprite.update(self.treeSprites,self.beeSprites, self.hive)
                

                self.screen.blit(self.background, (0,0))
                #Shows current level number at the top of window 
                if pygame.font:
                    levelText = self.font.render('LEVEL: {0}'.format(self.level), True, (250, 250, 250))
                    levelTextX = levelText.get_rect(centerx = self.background.get_width() / 2)
                    self.screen.blit(levelText, levelTextX)

                #Updating timer and displaying 
                timeOutput = self.font.render(time, True, (250,250,250))
                self.screen.blit(timeOutput, (0,0))
                self.frameCount += 1
                self.timer.tick(self.frameRate)

                self.hornetSprite.draw(self.screen)
                self.beeSprites.draw(self.screen)
                
                self.hiveSprite.draw(self.screen)
            #If player reaches last level, show text, reset timer and restart game when player clicks mouse 
            elif self.hornet.getLevel() == 1 and self.level == 3:
                completeText = self.font.render("GAME COMPLETE! {0} CLICK FOR MENU!".format(time), True, (250,250,250)) 
                text_rect1 = completeText.get_rect()
                text_x1 = self.screen.get_width() / 2 - text_rect1.width / 2
                text_y1 = self.screen.get_height() / 2 - text_rect1.height / 2
                self.screen.blit(completeText, [text_x1, text_y1])

                if pygame.mouse.get_pressed()[0]:
                    totalSeconds = 0 
                    self.frameCount = 0 
                    self.screen.fill((0,120,0))
                    self.background.blit(self.screen, (0,0)) 
                    
                    
                    self.hornet.getLevel = 0
                    self.level -= 2
                    
                    self.main()
                    self.treeSprites.draw(self.background)
            #Else if player completes other levels, show text, reset timer and proceed to next level when player clicks mouse
            elif self.hornet.getLevel() == 1:
                completeText = self.font.render("LEVEL COMPLETE! {0} CLICK TO PROCEED!".format(time), True, (250,250,250))
                text_rect1 = completeText.get_rect()
                text_x1 = self.screen.get_width() / 2 - text_rect1.width / 2
                text_y1 = self.screen.get_height() / 2 - text_rect1.height / 2
                self.screen.blit(completeText, [text_x1, text_y1])

                if pygame.mouse.get_pressed()[0] and (self.level+1) < 4:
                    totalSeconds = 0
                    self.frameCount = 0 
                    self.screen.fill((0,120,0))
                    self.background.blit(self.screen, (0,0)) 
                    
                    
                    self.hornet.getLevel = 0
                    self.level += 1
                    self.loadSprites(self.level)
                    self.treeSprites.draw(self.background)

            
            
                
                    
            #If player dies, show text and reload level when player clicks mouse 
            elif self.hornet.hit == 1:
                gameOver = self.font.render("GAME OVER. CLICK TO RESTART", True, (250,250,250))
                text_rect = gameOver.get_rect()
                text_x = self.screen.get_width() / 2 - text_rect.width / 2
                text_y = self.screen.get_height() / 2 - text_rect.height / 2
                self.screen.blit(gameOver, [text_x, text_y])

                if pygame.mouse.get_pressed()[0]:
                    self.hornet.hit = 0
                    self.loadSprites(self.level) 
                            
            
            pygame.display.flip()

if __name__ == "__main__":
    MyGame = CaptureHoney()
    MyGame.main()
    

        



        
        
        
