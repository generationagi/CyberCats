import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size + 5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        pass