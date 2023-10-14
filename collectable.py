import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Collectable(Sprite_Animation):
    def ___init__(self,sprite_name):
        super.__init__(sprite_name)
        self.sprite_name = sprite_name
        
        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def update(self):
        self.animate(self.vector)
    
    def colision(self):
        pass
    