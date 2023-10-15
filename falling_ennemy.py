import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Falling_Ennemy(Sprite_Animation):
    def __init__(self,sprite_name,coord):
        self.state = 'hit'
        super().__init__(sprite_name,self.state,LIST_STATE_F_ENNEMY, SCALE_F_ENNEMY)
        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.center = coord
    
    def update(self):
        Sprite_Animation.animate(self, key = self.state)
    
    def colision(self):
        pass
    
    def mouvement(self):
        pass