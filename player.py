import pygame
from sprite_animation import Sprite_Animation

class Player(Sprite_Animation):
    def ___init__(self):
        super.__init__("player")
        
        # Création des attributs par défaut du joueur
        self.health = 3
        self.max_health = 3
        self.velocity = 5
        self.vector = pygame.math.Vector2((0,0)) # Vérifie le déplacement
        self.slide = False

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



        