import pygame
from Lava import Lava
from Mushroom import Mushroom
from Exit import Exit

class World():
    def __init__(self, data, tile_size):
        self.tile_list = []
        self.lava_group = pygame.sprite.Group()
        self.mushroom_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.blob_group = pygame.sprite.Group()

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

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_list):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/slime.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.tile_list = tile_list
    
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 100:
            #Flips movement
            self.move_direction *= -1
            self.move_counter *= -1
    
        for tile in self.tile_list:
            if self.rect.colliderect(tile[1]):  # Check for collision with tile rect
                self.move_direction *= -1
                self.move_counter = 0
  

        
        print(self.move_counter)
        
