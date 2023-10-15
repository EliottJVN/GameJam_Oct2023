import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Falling_Ennemy(Sprite_Animation):
    def __init__(self,sprite_name,coord):
        self.state = 'idle'
        super().__init__(sprite_name,self.state,LIST_STATE_F_ENNEMY, SCALE_F_ENNEMY)
        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.timer = pygame.time.get_ticks()
        
    def update(self):
        if pygame.time.get_ticks - self.timer >= 3000 and self.state == 'hit':
            Sprite_Animation.animate(self, key = self.state)
        else:
            Sprite_Animation.animate(self, key = 'idle')
    
    def colision(self):
        pass
    
    def mouvement(self):
        pass