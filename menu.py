import pygame
from settings import *
from button import Bouton_Image

print(pygame.font.get_fonts())

class Menu:

    def __init__(self):
        
        # attribut pygame
        self.screen = pygame.display.get_surface()

        # groups
        self.all_buttons_menu = pygame.sprite.Group()

        # text
        self.fontIntro = pygame.font.SysFont("comicsansms", FONT_SIZE_INTRO)
        self.textIntro = self.fontIntro.render("I N T R O", True, "black")
        self.textIntro_rect = self.textIntro.get_rect(center = FONT_SIZE_INTRO_POS)

        self.fontTitle = pygame.font.SysFont("comicsansms", FONT_SIZE_TITLE)
        self.textTitle = self.fontTitle.render("I N T R O", True, "black")
        self.textTitle_rect = self.textTitle.get_rect(center = FONT_SIZE_TITLE_POS)

        # bouton
        self.nextButton = Bouton_Image(BUTONS_POS["intro next"], "assets/images/continue_button/export_button0.png", 
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/continue_button/export_button2.png",
                                       resize = 20)

        self.playButton = Bouton_Image(BUTONS_POS["menu jouer"], "assets/images/target.png", clickable=True, group = self.all_buttons_menu)
        self.continueButton = Bouton_Image(BUTONS_POS["menu continuer"], "assets/images/target.png", clickable=True, group = self.all_buttons_menu)
        self.quitButton = Bouton_Image(BUTONS_POS["menu quit"], "assets/images/target.png", clickable=True, group = self.all_buttons_menu)

        # iattributs
        self.introActive = True
        self.clickJouer = False
        self.quit = False


    # gere l'intro
    def intro(self):
        
        self.screen.fill("green")
        self.screen.blit(self.textIntro, self.textIntro_rect)
        self.screen.blit(self.nextButton.image, self.nextButton.rect)
        
        # bouton pour passer
        if self.nextButton.check_click():
            self.introActive = False



    # gere le menu
    def menuAffiche(self):
        
        self.screen.fill("blue")
        self.screen.blit(self.textTitle, self.textTitle_rect)

        self.all_buttons_menu.draw(self.screen)

        # boutons
        if self.playButton.check_click():
            self.clickJouer = True
        if self.continueButton.check_click():
            pass
        if self.quitButton.check_click():
            self.quit = True


    def run(self):

        if self.introActive: 
            self.intro()
        else:
            self.menuAffiche()