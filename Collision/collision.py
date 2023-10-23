def update (self):
    dx = 0
    dy = 0
    walk_cooldown = 5

    #get ketpresses
    key = pygame.key.get_pressed()
    if key [pygame.K_SPACE] and self.jumped == False:
        self.vel_y = -15
        self.jumped = True
    if key [pygame.K_SPACE] == False:
        self.jumped = False
    if key [pygame.K_LEFT]:
        dx -= 5
        self.counter += 1
        self.difection = -1
    if key [pygame.K_RIGHT]:
        dx += 5
        self.counter += 1
        self.direction = -1
    if key [pygame.K_LEFT] == False and key [pygame.K_RIGHT] == False:
        self.counter = 0
        self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left [self.index]

#handle animation
if self.counter > walk_cooldown:
    self.counter = 0
    self.index += 1
    if self.index >= len(self.images_right):
        self.index = 0
    if self.direction == 1:
        self.image = self.images_right[self.index]
    if self.direction == -1:
        self.image = self.images_left[self.index]
       
#add gravity
self.vel_y =+ 1
if self.vel_y > 10:
    self.vel_y = 10
dy += self.vel_y

#check for collision
for tile in CyberCat_list:
    #check for collision in x direction
    if tile [1].colliderect(self.rect.x, self.rect.y + dy,self.widht, self.height):
    dx = 0
#chechk for collision in y direction
if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
#check if below the ground i.e. jumping
if self.vel_y < 0:
   dy = tile [1].bottom - self.rect.top
   self.vel_y = 0
#check if above the ground i.e. falling
if self.vel_y >=0:
    dy = tile[1].top - self.rect.bottom
    self.vel_y = 0

#update player coordinates
self.rect.x += dx
self.rect.y += dy

if self.rect.bottom > screen_height:
    self.rect.bottom = screen_height
    dy = 0

#draw player onto screen
screen.blit(self.image, self.rect)
pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

