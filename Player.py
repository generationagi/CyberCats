import pygame

class Player:
    def __init__(self, x, y, screen_height, game_state):
        self.game_state = game_state
        self.images_right = [
            pygame.transform.scale(pygame.image.load('img/cat1.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/cat2.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/cat3.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/cat4.png'), (40, 80))
        ]
        #Flip once assets are given
        self.images_left = [
            pygame.transform.scale(pygame.image.load('img/cat5.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/cat6.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/cat7.png'), (40, 80)),
            pygame.transform.scale(pygame.image.load('img/cat8.png'), (40, 80))
        ]
        self.death_image = pygame.image.load('img/death.png')
        self.counter = 0
        self.index = 0
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width() - 5
        print(self.width)
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.jump = True
        self.screen_height = screen_height
        self.hitbox = pygame.Rect(x, y, self.width, self.height)

    def set_world(self, world):
        self.world = world

    def set_groups(self, blob_group, lava_group, exit_group):
        self.blob_group = blob_group
        self.lava_group = lava_group
        self.exit_group = exit_group

    def blob_collision(self, blob_group):
        if pygame.sprite.spritecollide(self, self.blob_group, False):
            self.game_state = -1

    def lava_collision(self, lava_group):
        if pygame.sprite.spritecollide(self, self.lava_group, False):
            self.game_state = -1
            
    def update_tile_list(self, new_tile_data, tile_size):
        self.world.tile_list = []  # Clear the old tile_list
        for row in range(len(new_tile_data)):
            for col in range(len(new_tile_data[row])):
                tile = new_tile_data[row][col]
                if tile in (1, 2):  # Handle dirt and grass tiles
                    # Get the corresponding images from the World class
                    img, img_rect = (self.world.dirt_img, self.world.dirt_img.get_rect()) if tile == 1 else (self.world.grass_img, self.world.grass_img.get_rect())
                    # Recreate a new image rectangle
                    img_rect = img_rect.move(col * tile_size, row * tile_size)
                    self.world.tile_list.append((img, img_rect))
                        # Handle other tile types here...
                else:
                    continue
                
                # Recreate a new image rectangle
                img_rect = img_rect.move(col * tile_size, row * tile_size)
                self.world.tile_list.append((img, img_rect))
    
    def update(self):
        dx = 0
        dy = 0
        #Animation cd (higher = slower)
        walk_cd = 10
        self.blob_collision(self.blob_group)
        self.lava_collision(self.lava_group)
        self.standing = False
    
        

        if self.game_state == 1:
            # Get keypresses
            key = pygame.key.get_pressed()
            if self.jump == True:
                self.jumped = False   
            if key[pygame.K_SPACE] and not self.jumped:
                self.vel_y = -15
                self.jumped = True
                self.jump = False

            if key[pygame.K_LEFT]:
                #Left walk speed
                dx -= 3
                self.counter += 1
            if key[pygame.K_RIGHT]:
                #Right walk speed
                dx += 3
                self.counter += 1

            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0

            if self.counter > walk_cd:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0

            if dx < 0:
                self.image = self.images_left[self.index]
            if dx > 0:
                self.image = self.images_right[self.index]
            if dx == 0:
                self.image = pygame.transform.scale(pygame.image.load('img/cat.png'), (40, 80))


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
                            self.jumped = True
                        #If above ground
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.standing = True
                    if self.standing:
                        self.jump = True

            
                    #Update player coordinates
                self.rect.x += dx
                self.rect.y += dy
            
            


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
       

        return self.game_state

    
        
  