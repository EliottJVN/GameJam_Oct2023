import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Running_Ennemy(Sprite_Animation):
    def ___init__(self):
        super.__init__("r_ennemy")
        
        # Création des attributs par défaut du joueur
        self.health = health_ennemy
        self.max_health = max_health_ennemy
        self.velocity = velocity_ennemy
        self.vector = pygame.math.Vector2(vector_ennemy) # Vérifie le déplacement

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def update(self):
        self.animate(self.vector)
    
    def colision(self):
        pass

    def mouvement(self):
        pass