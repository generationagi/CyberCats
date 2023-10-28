import pygame
from pygame import mixer
from pygame.locals import *
from Player import Player
from World import World  
from Lava import Lava
from Mushroom import Mushroom
from Exit import Exit
from Button import Button
from level_data import world_data

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cyber Cats')

#define game variables
tile_size = 40
game_state = 0
level = 1

# Load images
bg_img = pygame.image.load('img/sky1.png')



#load sounds
pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = pygame.mixer.Sound('sound/mushroom.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('sound/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('sound/death.wav')
game_over_fx.set_volume(0.5)



def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))          


def reset_game():
    # Reset player's position
    player.rect.x = 100
    player.rect.y = screen_height - 130
    player.game_state = 0 

start_button = Button(screen_width // 2 - 350, screen_height // 16, 'img/start.png')
quit_button = Button(screen_width // 2 + 100, screen_height // 16, 'img/quit.png')

world = World(world_data, tile_size)

blob_group = world.blob_group
Lava_group = pygame.sprite.Group()
lava_group = world.lava_group
mushroom_group = pygame.sprite.Group()
mushroom_group = world.mushroom_group
exit_group = world.exit_group

player = Player(100, screen_height - 130, screen_height, game_state)
player.set_groups(blob_group, lava_group, exit_group)
player.set_world(world)
player.game_state = 1

run = True
while run:
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check if the left mouse button is clicked
                if start_button.rect.collidepoint(event.pos):
                    reset_game()   
                elif quit_button.rect.collidepoint(event.pos):
                    quit_button.quit_game()


    #Rendering
    if player.game_state == 1:
        start_button.draw(screen)
        quit_button.draw(screen)
    
    if player.game_state == 0:
        world.draw(screen)
        blob_group.draw(screen)
        exit_group.update()
        exit_group.draw(screen)
        lava_group.update()
        lava_group.draw(screen)
        blob_group.update()
        player.update()
        player.draw(screen)
        mushroom_group.draw(screen)
        mushroom_group.update()
         
    if player.game_state == -1:
        player.image = player.death_image
        player.update()
        player.draw(screen)
        if start_button.draw(screen):
                reset_game()
        start_button.draw(screen)
        quit_button.draw(screen)

    pygame.display.update()

pygame.quit()
