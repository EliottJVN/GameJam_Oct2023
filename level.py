import pygame
from player import Player
from settings import *


class Level:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()
        self.image = None

        # attribu str "11", "12", "2"
        self.level_name = None
        self.rain = False

        # objet
        self.player = Player()

        # text slide stop
        self.fontStop = pygame.font.SysFont("comicsansms", FONT_SIZE_STOP)
        self.textStop = self.fontStop.render("PRESS SPACE", True, "black")
        self.textStop_rect = self.textStop.get_rect(center = FONT_SIZE_STOP_POS)

        #group
        self.all_sprite = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.Group()

        self.all_sprite.add(self.player)

    
    # setup level en fonction niveau
    def setup(self, level_name):

        # crée bon setup pour le niveau
        self.level_name = level_name

        if self.level_name == "11":
            # fond
            self.image = pygame.image.load("assets/images/backgrounds/rain.png")
            self.image = pygame.transform.scale(self.image, (800, 800))        
            self.rain = True

            #player
            self.player.slide = True

        elif self.level_name == "12":
            pass

        elif self.level_name == "11":
            pass

    
    # reset tout les groupes/attributs
    def win(self):

        self.level_name = None
        self.image = None
        self.rain = False

        self.player.slide = False

        self.all_sprite.clear()
        self.sprite_enemies.clear()


    def update(self):

        # pour afficher SPACE pour frame perfect stop
        if self.level_name == "11":
            if self.player.slideActive and 450 < pygame.time.get_ticks() - self.player.curentTimeSlide < 700:
                self.screen.blit(self.textStop, self.textStop_rect)


    def run(self):

        #fond
        self.screen.blit(self.image, (0, 0))

        #draw sprite
        self.all_sprite.draw(self.screen)

        #update ce qui se passe et draw au dessus player
        self.update()

        #update sprite
        self.all_sprite.update()
        