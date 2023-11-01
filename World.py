import pygame
pygame.init()
from Lava import Lava
from Platform import Platform
from Mushroom import Mushroom
from Enemy import Enemy
from Exit import Exit
from level_data import world_data



class World():
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Cyber Cats')
    
    def __init__(self, data, tile_size):
        self.tile_list = []
        self.lava_group = pygame.sprite.Group()
        self.mushroom_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.blob_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()

        #Load images
        grass_img = pygame.image.load('img/top_block.png')
        dirt_img = pygame.image.load('img/block.png')


        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 3, self.tile_list)
                    self.blob_group.add(blob) 
                if tile == 5:
                    platform = Platform(col_count * tile_size, row_count * tile_size + 3, self.tile_list)
                    self.platform_group.add(platform) 
                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size, tile_size)
                    self.lava_group.add(lava)
                if tile == 7:
                    mushroom = Mushroom(col_count * tile_size, row_count * tile_size, tile_size)
                    self.mushroom_group.add(mushroom)
                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count * tile_size, tile_size)
                    self.exit_group.add(exit)
                col_count += 1
            row_count += 1
    
    
            




