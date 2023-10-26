import pygame

class Player:
    def __init__(self, x, y, screen_height, game_over):
        self.game_over = game_over
        self.blob_group = None
        self.lava_group = None
        self.images_right = [
            pygame.transform.scale(pygame.image.load('img/guy1.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/guy2.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/guy3.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/guy4.png'), (40, 80))
        ]
        #Flip once assets are given
        self.images_left = [
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
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.screen_height = screen_height
        self.world = None

    def set_world(self, world):
        self.world = world

    def set_groups(self, blob_group, lava_group):
        self.blob_group = blob_group
        self.lava_group = lava_group

    def blob_collision(self, blob_group):
        if pygame.sprite.spritecollide(self, self.blob_group, False):
            self.game_over = -1

    def lava_collision(self, lava_group):
        if pygame.sprite.spritecollide(self, self.lava_group, False):
            self.game_over = -1
            print(self.game_over)
    
    def update(self):
        dx = 0
        dy = 0
        walk_cd = 5

        if self.game_over == 0:
            self.blob_collision(self.blob_group)
            self.lava_collision(self.lava_group)
            #Get keypresses
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
                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0 
                    self.index = 0
                    self.image = self.images_right[self.index]

            #Animation
            if self.counter > walk_cd:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                self.image = self.images_right[self.index]
                

            #Add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #Check for collision
            if self.world:  # Ensure 'world' is set
                for tile in self.world.tile_list:
                    #Check collision x
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0
                    #Check collision y
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        #If below ground
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                        #If above ground
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0

            
                    #Update player coordinates
                self.rect.x += dx
                self.rect.y += dy


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return self.game_over

    
        
        