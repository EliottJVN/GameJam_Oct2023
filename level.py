import pygame
from player import Player


class Level:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()

        #group
        self.all_sprite = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.Group()

        


    def run(self):

        self.screen.fill("white")
        self.all_sprite.draw(self.screen)

        self.all_sprite.update()