import pygame

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        img = pygame.image.load('img/mushroom.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2 + 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        pass
