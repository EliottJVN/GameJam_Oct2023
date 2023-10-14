import pygame


class Menu:

    def __init__(self):
        
        # attribut pygame
        self.screen = pygame.display.get_surface()
        self.screen.fill("green")

        # groups
        self.all_sprites = pygame.sprite.Group()


    def run(self):

        pass