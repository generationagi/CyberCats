import pygame

from main import screen

from lvl_editor import SCREEN_HEIGHT

def update(self):
    dx = 0
    dy = 0
    walk_cooldown = 5

    # Get keypresses
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and not self.jumped:
        self.vel_y = -15
        self.jumped = True
    if not key[pygame.K_SPACE]:
        self.jumped = False
    if key[pygame.K_LEFT]:
        dx -= 5
        self.counter += 1
        self.direction = -1
    if key[pygame.K_RIGHT]:
        dx += 5
        self.counter += 1
        self.direction = 1
    if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
        self.counter = 0
        self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]

    # Handle animation
    if self.counter > walk_cooldown:
        self.counter = 0
        self.index += 1
        if self.index >= len(self.images_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]

    # Add gravity
    self.vel_y += 1
    if self.vel_y > 10:
        self.vel_y = 10
    dy += self.vel_y

    # Check for collision
    for tile in CyberCat_list:
        # Check for collision in x direction
        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
            dx = 0
        # Check for collision in y direction
        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
            # Check if below the ground i.e. jumping
            if self.vel_y < 0:
                dy = tile[1].bottom - self.rect.top
                self.vel_y = 0
            # Check if above the ground i.e. falling
            if self.vel_y >= 0:
                dy = tile[1].top - self.rect.bottom
                self.vel_y = 0

    # Update player coordinates
    self.rect.x += dx
    self.rect.y += dy

    if self.rect.bottom > SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
        dy = 0

    # Draw player onto screen
    screen.blit(self.image, self.rect)
    pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

