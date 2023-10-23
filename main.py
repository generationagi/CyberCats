from Collision import collision
#Importing and initialising the pygame library

import pygame
pygame.init()

#Test commit by Mayerlin
#Setting a resolution
screen_width = 800
screen_height = 800

#Giving a name to the app as it runs
pygame.display.set_caption("CyberCat")
screen = pygame.display.set_mode((screen_width, screen_height))

BG = pygame.image.load('pictures/bg_img.png')

#Locating the Background image from a temporary picture folder *will change*
pygame.display.set_caption('Cyber Cats')

#define game variable
tile_size = 40








# the app running loop 

#world = World(world_data)

run = True
while run:
    
        screen.blit(BG, (0, 0))
    
        #world.draw()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
        
  

pygame.quit()


