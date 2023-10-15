import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Falling_Ennemy(Sprite_Animation):
    def __init__(self,sprite_name,coord):
        self.state = 'idle'
        if sprite_name == 'eclair':
            scale = SCALE_F_ENNEMY[0]
            fps = FPS_ENNEMY[0]
        else:
            scale = SCALE_F_ENNEMY[1]
            fps = FPS_ENNEMY[1]
        super().__init__(sprite_name,self.state,LIST_STATE_F_ENNEMY, scale, fps=fps)
        # Création du rectangle
        
        
        self.hitbox = pygame.image.load("assets\images\eclair\eclair_idle\eclair_idle0.png")
        self.hitbox_rect = self.hitbox.get_rect()
        self.hitbox_rect.center = coord

        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.save_coord = coord
        self.timer = pygame.time.get_ticks()
        
    def update(self):      
        if pygame.time.get_ticks() - self.timer >= WAIT and self.state == 'hit':

            Sprite_Animation.animate(self, vect=pygame.math.Vector2((1,1)),key = self.state)
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.save_coord
        else:
            Sprite_Animation.animate(self, key = 'idle')
    
    def colision(self):
        pass
    
    def mouvement(self):
        pass