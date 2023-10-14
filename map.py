import pygame
from button import Bouton_Image
from settings import *


class Map:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()

        #group
        self.all_sprite = pygame.sprite.Group()     

        # Bouton
        self.level11 = Bouton_Image(BUTON_MAP_POS[0], "assets/images/playable_button/playable_button0.png",
                                       group =  self.all_sprite,
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/playable_button/playable_button2.png",
                                       resize = 2)
        self.level12 = Bouton_Image(BUTON_MAP_POS[1], "assets/images/playable_button/playable_button0.png", 
                                       group =  self.all_sprite,    
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/playable_button/playable_button2.png",
                                       resize = 2)
        self.level2 = Bouton_Image(BUTON_MAP_POS[2], "assets/images/not_yet_button/not_yet_button0.png", 
                                       group =  self.all_sprite,
                                       clickable=False, 
                                       survolable = False, 
                                       resize = 2)
        

    def update(self):

        # si clique faire niveau et passer bouton ver
        if self.level11.check_click():
            self.level11.clickable = False
            self.level11.survolable = False
            self.level11.image = pygame.transform.scale_by(pygame.image.load("assets/images/played_button/played_button0.png").convert_alpha(), 2)

        elif self.level12.check_click():
            self.level12.clickable = False
            self.level12.survolable = False
            self.level12.image = pygame.transform.scale_by(pygame.image.load("assets/images/played_button/played_button0.png").convert_alpha(), 2)

        elif self.level2.check_click():
            pass


    def run(self):

        self.screen.fill("black")
        self.all_sprite.draw(self.screen)

        self.all_sprite.update()

        self.update()