import pygame



#Defineing of second button class
class Button2():
    #initiating position (x,y), image and a scale factor
    def __init__(self,x, y, image, scale):

        #get the width of the image
        width = image.get_width() 

        #get the height of the image
        height = image.get_height()

        #scale the image 
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) 
        #get the rectangular area of the scaled image
        self.rect = self.image.get_rect()
        #position the top left corner of the rectangle at (x, y) 
        self.rect.topleft = (x, y) 
        #initialize the clicked status to False 
        self.clicked = False

    #define to draw the button on the screen
    def draw(self, surface): 

        #initialize action to False
        action = False

        #get the current mouse position
        pos = pygame.mouse.get_pos()  

        #check if the mouse is over button
        if self.rect.collidepoint(pos): 
            #check if left mouse button is pressed and that it was not clicked before
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: 
                #if so, set action to True
                action = True 
                #and set clicked status to True
                self.clicked = True 


        #check if the left mouse button is not pressed        
        if pygame.mouse.get_pressed()[0] == 0: 
            #if so, set clicked status to False
            self.clicked = False 
        #draw the button image on the surface at its current position   
        surface.blit(self.image, (self.rect.x, self.rect.y)) 
        
        #return whether an action/click happened
        return action 


        