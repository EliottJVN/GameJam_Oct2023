import pygame
from player import Player
from settings import *
from middleImage import *


class Level:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()
        self.image = None

        # attribu str "11", "12", "2"
        self.levelName = None
        self.middleImage = None
        self.rain = False

        # text slide stop
        self.fontStop = pygame.font.SysFont("comicsansms", FONT_SIZE_STOP)
        self.textStop = self.fontStop.render("PRESS SPACE", True, "black")
        self.textStop_rect = self.textStop.get_rect(center = FONT_SIZE_STOP_POS)

        #group
        self.all_sprite = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.Group()
        self.collide_sprite = pygame.sprite.Group()

        # objet
        self.player = Player(self.sprite_enemies, self.collide_sprite)

        self.all_sprite.add(self.player)

    
    # setup level en fonction niveau
    def setup(self, levelName):

        # crée bon setup pour le niveau
        self.levelName = levelName

        if self.levelName == "11":
            # fond
            self.image = pygame.image.load("assets/images/backgrounds/rain.png")
            self.image = pygame.transform.scale(self.image, (800, 800))        
            self.rain = True

            # middle image
            self.middleImage = Campfire("middle_image", "campfire_burning", LIST_MIDDLE_IMAGE)
            self.collide_sprite.add(self.middleImage)
            self.all_sprite.add(self.middleImage)

            #player
            self.player.slide = True

        elif self.levelName == "12":
            pass

        elif self.levelName == "11":
            pass

    
    # reset tout les groupes/attributs
    def win(self):

        self.all_sprite.clear()
        self.sprite_enemies.clear()

        self.levelName = None
        self.image = None
        self.rain = False
        self.middleImage = None

        self.player.slide = False 


    def update(self):

        # pour afficher SPACE pour frame perfect stop
        if self.levelName == "11":
            if self.player.slideActive and 450 < pygame.time.get_ticks() - self.player.curentTimeSlide < 700:
                self.screen.blit(self.textStop, self.textStop_rect)


    def run(self):
        
        #verifie bien niveau avec image de fond (pour niveau par encore finit)
        if self.image:
            #fond
            self.screen.blit(self.image, (0, 0))

            #draw sprite
            self.all_sprite.draw(self.screen)

            #update ce qui se passe et draw au dessus player
            self.update()

            #update sprite
            self.all_sprite.update()
        
        #sinon ecran noir
        else:
            self.screen.fill('black')
        