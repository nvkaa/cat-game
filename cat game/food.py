import pygame, os, random

from pygame.math import Vector2

cell_size = 30
number_of_cells = 20
screen_size = cell_size*number_of_cells
screen = pygame.display.set_mode((screen_size, screen_size))

OFFSET = 75

fish = pygame.image.load(os.path.join('Graphics', 'food.png'))
class Food:
    def __init__(self):
        # self.x = random.randint(0, number_of_cells-1)
        # self.y = random.randint(0, number_of_cells-1)
        # self.pos = Vector2(self.x, self.y)
        self.randomize()
        
    def draw(self, screen):
        screen.blit(fish, self.rect)

    def randomize(self):
        self.x = random.randint(0,number_of_cells - 1)
        self.y = random.randint(0,number_of_cells - 1)
        self.pos = Vector2(self.x,self.y)
        self.rect = pygame.Rect(self.x*cell_size, self.y*cell_size, cell_size, cell_size)
