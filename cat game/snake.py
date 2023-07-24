import pygame, os, random, sys
from pygame.math import Vector2
# from food import Food
# from main import *
pygame.init()

title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 20

OFFSET = 75

# snake = pygame.image.load("snake tu lam/Graphics/head.png")

class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5,9), Vector2(4,9)]
        # self.rect = pygame.Rect(pygame.Rect(self.body[0].x, self.body[0].y))
        self.direction = Vector2(0, 0)
        # self.image = snake
        self.image = pygame.image.load(os.path.join('Graphics', 'head.png'))
        self.new_block = False


    def draw(self, screen):
        # pygame.Surface.blit(screen, self.image, self.rect)
        for block in self.body:
            blockx = block.x*cell_size
            blocky = block.y*cell_size
            blockRect = pygame.Rect(blockx, blocky, cell_size, cell_size)
            screen.blit(self.image, blockRect)

    def add_block(self):
        self.new_block = True

    def move(self):
        if self.new_block == True:
            new_body = self.body[:]
            new_body.insert(0,new_body[0] + self.direction)
            self.body = new_body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def game_over(self):
        self.body = [Vector2(6, 9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(0,0)
        


    def collide(self):
        if not 0 <= self.body[0].x < number_of_cells or not 0 <= self.body[0].y < number_of_cells:
            self.game_over()
        
        for block in self.body[1:]:
            if block == self.body[0]:
                self.game_over()
    
    # def randomize(self):
    #     for x in range(0,number_of_cells):
    #         for y in range(0, number_of_cells):
    #             return (x,y)
    #     print((x,y))

