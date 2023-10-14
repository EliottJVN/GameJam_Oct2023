import pygame
from sprite_animation import Sprite_Animation

class Falling_Ennemy(Sprite_Animation):
    def ___init__(self,sprite_name):
        super.__init__(sprite_name)
        
        # Création des attributs par défaut du joueur
        self.velocity = 5
        self.vector = pygame.math.Vector2((0,0)) # Vérifie le déplacement

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