import pygame, os, random, sys, asyncio
from pygame.math import Vector2
from snake import Snake
from food import Food, fish

pygame.init()
cell_size = 30
number_of_cells = 20
screen_size = cell_size*number_of_cells
OFFSET = 75
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 25)
# title_font = pygame.font.Font(None, 60)
# score_font = pygame.font.Font(None, 40)

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)


SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 150) 	
# screen.fill("green")

dt = 0
def main():    
    running = True
    food = Food()
    snake = Snake()
    

    

    while running:
        # for x in range(0, screen_size, cell_size):
        #     for y in range(0, screen_size, cell_size):
        #         rect = pygame.Rect(x, y, cell_size, cell_size)
        #         pygame.draw.rect(screen,DARK_GREEN, rect, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == SNAKE_UPDATE:
                snake.move()
                snake.collide()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.direction.y != 1 and snake.direction.y != -1:
                        snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    if snake.direction.x != -1 and snake.direction.x != 1:
                        snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    if snake.direction.y != -1 and snake.direction.y != 1:
                        snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if snake.direction.x != 1 and snake.direction.x != -1:
                        snake.direction = Vector2(-1,0)
        

        screen.fill(DARK_GREEN)
        food.draw(screen)
        snake.draw(screen)

        if food.pos == snake.body[0]:
            # snake.eat(food)
            food.randomize()
            snake.add_block()
        
        for block in snake.body[1:]:
            if block == food.pos:
                food.randomize()
            
        score_text = str(len(snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * number_of_cells - 60)
        score_y = int(cell_size * number_of_cells - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        fish_rect = fish.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(fish_rect.left,fish_rect.top,fish_rect.width + score_rect.width + 6,fish_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(fish,fish_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
        # flip() the display to put your work on screen
        pygame.display.flip()

        #clock.tick(60)  # limits FPS to 60
        dt = clock.tick(60) / 1000
        # await asyncio.sleep(0)


# asyncio.run(main())

if __name__ == "__main__":
    main()