import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Collectable(Sprite_Animation):
    def __init__(self, pos, type, group=None): # + groupe voir ligne27
        # type 3 valeurs possibles "ore", "stick" et "stone".
        # pos tuples de coord.
        self.coord = pos # Coordonnées du collectable

        # Adaptation à la classe Sprite_Animation
        super().__init__("collectable", scale=3) 
        self.images = {
            type: [pygame.image.load(f"assets\images\collectables\{type}.png")]
        }

        print(self.images)
        self.image = self.images[type][0]
        print(self.image)
        self.type = type

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)

        # group to collide
        self.collide_sprite = group 
    

    def update(self):
        # self.colisionBorder()
        # self.collision()
        Sprite_Animation.animate(self, key = self.type)
    
    def colision(self):
        pass
    