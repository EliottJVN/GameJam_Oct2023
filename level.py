import pygame
from player import Player
from collectable import Collectable
from falling_ennemy import Falling_Ennemy
from running_ennemy import Running_Ennemy
from settings import *
from middleImage import *
from button import Space_Buton, E_Buton
from rain import Rain
from ui import UI
from sound_manager import Sound_Manager


class Level:


    def __init__(self):
        self.sound_manager = Sound_Manager()
        #attributs pygame
        self.screen = pygame.display.get_surface()
        self.image = None

        # attribu str "11", "12", "2"
        self.levelName = None
        self.middleImage = None

        self.won = False

        # text
        self.text = "0/5"
        self.fontNbrStick = pygame.font.Font("assets/fonts/Pixeled.ttf", FONT_SIZE_NBRSTICK)
        self.textNbrStick = self.fontNbrStick.render(self.text, True, "white")
        self.textNbrStick_rect = self.textNbrStick.get_rect(center = FONT_SIZE_NBRSTICK_POS)

        # button space
        self.spaceButon = Space_Buton()
        self.e_button = E_Buton()

        self.image_pickup_object = None

        #group
        self.all_sprite = pygame.sprite.Group()
        self.sprite_sticks = pygame.sprite.Group()
        self.sprite_falling_enemies = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.Group()
        self.collide_sprite = pygame.sprite.Group()

        # objet
        self.player = Player(self.sprite_enemies, self.collide_sprite)
        self.ui = UI(self.player.health)
       
        self.all_sprite.add(self.player) 
        

    
    # setup level en fonction niveau
    def setup(self, levelName):

        # crée bon setup pour le niveau
        self.levelName = levelName
        self.all_sprite.add(self.player)

        self.won = False

        if self.levelName == "11":
            self.sound_manager.play_music('niv')
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

        ## Setup niv 1.2
        elif self.levelName == "12":
            # fond
            self.sound_manager.play_music('nivbis')
            self.image = pygame.image.load("assets/images/backgrounds/day.png")
            self.image = pygame.transform.scale(self.image, (800, 800))        

            # middle image
            self.middleImage = Crafting_Tables("middle_image", "crafting_table", LIST_MIDDLE_IMAGE)
            self.collide_sprite.add(self.middleImage)
            self.all_sprite.add(self.middleImage)

            self.goat = Running_Ennemy('goat')
            self.collide_sprite.add(self.goat)
            self.all_sprite.add(self.goat)

            self.createStickAndStone()


        elif self.levelName == "2":
            pass


    # crée les stick stone
    def createStickAndStone(self):
        
        for i in range(3):
                stick = Collectable(POSITION_STICK_L2[i],"stick")
                self.sprite_sticks.add(stick)
                self.collide_sprite.add(stick)
                self.all_sprite.add(stick)
        for i in range(3):
                stone = Collectable(POSITION_STONE[i],"stone")
                self.sprite_sticks.add(stone)
                self.collide_sprite.add(stone)
                self.all_sprite.add(stone)


    
    # reset tout les groupes/attributs
    def win(self):

        if self.levelName == "11" and self.middleImage.inventory["stick"] == 5:
                    
            self.all_sprite.empty()
            self.sprite_sticks.empty()
            self.sprite_falling_enemies.empty()
            self.sprite_enemies.empty()
            self.sprite_enemies.empty()

            self.won = True
            self.image = None
            self.middleImage = None
            self.get_rect = None

            self.player.delete()


    # reset tout les groupes/attributs
    def game_over(self):

        if self.player.dead:
            self.levelName = "RESET"


    def update(self):

        if self.levelName == "11":

            # pour la pluie
            self.ui.update(self.player.health)
            self.screen.blit(self.ui.image,self.ui.rect)
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
            self.sound_manager.play('eclair')
            if pygame.time.get_ticks() - self.eclair.timer >= REFRESH:
                for sprite in self.sprite_falling_enemies:
                    sprite.kill()
                self.create_eclairs()
        
        
        elif self.levelName == "12":
            self.ui.update(self.player.health)
            self.screen.blit(self.ui.image,self.ui.rect)
            if 300<self.goat.rect.centerx<500:
                self.sound_manager.play('goat')
                  

        # si le joueur peur récupérer ou déposer un objet
        if self.player.afficher_pickable:
            self.all_sprite.add(self.e_button)
            self.e_button.rect.center = (self.player.rect.centerx, self.player.rect.centery-60)
        else:
            if self.e_button in self.all_sprite:
                self.e_button.kill()

        #si le joueuer a recup un objet il s'affiche au dessus
        if self.player.inventory:
            self.image_pickup_object = pygame.transform.scale_by(pygame.image.load(f"assets/images/collectables/{self.player.inventory}.png").convert_alpha(), SCALE_COLLECTABLE)
            self.screen.blit(self.image_pickup_object, (self.player.rect.centerx-10, self.player.rect.centery-70))
        else:
            self.image_pickup_object = None
 

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

            # verifie si a win
            self.win()

            # verifie si dead
            self.game_over()
        
        #sinon ecran noir
        else:
            self.screen.fill('black')
    
    def create_eclairs(self):
        eclairs = []
        apparition = [(rd.randint(10,400),rd.randint(10,400)),
                    (rd.randint(400,790),rd.randint(10,400)),
                    (rd.randint(10,790),rd.randint(10,790)),
                    (rd.randint(10,400),rd.randint(400,790)),
                    (rd.randint(400,790),rd.randint(400,790))]
        
        for i in range(5):
            eclair = Falling_Ennemy(sprite_name='eclair',coord=apparition[i])
            self.sprite_falling_enemies.add(eclair)
            self.all_sprite.add(eclair)
            eclairs.append(eclair)

        pick = rd.randint(0,4)
        self.eclair = eclairs[pick]
        self.eclair.state = "hit"
        self.collide_sprite.add(self.eclair)
        