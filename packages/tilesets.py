import pygame, cv2, numpy

class Tile(pygame.sprite.Sprite):
    def __init__(self,):
        self.image = cv2.imread('assets/graphics/sprites/tileset.png')
        self.dim = numpy.shape(self.image)
        self.it = 0

        for x in range(self.dim[0] - 1):
            for y in range(self.dim[1] - 1):
                if x % 16 == 0 and y % 16 == 0:
                    cv2.imwrite("temp/"+str(self.it)+".png",self.image[x:x+16,y:y+16])
                    self.it += 1