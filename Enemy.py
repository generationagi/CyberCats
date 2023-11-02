import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_list):
        pygame.sprite.Sprite.__init__(self)
         # Load the image for the enemy
        self.image = pygame.image.load('img/slime.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.tile_list = tile_list
    
    def update(self):
        # Move the enemy horizontally
        self.rect.x += (self.move_direction * 1.3)
        self.move_counter += 2
        if abs(self.move_counter) > 100:
            print(self.move_counter)
            #Flips movement
            self.move_direction *= -1
            self.move_counter *= -1
    
        for tile in self.tile_list:
            if self.rect.colliderect(tile[1]):  # Check for collision with tile rect
                # If there's a collision, reverse the movement direction
                self.move_direction *= -1
                self.move_counter = 0