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


        