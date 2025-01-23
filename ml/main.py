import pygame
from settings import * ## import all variables
from map import Map
from player import Player

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

map = Map()
player = Player()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    map.render(screen)
    player.render(screen)
    pygame.display.update()