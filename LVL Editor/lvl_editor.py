import pygame
import pickle
import button2
from os import path


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

level = 0


#   Colors    yay!

WHITE = (255, 255, 255)

PURPLE = (128, 0, 128)

RED_PURPLE = (149, 53, 83)

YELLOW = (255,255,0)


#define font to be used
font = pygame.font.SysFont('Comic Sans', 20)

#making empty tile list

world_data = []
for row in range(ROWS):
	r = [-1] * COLUMS
	world_data.append(r)

#adding ground as editor starts
for tile in range(0, COLUMS):
	world_data[ROWS - 1][tile] = 0



#function for showing text inside the game
def draw_txt(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


#load images

bg_image = pygame.image.load('pictures/bg_img.png').convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH , SCREEN_HEIGHT))

#list that stores tiles nr list 
pic_list = []
for x in range(TILE_NR):
        pic = pygame.image.load(f'pictures3/{x}.png').convert_alpha()
        pic = pygame.transform.scale(pic , (TILE_SIZE, TILE_SIZE))
        pic_list.append(pic)

#save & load images

save_pic = pygame.image.load('menu buttons/save.png').convert_alpha()
load_pic = pygame.image.load('menu buttons/load.png').convert_alpha()

#function to draw BG

def draw_bg():
        screen.fill(PURPLE)
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

save_but = button2.Button2(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50, save_pic, 1)
load_but = button2.Button2(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 50, load_pic, 1)


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

        draw_txt(f'Level: {level}', font, YELLOW, 10, SCREEN_HEIGHT + LOWER_MARGIN - 90)
        draw_txt('To change LVL press up or down.', font, YELLOW, 10, SCREEN_HEIGHT + LOWER_MARGIN - 60)



        #save & load buttons data
        if save_but.draw(screen):
		#save level data

                #opening file to write
                pickle_out = open(f'Cyber_level{level}_data', 'wb')
                #dumping lvl data to world_data
                pickle.dump(world_data, pickle_out)
                pickle_out.close()
        if load_but.draw(screen):
                #load in level data

                #reset wold_data list
                world_data = []
		
                #check if path exsits
                if path.exists(f'Cyber_level{level}_data'):
                        #open with pickle to read data
                        pickle_in = open(f'Cyber_level{level}_data', 'rb')
                        #load in world_data list
                        world_data = pickle.load(pickle_in)


        #drawring the tile pannel and tiles
        pygame.draw.rect(screen, PURPLE, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))



        #select tile, as but_count updates SELECTED_TILE will update to the tile selected
        but_count = 0
        for but_count, i in enumerate(but_list):
                if i.draw(screen):
                        SELECTED_TILE = but_count

        #showing the tile is selected by adding rectangle behind

        pygame.draw.rect(screen, RED_PURPLE, but_list[SELECTED_TILE].rect, 3)


        #adding new tiles to map -- Editing the map

        #getting the position of the mouse
        pos = pygame.mouse.get_pos()
        x = pos[0] // TILE_SIZE
        y = pos[1] // TILE_SIZE

        #check if coordinates are inside the tile area where tiles are placed
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
		#update value of tile to curently selected tile
                if pygame.mouse.get_pressed()[0] == 1:
                        if world_data[y][x] != SELECTED_TILE:
                                world_data[y][x] = SELECTED_TILE
                if pygame.mouse.get_pressed()[2] == 1:
                        world_data[y][x] = -1


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False


                #keyboard input
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                level += 1
                        #to not get in negative lvl number we subtract only if higher than 0
                        if event.key == pygame.K_DOWN and level > 0:
                                level -= 1

        pygame.display.update()
        
  

pygame.quit()
