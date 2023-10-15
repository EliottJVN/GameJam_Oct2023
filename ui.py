import pygame

class UI:
    def __init__(self,health):
        self.image =pygame.image.load(f'assets\images\heart\heart{health}.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,10)
        self.health = health

    def update(self,health):
        self.image = pygame.image.load(f'assets\images\heart\heart{health}.png')