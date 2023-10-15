import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Collectable(Sprite_Animation):
    def __init__(self, pos, type, group=None): # + groupe voir ligne27
        # type 3 valeurs possibles "ore", "stick" et "stone".
        # pos tuples de coord.
        # Adaptation à la classe Sprite_Animation
        super().__init__("collectable", scale=SCALE_COLLECTABLE) 
        img = pygame.image.load(f"assets\images\collectables\{type}.png")
        img = pygame.transform.scale_by(img,SCALE_COLLECTABLE)
        self.images = {
            type: [img]
        }
        
        self.image = self.images[type][0]
        self.type = type

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.center = pos       
    

    def update(self):
        Sprite_Animation.animate(self, key = self.type)
    