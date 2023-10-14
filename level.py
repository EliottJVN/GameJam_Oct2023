import pygame
from player import Player


class Level:


    def __init__(self):
        
        self.screen = pygame.display.get_surface()  


    def run(self):

        self.screen.fill("black")