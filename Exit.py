import pygame

class Exit(pygame.sprint.Sprite):
      def_int_(self, x, y):
              pygame.sprite.Sprite._init_(self)
              img = pygame.image.load ("img/exit.png")
              self.image = pygame.transform.scale (img, (tile_size, int (tile_size * 1.5)))
              self.rect = self.image.get_rect ()
              self.rect.x = x
              self.rect.y = y 
