import pygame


class Map:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()

        #group
        self.all_sprite = pygame.sprite.Group()     


    def run(self):

        self.screen.fill("black")
        self.all_sprite.draw(self.screen)

        self.all_sprite.update()