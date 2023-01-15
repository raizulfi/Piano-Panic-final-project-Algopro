import pygame

screen = width,height = 324, 700

# COLORS ///////////////////////////////////////////////////
light_voilet = (54.9,32.2,100)
white = (255,255,255)

# a block will contain 1/4 of the lane 
block_width = width//4
block_height = 130

# block will inherent from the inbuild class from pygame
class Block(pygame.sprite.Sprite):
    def __init__(self, x , y,window):
        super(Block, self).__init__()
        
        self.window = window
        self.x,self.y = x,y
        self.color = light_voilet
        self.alive = True

        # making the block onces hit, transparent

        #srcalpha makes it transparent
        self.surface = pygame.Surface((block_width, block_height),pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

        # draws the block + speed will allow the blocks to move down by updating the y axis
    def update(self, speed):
        self.rect.y += speed 
        if self.rect.y >=  height:
            self.kill()
            # from the pygame libarary it will kill the blocks if it reaches moves down beyond the bottom window

        if self.alive: # if the block has not been clicked yet 
            pygame.draw.rect(self.surface, self.color,(0,0,block_width,block_height))
            pygame.draw.rect(self.surface,white,(0,0,block_width,block_height),2)
        else:
            pygame.draw.rect(self.surface, (54.9,32.2,100, 200) ,(0,0,block_width,block_height)) # not alive hence tranparent >> (x,y,z, 90) #this what makes it transparent)

        self.window.blit(self.surface, self.rect)