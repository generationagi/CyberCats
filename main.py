import pygame
pygame.init
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
screen_height = 642

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cyber Cats')

font_score = pygame.font.SysFont("Bauhaus 93", 35)

#define game variables
tile_size = 40
score = 0
level_changed = False

#define colours
red = (255, 0, 0)

#Load images
bg_img = pygame.image.load('img/sky1.png')
logo_img = pygame.image.load('img/logo.png')
dirt_img = pygame.image.load('img/block.png')
game_over_img = pygame.image.load('img/game_over.png')


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
    #player.rect.x = 100
    #player.rect.y = screen_height - 130
    pass
    
    
def reload_tile_data():
    pygame.sprite.Group.empty(world.lava_group)
    pygame.sprite.Group.empty(world.exit_group)
    pygame.sprite.Group.empty(world.mushroom_group)
    pygame.sprite.Group.empty(world.blob_group)
    pygame.sprite.Group.empty(player.lava_group)
    pygame.sprite.Group.empty(player.exit_group)
    pygame.sprite.Group.empty(player.mushroom_group)
    pygame.sprite.Group.empty(player.blob_group)

def draw(screen):
    for tile in world.tile_list:
        screen.blit(tile[0], tile[1])
        
def draw_all():
    draw(screen)
    player.update()
    world.blob_group.draw(screen)
    world.exit_group.update()
    world.exit_group.draw(screen)
    world.lava_group.update()
    world.lava_group.draw(screen)
    world.blob_group.update()
    world.platform_group.draw(screen)
    world.platform_group.update()
    score = 0  # Reset the score
    world.mushroom_group.draw(screen)
    world.mushroom_group.update()
    player.draw(screen)
  


start_button = Button(screen_width // 2 - 350, screen_height // 16, 'img/start.png')
quit_button = Button(screen_width // 2 + 100, screen_height // 16, 'img/quit.png')

world = World(world_data, tile_size)

game_state = 0
player = Player(100, screen_height - 130, screen_height, game_state)
player.set_groups(world.blob_group, world.lava_group, world.exit_group, world.mushroom_group)
player.set_world(world)
game_state = player.game_state
score = player.score
player.game_state = 0

run = True
while run:
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    #print(player.game_state)
    draw_text("X " + str(score), font_score, red, tile_size - 10, 10)
    #print(level, 'level')
    #if start_button.clicked:
        #print('bbbbb')
        #reset_game()
        #draw(screen)  
    #if quit_button.clicked:
        #run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check if the left mouse button is clicked
                if start_button.rect.collidepoint(event.pos):
                    #print('aaaa')
                    reset_game()
                    player.game_state = 1
                    draw(screen)   
                if quit_button.rect.collidepoint(event.pos):
                    run = False

    if player.game_state == 0:
         # Draw the logo on the start screen
        screen.blit(logo_img, (screen_width // 2 - logo_img.get_width() // 2, screen_height // 4 - logo_img.get_height() // 2))
        start_button.draw(screen)
        quit_button.draw(screen)
        
    
    if player.game_state == 1:
        draw_all()
        if pygame.sprite.spritecollide(player, world.exit_group, True):
            player.game_state += 1
            print(player.game_state)
        

    if player.game_state == 2:
        if level_changed == False:
            world.tile_list.clear()
            print(world.tile_list, 'empty hop')
            #Redo world init with data replaced by next level
            world.__init__(world2_data, tile_size)
            print(world.tile_list)
            player.set_world(world)
            level_changed = True
            player.set_groups(world.blob_group, world.lava_group, world.exit_group, world.mushroom_group)
           
        draw_all()
        if pygame.sprite.spritecollide(player, world.exit_group, True):
            player.game_state == 3
            print(player.game_state)
        
    if player.game_state == -1:
        player.image = player.death_image
        player.update()
        player.draw(screen)
        screen.blit(logo_img, (screen_width // 2 - logo_img.get_width() // 2, screen_height // 4 - logo_img.get_height() // 2))
        screen.blit(game_over_img, (screen_width // 2 - game_over_img.get_width() // 2, screen_height // 2 - game_over_img.get_height() // 2))
        
        if start_button.draw(screen):
            reset_game()
        start_button.draw(screen)
        quit_button.draw(screen)
        score = 0  # Reset the score

    pygame.display.update()

pygame.quit()

