import pygame
from settings import *
from sprite_animation import Sprite_Animation
import random as rd

class Running_Ennemy(Sprite_Animation):
    def __init__(self,sprite_name):
        self.state = rd.choice(['right_dash','left_dash'])
        super().__init__(sprite_name,self.state,LIST_STATE_ENNEMY, SCALE_ENNEMY, fps = 0.2)
        self.set_up()
        self.destroy = False
        
    def set_up(self):
        # Attribut par défaut
        self.velocity = VELOCITY_ENNEMY 
        
        # Création du rectangle
        if self.state == "right_dash":
            coord = (-100,400)
            self.vect = pygame.math.Vector2((1,0))
        else:
            coord = (900,400)
            self.vect = pygame.math.Vector2((-1,0))
        self.rect = self.image.get_rect()
        self.rect.center = coord
        
    def update(self):      
        Sprite_Animation.animate(self, self.vect,key = self.state)
        if self.state == "right_dash":
            self.rect.centerx += self.velocity
            if self.rect.centerx > 400:
                self.state = 'right'
                self.velocity = VELOCITY_ENNEMY
                if not self.destroy:
                    self.destroy = True
                
        elif self.state == "left_dash":
            self.rect.centerx -= self.velocity
            if self.rect.centerx < 400:
                self.state = "left"
                self.velocity = VELOCITY_ENNEMY
                if not self.destroy:
                    self.destroy = True
                
        elif self.state == "left":
            self.rect.centerx -= self.velocity
            if self.rect.centerx < -275:
                self.state = rd.choice(['right_dash','left_dash'])
                self.set_up()
            
        elif self.state == "right":
            self.rect.centerx += self.velocity
            if self.rect.centerx > 1075:
                self.state = rd.choice(['right_dash','left_dash'])
                self.set_up()
        