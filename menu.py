import pygame
from settings import *
from button import Bouton_Image

print(pygame.font.get_fonts())

class Menu:

    def __init__(self):
        
        # attribut pygame
        self.screen = pygame.display.get_surface()
        self.screen.fill("green")

        # groups
        self.all_sprites = pygame.sprite.Group()

        # text
        self.fontIntro = pygame.font.SysFont("comicsansms", FONT_SIZE_INTRO)
        self.textIntro = self.fontIntro.render("I N T R O", True, "black")
        self.textIntro_rect = self.textIntro.get_rect(center = FONT_SIZE_INTRO_POS)

        # bouton
        self.nextButton = Bouton_Image((300, 300), "assets/target.png", clickable=True)

        # intro actif ou nom
        self.introActive = True



    # gere l'intro
    def intro(self):
        
        self.screen.blit(self.textIntro, self.textIntro_rect)
        
        # bouton pour passer
        if self.nextButton.check_click():
            self.introActive = False


    # gere le menu
    def menuAffiche(self):

        self.fill("red")


    def run(self):

        if self.introActive: 
            self.intro()
        else:
            self.menu()