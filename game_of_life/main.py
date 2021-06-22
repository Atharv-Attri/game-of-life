import sys
import pygame
from game import GameofLife

pygame.init()
pygame.display.set_caption("Conway's Game of Life")

WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game = GameofLife(screen, scale=6)

clock = pygame.time.Clock()
fps = 60


while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.run()

    pygame.display.update()