import pygame

class Mushroom(pygame.sprite.Sprite):
  # Initialize the Mushroom as a sprite
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
         # Store the tile size for scaling
        self.tile_size = tile_size
        
        # Load the mushroom image and scale it
        img = pygame.image.load('img/mushroom.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2 + 25))
        
        # Set the position of the mushroom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        pass
