import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Player(Sprite_Animation):
    def __init__(self):
        self.state = STATE
        super().__init__("player",self.state) 
        # Création des attributs par défaut du joueur
        
        self.health = health
        self.max_health = max_health
        self.velocity = velocity_player
        self.vector = pygame.math.Vector2(vector) # Vérifie le déplacement
        self.slide = slide
        self.state = STATE

        # Création du rectangle
        self.rect = self.image.get_rect(center=(X_PLAYER,Y_PLAYER))
    
    def update(self):
        print(self.sprite_name)
        Sprite_Animation.animate(self, self.vector)
        self.mouvement()
    
    def mouvement(self):
        # Récupere un dico des clés pressées.
        key = pygame.key.get_pressed()

        # En fonction des clés mises à jour du vecteur position.
        if key == pygame.K_d:
            self.state = 'right'
            self.vector.x = 1
            self.vector.y = 0
        elif key == pygame.K_z:
            self.state = 'up'
            self.vector.x = 0
            self.vector.y = 1
        elif key == pygame.K_s:
            self.state = 'down'
            self.vector.x = 0
            self.vector.y = -1
        elif key == pygame.K_q:
            self.state = 'left'
            self.vector.x = -1
            self.vector.y = 0
        else:
            self.state = 'idle'
        
        # Reload des nouvelles animations
        # self.sprite_name = f"player_{self.state}"
        # super().__init__(self.sprite_name)


    def colision(self):
        pass



        