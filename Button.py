import pygame



class Button():
    def __init__(self, x, y, image_path):
 # Load the button image and initialize its position 
        self.image = pygame.image.load(image_path)   
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    
    def draw(self, screen):
         # Draw the button on the screen
        screen.blit(self.image, self.rect)
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            # Check if the mouse pointer is over the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
             # Check if the left mouse button is clicked
                self.clicked = True
                print('clicked')
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

    