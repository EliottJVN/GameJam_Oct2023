import pygame
from settings import *
from button import Bouton_Image
from sprite_animation import Sprite_Animation


class Menu:

    def __init__(self):
        
        # attribut pygame
        self.screen = pygame.display.get_surface()

        # groups
        self.all_buttons_menu = pygame.sprite.Group()

        # text
        self.fontIntro = pygame.font.Font("assets/fonts/Pixeled.ttf", FONT_SIZE_INTRO)
        self.textIntro = self.fontIntro.render("I N T R O", True, "black")
        self.textIntro_rect = self.textIntro.get_rect(center = FONT_SIZE_INTRO_POS)

        self.fontTitle = pygame.font.Font("assets/fonts/Pixeled.ttf", FONT_SIZE_TITLE)
        self.textTitle = self.fontTitle.render("FLASH MONKEY", True, "black")
        self.textTitle_rect = self.textTitle.get_rect(center = FONT_SIZE_TITLE_POS)

        # intro animation
        self.index = 0
        self.images = [pygame.transform.scale_by(pygame.image.load(f'assets/images/intro/intro{i}.png'), 4) for i in range(35)]
        self.image = self.images[self.index]

        # bouton
        self.nextButton = Bouton_Image(BUTONS_POS["intro next"], "assets/images/next_button/next_button0.png", 
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/next_button/next_button2.png",
                                       resize = 2)

        self.playButton = Bouton_Image(BUTONS_POS["menu jouer"], "assets/images/start_button/start_button0.png",
                                       group =  self.all_buttons_menu,
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/start_button/start_button2.png",
                                       resize = 2)
        self.continueButton = Bouton_Image(BUTONS_POS["menu continuer"], "assets/images/continue_button/export_button0.png", 
                                       group =  self.all_buttons_menu,    
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/continue_button/export_button2.png",
                                       resize = 2)
        self.quitButton = Bouton_Image(BUTONS_POS["menu quit"], "assets/images/quit_button/quit_button0.png", 
                                       group =  self.all_buttons_menu,
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/quit_button/quit_button2.png",
                                       resize = 2)

        # iattributs
        self.introActive = True
        self.clickJouer = False
        self.quit = False


    # gere l'intro
    def intro(self):
        
        # animation
        self.screen.blit(self.image, (0,0))
        if self.index < len(self.images):
            self.image = self.images[int(self.index)]
            self.index += 0.2

        # bouton
        self.screen.blit(self.nextButton.image, self.nextButton.rect)

        # bouton pour passer
        if self.nextButton.check_click():
            self.introActive = False
            self.index = 0
            self.image = self.images[int(self.index)]



    # gere le menu
    def menuAffiche(self):
        
        self.screen.blit(self.image, (0,0))

        self.all_buttons_menu.draw(self.screen)

        pygame.draw.rect(self.screen, "black", pygame.Rect(20, 155, 745, 140))
        pygame.draw.rect(self.screen, (255, 229, 204), pygame.Rect(25, 160, 735, 100))
        self.screen.blit(self.textTitle, self.textTitle_rect)

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


class Game_Over():

    def __init__(self):

        # attribut pygame
        self.screen = pygame.display.get_surface()

        # text
        self.fontIntro = pygame.font.Font("assets/fonts/Pixeled.ttf", 50)
        self.textIntro = self.fontIntro.render("G A M E   O V E R", True, "white")
        self.textIntro_rect = self.textIntro.get_rect(center = (400, 250))

        # bouton
        self.quitButton = Bouton_Image((400, 550), "assets/images/quit_button/quit_button0.png", 
                                       clickable=True, 
                                       survolable = True, 
                                       image_path_survolee="assets/images/quit_button/quit_button2.png",
                                       resize = 3)

        # iattributs
        self.quit = False


    def run(self):

        self.screen.fill("black")

        # bouton
        self.screen.blit(self.quitButton.image, self.quitButton.rect)
        self.screen.blit(self.textIntro, self.textIntro_rect)

        # bouton pour passer
        if self.quitButton.check_click():
            self.quit = True


class Animated_Win():

    def __init__(self):
        # attribut pygame
        self.screen = pygame.display.get_surface()
        self.end = False

        # 11
        self.image_campfire = pygame.transform.scale_by(pygame.image.load(f"assets/images/middle_image/middle_image_campfire_building/middle_image_campfire_building5.png").convert_alpha(), 2)
        self.image_rectF = self.image_campfire.get_rect()
        self.image_rectF.center = (400, 400)
        self.list_images_campfire = [pygame.transform.scale_by(pygame.image.load(f"assets/images/middle_image/middle_image_campfire_burning/middle_image_campfire_burning{i}.png").convert_alpha(), 2) for i in range(4)]
        self.list_images_eclair = [pygame.transform.scale_by(pygame.image.load(f"assets/images/eclair/eclair_hit/eclair_hit{i}.png").convert_alpha(), 2.5) for i in range(4)]
        self.img11 = pygame.transform.scale(pygame.image.load(f"assets/images/backgrounds/rain.png").convert_alpha(),(800,800))

        self.index = 0
        self.image = self.list_images_eclair[self.index]

        self.startAnimationTimer = 0

    
    def run(self, levelname):

        if levelname == "11":
            # animation
            self.screen.blit(self.img11, (0,0))
            self.screen.blit(self.image_campfire, self.image_rectF)
            if 300 < pygame.time.get_ticks() - self.startAnimationTimer < 950:
                if self.index < len(self.list_images_eclair):
                    self.image = self.list_images_eclair[int(self.index)]
                    self.index += 1
                else:
                    self.index = 0
                image_rect = self.image.get_rect()
                image_rect.midbottom = self.image_rectF.midbottom
                self.screen.blit(self.image, image_rect)

            elif pygame.time.get_ticks() - self.startAnimationTimer < 2950:
                if self.index < len(self.list_images_campfire):
                    self.image = self.list_images_campfire[int(self.index)]
                    self.index += 0.2
                else:
                    self.index = 0
                self.screen.blit(self.image, self.image_rectF)

            else:
                self.end = True