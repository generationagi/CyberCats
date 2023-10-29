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

SELECTED_TILE = 0


#   Colors    yay!

WHITE = (255, 255, 255)

PURPLE = (128, 0, 128)

RED_PURPLE = (149, 53, 83)

#making empty tile list

world_data = []
for row in range(ROWS):
	r = [-1] * COLUMS
	world_data.append(r)

#adding ground underneath the map 
for tile in range(0, COLUMS):
	world_data[ROWS - 1][tile] = 0




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
		

#function for drawing world tiles
def draw_world():
        for y, row in enumerate(world_data):
                for x, tile in enumerate(row):
                        if tile >= 0:
                                screen.blit(pic_list[tile], (x * TILE_SIZE, y * TILE_SIZE))

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
        draw_world()

        #drawring the tile pannel and tiles
        pygame.draw.rect(screen, PURPLE, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))



        #select tile, as but_count updates SELECTED_TILE will update to the tile selected
        but_count = 0
        for but_count, i in enumerate(but_list):
                if i.draw(screen):
                        SELECTED_TILE = but_count

        #showing the tile is selected by adding rectangle behind

        pygame.draw.rect(screen, RED_PURPLE, but_list[SELECTED_TILE].rect, 3)


         







        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
        
  

pygame.quit()
