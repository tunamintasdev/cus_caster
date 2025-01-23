import math
import pygame 
from settings import *

class Player:
    def __init__(self, velocity):
        self.x = WINDOW_WIDTH / 2
        self.y =  WINDOW_HEIGHT /2 ## the player is in the middle
        self.velocity = velocity
        
        self.radius = 3

    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)


