 
#Importing and initialising the pygame library

import pygame
pygame.init()

#Setting a resolution
screen=pygame.display.set_mode([800,600])

#Giving a name to the app as it runs
pygmae.display.set_caption("CyberCat 2077")

#Locating the Background image from a temporary picture folder *will change*
BG = pygame.image.load("/TempBGpic/cheese_planet.jpg")

# Making the background start from y0 andd x0 so it fills the screen and updating the display so we see the background
def draw():
    screen.blit(BG, (0, 0))
    pygame.display.update()




