import pygame
import pickle
import button2


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

TILE_SIZE = SCREEN_HEIGHT // ROWS

TILE_NR = 8

WHITE = (255, 255, 255)

PURPLE = (128, 0, 128)

#load images

bg_image = pygame.image.load('pictures/bg_img.png').convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH , SCREEN_HEIGHT))

#list that stores tiles nr list 
pic_list = []
for x in range(TILE_NR):
        pic = pygame.image.load(f'pictures3/{x}.png')
        pic = pygame.transform.scale(pic , (TILE_SIZE, TILE_SIZE))
        pic_list.append(pic)

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
		



#create buttons
#button list
but_list = []
but_col = 0
but_row = 0

#create button from each image
for i in range(len(pic_list)):
        tile_button = button2.Button2(SCREEN_WIDTH + (75 * but_col) + 50, 75 * but_row + 50, pic_list[i],  1 )
        but_list.append(tile_button)
        #as button is created, button gets shifted along
        but_col += 1
        if but_col == 3:
                but_row += 1
                but_col = 0


run = True
while run:
        
        draw_bg()
        draw_grid()

        #drawring the tile pannel and tiles
        pygame.draw.rect(screen, PURPLE, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

        for i in but_list:
                i.draw(screen)

         







        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
        
  

pygame.quit()
