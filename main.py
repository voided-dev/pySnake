import pygame
import sys
from pygame.locals import *

pygame.init()
SCR_WIDTH = 600
SCR_HEIGHT = 600
GRID_SIZE = 40
WHITE = (255,255,255)

def displayGrid():
    for x in range(0, SCR_WIDTH, GRID_SIZE):
        for y in range(0, SCR_HEIGHT, GRID_SIZE):
            grid_rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(SCREEN, 'light blue', grid_rect, 1)


def main():
    global SCREEN, CLOCK
    pygame.display.set_caption('pySnake')
    SCREEN = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
    CLOCK = pygame.time.Clock()
    running = True

    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
    
        SCREEN.fill('black')
        displayGrid()
        pygame.display.update()

    CLOCK.tick(30)


if __name__ == '__main__':
    main()
