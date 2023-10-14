import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Player(Sprite_Animation):
    def __init__(self):
        print("Player")
        super().__init__("player") 
        
        # Création des attributs par défaut du joueur
        self.health = health
        self.max_health = max_health
        self.velocity = velocity_player
        self.vector = pygame.math.Vector2(vector) # Vérifie le déplacement
        self.slide = slide

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def update(self):
        self.animate(self.vector)
    
    def mouvement(self):
        # Récupere un dico des clés pressées.
        key = pygame.key.get_pressed()

        # En fonction des clés mises à jour du vecteur position.
        if key == pygame.K_d:
            self.vector.x = 1
            self.vector.y = 0
        elif key == pygame.K_z:
            self.vector.x = 0
            self.vector.y = 1
        elif key == pygame.K_s:
            self.vector.x = 0
            self.vector.y = -1
        elif key == pygame.K_q:
            self.vector.x = -1
            self.vector.y = 0
                
    def colision(self):
        pass



        