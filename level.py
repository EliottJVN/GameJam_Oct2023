import pygame
from player import Player


class Level:


    def __init__(self):
        
        #attributs pygame
        self.screen = pygame.display.get_surface()
        self.image = None

        # attribu str "11", "12", "2"
        self.level_name = None

        # objet
        self.player = Player()

        #group
        self.all_sprite = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.Group()

        self.all_sprite.add(self.player)

    
    def setup(self, level_name):

        # crée bon setup pour le niveau
        self.level_name = level_name

        if self.level_name == "11":
            pass

        elif self.level_name == "12":
            pass

        elif self.level_name == "11":
            pass

    
    # reset tout les groupes/attributs
    def win(self):

        self.level_name = None
        self.image = None

        self.all_sprite.clear()
        self.sprite_enemies.clear()


    def run(self):

        self.screen.fill("white")
        self.all_sprite.draw(self.screen)

        self.all_sprite.update()