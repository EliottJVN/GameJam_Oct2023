import pygame
from player import Player
from collectable import Collectable
from settings import *
from middleImage import *
from button import Space_Buton
from rain import Rain


class Level:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()
        self.image = None

        # attribu str "11", "12", "2"
        self.levelName = None
        self.middleImage = None

        # button space
        self.spaceButon = Space_Buton()

        #group
        self.all_sprite = pygame.sprite.Group()
        self.sprite_sticks = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.Group()
        self.collide_sprite = pygame.sprite.Group()

        # objet
        self.player = Player(self.sprite_enemies, self.collide_sprite)

    
        for i in range(5):
            stick = Collectable(POSITION_STICK[i],"stick")
            self.sprite_sticks.add(stick)
            self.collide_sprite.add(stick)
            self.all_sprite.add(stick)

        self.collectable = Collectable((200,200),"stick")
        self.rain = Rain(self.all_sprite)

        
        self.all_sprite.add(self.collectable)
        self.all_sprite.add(self.player)        

    
    # setup level en fonction niveau
    def setup(self, levelName):

        # crée bon setup pour le niveau
        self.levelName = levelName

        if self.levelName == "11":
            # fond
            self.image = pygame.image.load("assets/images/backgrounds/rain.png")
            self.image = pygame.transform.scale(self.image, (800, 800))        

            # middle image
            self.middleImage = Campfire("middle_image", "campfire_burning", LIST_MIDDLE_IMAGE)
            self.collide_sprite.add(self.middleImage)
            self.all_sprite.add(self.middleImage)

            #player
            self.player.slide = True

        elif self.levelName == "12":
            pass

        elif self.levelName == "2":
            pass

    
    # reset tout les groupes/attributs
    def win(self):

        self.all_sprite.clear()
        self.sprite_enemies.clear()

        self.levelName = None
        self.image = None
        self.middleImage = None

        self.player.slide = False 


    def update(self):

        if self.levelName == "11":

            # pour afficher SPACE pour frame perfect stop
            if self.player.slideActive and 450 < pygame.time.get_ticks() - self.player.curentTimeSlide < 700:
                self.all_sprite.add(self.spaceButon)
            else:
                self.spaceButon.kill()

            # pour la pluie
            self.rain.update()


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
        