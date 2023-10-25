import pygame

class Player:
    def __init__(self, x, y, screen_height):
        self.images_right = [
            pygame.transform.scale(pygame.image.load('img/guy1.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/guy2.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/guy3.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/guy4.png'), (40, 80))
        ]

        self.counter = 0
        self.index = 0
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.screen_height = screen_height
    
    def update(self):
        dx = 0
        dy = 0
        walk_cd = 5

        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.jumped:
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            self.counter += 1
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
                
        #Animation
        if self.counter > walk_cd:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            self.image = self.images_right[self.index]
            

        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check for collision

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            dy = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)