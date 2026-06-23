import pygame
from settings import BLUE

class Player:

    def __init__(self):
        self.x = 380
        self.y = 500
        self.width = 40
        self.height = 60
        self.speed = 6

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))