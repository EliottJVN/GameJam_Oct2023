import pygame
from player import Player


class Level:


    def __init__(self, surface):
        
        self.ecran = pygame.display.get_surface()

        # définit attribut
        self.ecran.fill("black")

        # definit classe
        self.player = Player()
