import pygame
from player import Player


class Level:


    def __init__(self):
        
        self.screen = pygame.display.get_surface()  
        self.image = pygame.image.load("assets/player_left/player_left2.png")
        self.image = pygame.transform.scale_by(self.image, 5)
        self.rect = self.image.get_rect()


    def run(self):

        self.screen.fill("white")
        self.screen.blit(self.image, self.rect)