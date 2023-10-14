import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Running_Ennemy(Sprite_Animation):
    def ___init__(self, state):
        super.__init__("goat")
        
        # Création des attributs par défaut de la chevre
        self.velocity = VELOCITY_ENNEMY
        self.vector = pygame.math.Vector2(VECTOR_ENNEMY) # Vérifie le déplacement

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def update(self):
        self.animate(self, self.vector)
    
    def colision(self):
        pass

    def mouvement(self):
        pass