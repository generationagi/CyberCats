import pygame
import pickle


pygame.init()





#editor window size
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 800
#margins for the assets to fit in
LOWER_MARGIN = 100 
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))


#define game variebles
ROWS = 16

COLUMS = 20

TILE_TYPE = 9

TILE_SIZE = SCREEN_HEIGHT // ROWS

WHITE = (255, 255, 255)

#load images

bg_image = pygame.image.load('pictures/bg_img.png').convert_alpha()
#resize of background
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH , SCREEN_HEIGHT))
#list of tiles, loads all images as they are numbered
til_list = []
for x in range(TILE_TYPE):
        til = pygame.image.load(f'pictures2/editor objects/{x}.png')
        #resize of tiles
        til = pygame.transform.scale(til, (TILE_SIZE, TILE_SIZE))
        til_list.append(til)
        



#function to draw BG

def draw_bg():
        screen.blit(bg_image, (0, 0))








#Tab name
pygame.display.set_caption('lvl Editor')


#draw the grid

def draw_grid():
        #vertical lines
        for c in range(COLUMS ):
                #vertical lines
                pygame.draw.line(screen, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
	
        for c in range(ROWS ):
                #Horizontal lines
                pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))
		







run = True
while run:
        
        draw_bg()
        draw_grid()
         
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
        
  

pygame.quit()
