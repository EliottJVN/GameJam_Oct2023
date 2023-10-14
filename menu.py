import pygame
from settings import *

print(pygame.font.get_fonts())

class Menu:

    def __init__(self):
        
        # attribut pygame
        self.screen = pygame.display.get_surface()
        self.screen.fill("green")

        # groups
        self.all_sprites = pygame.sprite.Group()

        # text
        self.font = pygame.font.SysFont("comicsansms", FONT_SIZE_INTRO)
        self.text = self.font.render("I N T R O", True, "black")
        self.text_rect = self.text.get_rect(center = FONT_SIZE_INTRO_POS)



    def intro(self):
        
        self.screen.blit(self.text, self.text_rect)



    def run(self):

        self.intro()