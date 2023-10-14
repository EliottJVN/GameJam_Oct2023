import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Player(Sprite_Animation):
    def __init__(self):
        self.state = STATE
        super().__init__("player",self.state,LIST_STATE) 
        # Création des attributs par défaut du joueur
        
        self.health = HEALTH
        self.max_health = MAX_HEALTH
        self.velocity = VELOCITY_PLAYER
        self.vector = pygame.math.Vector2(VECTOR) # Vérifie le déplacement
        self.slide = SLIDE
        self.state = STATE

        # Création du rectangle
        self.rect = self.image.get_rect(center=(X_PLAYER,Y_PLAYER))
    
    def update(self):
        self.mouvement()
        Sprite_Animation.animate(self, self.vector,self.state)
        
    
    def mouvement(self):
        # Récupere un dico des clés pressées.
        key = pygame.key.get_pressed()
        
        # En fonction des clés mises à jour du vecteur position.
        if key[pygame.K_d]:
            self.state = 'right'
            self.vector.x = 1
            self.vector.y = 0
        elif key[pygame.K_z]:
            self.state = 'up'
            self.vector.x = 0
            self.vector.y = 1
        elif key[pygame.K_s]:
            self.state = 'down'
            self.vector.x = 0
            self.vector.y = -1
        elif key[pygame.K_q]:
            self.state = 'left'
            self.vector.x = -1
            self.vector.y = 0
        else:
            self.vector.x = 0
            self.vector.y = 0
            self.state = 'idle'

    def colision(self):
        pass



        