import pygame
import random
from settings import RED

class Enemy:

    def __init__(self):
        self.x = random.randint(0, 760)
        self.y = -50
        self.width = 40
        self.height = 40
        self.speed = 3

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))