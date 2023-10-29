import pygame
from pygame.locals import *
from Player import Player
from World import World  
from Lava import Lava
from Mushroom import Mushroom
from Exit import Exit
from Button import Button
from level_data import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cyber Cats')

font_score = pygame.font.SysFont("Bauhaus 93", 35)

#define game variables
tile_size = 40
game_state = 0
score = 0

#define colours
red = (255, 0, 0)

#Load images
bg_img = pygame.image.load('img/sky1.png')
logo_img = pygame.image.load('img/logo.png')
dirt_img = pygame.image.load('img/block.png')

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#load sounds
pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = pygame.mixer.Sound('sound/mushroom.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('sound/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('sound/death.wav')
game_over_fx.set_volume(0.5)

def reset_game():
    # Reset player's position
    player.rect.x = 100
    player.rect.y = screen_height - 130
    player.game_state = 1 
    
def reload_tile_data():
    #Clear the existing tile list
    #world.tile_list.clear()
    draw(screen)

def draw(screen):
    for tile in world.tile_list:
        screen.blit(tile[0], tile[1])
  

start_button = Button(screen_width // 2 - 350, screen_height // 16, 'img/start.png')
quit_button = Button(screen_width // 2 + 100, screen_height // 16, 'img/quit.png')

world = World(world_data, tile_size)

blob_group = world.blob_group
lava_group = world.lava_group
mushroom_group = world.mushroom_group
exit_group = world.exit_group

player = Player(100, screen_height - 130, screen_height, game_state)
player.set_groups(blob_group, lava_group, exit_group)
player.set_world(world)
player.game_state = 0

run = True
while run:
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    #print(game_state)
    #print(level, 'level')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check if the left mouse button is clicked
                if start_button.rect.collidepoint(event.pos):
                    reset_game()
                    draw(screen)   
                if quit_button.rect.collidepoint(event.pos):
                    pygame.quit

    if player.game_state == 0:
         # Draw the logo on the start screen
        screen.blit(logo_img, (screen_width // 2 - logo_img.get_width() // 2, screen_height // 4 - logo_img.get_height() // 2))
        start_button.draw(screen)
        quit_button.draw(screen)
    
    if player.game_state == 1:
        draw(screen)
        blob_group.draw(screen)
        world.exit_group.update()
        world.exit_group.draw(screen)
        lava_group.update()
        lava_group.draw(screen)
        blob_group.update()
        player.update()
        player.draw(screen)
        score = 0  # Reset the score
        mushroom_group.draw(screen)
        mushroom_group.update()
        
        if pygame.sprite.spritecollide(player, mushroom_group, True):
            score += 1
        if pygame.sprite.spritecollide(player, exit_group, True):
            player.game_state = 2
        
        draw_text("X " + str(score), font_score, red, tile_size - 10, 10)

    if player.game_state == 2:
        world.tile_list.clear()
        world.tile_list = world2_data
        world.__init__(world2_data, tile_size)
        reset_game()
        print(world.tile_list)
        #draw(screen)
        blob_group.draw(screen)
        world.exit_group.update()
        world.exit_group.draw(screen)
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
        screen.blit(logo_img, (screen_width // 2 - logo_img.get_width() // 2, screen_height // 4 - logo_img.get_height() // 2))
        if start_button.draw(screen):
            reset_game()
        start_button.draw(screen)
        quit_button.draw(screen)
        score = 0  # Reset the score

    pygame.display.update()

pygame.quit()

