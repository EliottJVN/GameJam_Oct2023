import pygame
from player import Player
from collectable import Collectable
from falling_ennemy import Falling_Ennemy
from settings import *
from middleImage import *
from button import Space_Buton, E_Buton
from rain import Rain


class Level:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()
        self.image = None

        # attribu str "11", "12", "2"
        self.levelName = None
        self.middleImage = None

        # text
        self.text = "0/5"
        self.fontNbrStick = pygame.font.Font("assets/fonts/Pixeled.ttf", FONT_SIZE_NBRSTICK)
        self.textNbrStick = self.fontNbrStick.render(self.text, True, "white")
        self.textNbrStick_rect = self.textNbrStick.get_rect(center = FONT_SIZE_NBRSTICK_POS)

        # button space
        self.spaceButon = Space_Buton()
        self.e_button = E_Buton()

        #group
        self.all_sprite = pygame.sprite.Group()
        self.sprite_sticks = pygame.sprite.Group()
        self.sprite_falling_enemies = pygame.sprite.Group()
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

            # middle image
            self.middleImage = Campfire("middle_image", "campfire_building", LIST_MIDDLE_IMAGE)
            self.collide_sprite.add(self.middleImage)
            self.all_sprite.add(self.middleImage)

            ## Collectable du niveau 1
            for i in range(5):
                stick = Collectable(POSITION_STICK[i],"stick")
                self.sprite_sticks.add(stick)
                self.collide_sprite.add(stick)
                self.all_sprite.add(stick)
            
            ## Rain
            self.rain = Rain(self.all_sprite)
            
            # Eclair
            self.create_eclairs()
            
            #player
            self.player.slide = True

        elif self.levelName == "12":
            # fond
            self.image = pygame.image.load("assets/images/backgrounds/day.png")
            self.image = pygame.transform.scale(self.image, (800, 800))        

            # middle image
            self.middleImage = Crafting_Tables("middle_image", "crafting_table", LIST_MIDDLE_IMAGE)
            self.collide_sprite.add(self.middleImage)
            self.all_sprite.add(self.middleImage)

        elif self.levelName == "2":
            pass

    
    # reset tout les groupes/attributs
    def win(self):

        self.all_sprite.empty()
        self.sprite_enemies.empty()

        self.levelName = None
        self.image = None
        self.middleImage = None

        self.player.slide = True


    def update(self):

        if self.levelName == "11":

            # pour la pluie
            self.rain.update()
            
            # pour afficher SPACE pour frame perfect stop
            if self.player.slideActive and 450 < pygame.time.get_ticks() - self.player.curentTimeSlide < 700:
                self.all_sprite.add(self.spaceButon)
            else:
                self.spaceButon.kill()

            # affiche nombre de stick
            if self.text != f"{self.middleImage.inventory['stick']}/5":
                self.text = f"{self.middleImage.inventory['stick']}/5"
                self.textNbrStick = self.fontNbrStick.render(self.text, True, "white")
            self.screen.blit(self.textNbrStick, self.textNbrStick_rect)

            # Eclair
            if pygame.time.get_ticks() - self.eclair.timer >= REFRESH:
                for sprite in self.sprite_falling_enemies:
                    sprite.kill()
                self.create_eclairs()
                        
            # si le joueur peur récupérer ou déposer un objet
        if self.player.afficher_pickable:
            self.all_sprite.add(self.e_button)
            self.e_button.rect.center = (self.player.rect.centerx, self.player.rect.centery-60)
        else:
            if self.e_button in self.all_sprite:
                self.e_button.kill()



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
    
    def create_eclairs(self):
        eclairs = []
        apparition = [(rd.randint(120,300),rd.randint(120,300)),
                    (rd.randint(500,680),rd.randint(120,300)),
                    (rd.randint(120,300),rd.randint(300,500)),
                    (rd.randint(120,300),rd.randint(500,680)),
                    (rd.randint(500,680),rd.randint(500,680))]
        
        for i in range(5):
            eclair = Falling_Ennemy(sprite_name='eclair',coord=apparition[i])
            self.sprite_falling_enemies.add(eclair)
            self.all_sprite.add(eclair)
            eclairs.append(eclair)

        pick = rd.randint(0,4)
        self.eclair = eclairs[pick]
        self.eclair.state = "hit"
        self.collide_sprite.add(self.eclair)
        