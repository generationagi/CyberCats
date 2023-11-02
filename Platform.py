import pygame

class Platform(pygame.sprite.Sprite):
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
        # Move the platform horizontally
        self.rect.x += self.move_direction
        self.move_counter += 1
        
        # Reverse the movement direction and reset the counter when the platform has moved a certain distance
        if abs(self.move_counter) > 50:
            #Flips movement
            self.move_direction *= -1
            self.move_counter *= -1
    
        # Check for collisions with tiles in the tile list
        for tile in self.tile_list:
            if self.rect.colliderect(tile[1]):  # Check for collision with tile rect
                self.move_direction *= -1
                self.move_counter = 0