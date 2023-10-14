import pygame


class Map:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()

        # Bouton
        self.level11 = Bouton_Image(BUTON_MAP_POS[0], "assets/images/playable_button/playable_button0.png",
                                       group =  self.all_buttons_menu,
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/playable_button/playable_button2.png",
                                       resize = 2)
        self.level12 = Bouton_Image(BUTON_MAP_POS[1], "assets/images/playable_button/playable_button0.png", 
                                       group =  self.all_buttons_menu,    
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/playable_button/playable_button2.png",
                                       resize = 2)
        self.level2 = Bouton_Image(BUTON_MAP_POS[2], "assets/images/quit_button/quit_button0.png", 
                                       group =  self.all_buttons_menu,
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/quit_button/quit_button2.png",
                                       resize = 2)

        #group
        self.all_sprite = pygame.sprite.Group()     


    def run(self):

        self.screen.fill("black")
        self.all_sprite.draw(self.screen)

        self.all_sprite.update()