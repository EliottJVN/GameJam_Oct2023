import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Player(Sprite_Animation):

    def __init__(self, sprite_enemies, collide_sprite):
        self.state = STATE
        super().__init__("player",self.state,LIST_STATE, 3, fps = 0.15) 

        # Création des attributs par défaut du joueur    
        self.health = HEALTH
        self.max_health = MAX_HEALTH
        self.velocity = VELOCITY_PLAYER
        self.vector = pygame.math.Vector2(VECTOR) # Vérifie le déplacement
        self.state = STATE

        # attributs joueur slide
        self.slide = SLIDE
        self.slideActive = False
        self.perfectStop = False

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)

        # timer glissade
        self.curentTimeSlide = 0

        # group to collide
        self.sprite_enemies = sprite_enemies
        self.collide_sprite = collide_sprite 
    

    def update(self):
        if self.slide:
            self.mouvementSlide()
        else:
            self.mouvement()
        self.colisionBorder()
        self.collision()
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
            self.vector.y = -1
        elif key[pygame.K_s]:
            self.state = 'down'
            self.vector.x = 0
            self.vector.y = 1
        elif key[pygame.K_q]:
            self.state = 'left'
            self.vector.x = -1
            self.vector.y = 0
        else:
            self.vector.x = 0
            self.vector.y = 0
            self.state = 'idle'

        self.rect.center += self.velocity * self.vector


    def mouvementSlide(self):

        # Récupere un dico des clés pressées.
        key = pygame.key.get_pressed()
        
        # En fonction des clés mises à jour du vecteur position.
        if not self.slideActive:
            if key[pygame.K_d]:
                self.state = 'right'
                self.vector.x = 1
                self.vector.y = 0
            elif key[pygame.K_z]:
                self.state = 'up'
                self.vector.x = 0
                self.vector.y = -1
            elif key[pygame.K_s]:
                self.state = 'down'
                self.vector.x = 0
                self.vector.y = 1
            elif key[pygame.K_q]:
                self.state = 'left'
                self.vector.x = -1
                self.vector.y = 0

            # le player s'arrete sliiiiiide
            elif self.vector.magnitude() > 0:
                self.slideActive = True
                self.curentTimeSlide = pygame.time.get_ticks()

            # le player est arrété
            else:
                self.state = 'idle'
                self.vector.x = 0
                self.vector.y = 0         

        #gere le slide
        elif self.slideActive and pygame.time.get_ticks() - self.curentTimeSlide < 500:
            # horizontal
            self.velocity = 2
            if self.vector.x < 0:
                self.state = 'left_crash_begin'
            elif self.vector.x > 0:
                self.state = 'right_crash_begin'
            # vertical
            if self.vector.y < 0:
                self.state = 'right_crash_begin'
            elif self.vector.y > 0:
                self.state = 'left_crash_begin'

        # gere perfect stop
        elif self.slideActive and pygame.time.get_ticks() - self.curentTimeSlide < 700:
            if key[pygame.K_SPACE]:
                self.perfectStop = True

        # gere le slide
        elif self.slideActive and pygame.time.get_ticks() - self.curentTimeSlide < 3000 and not self.perfectStop:
            self.velocity = 1
            #horizontal
            if self.vector.x < 0:
                self.state = 'left_crash'     
            elif self.vector.x > 0:
                self.state = 'right_crash'
            # vertical
            if self.vector.y < 0:
                self.state = 'right_crash'
            elif self.vector.y > 0:
                self.state = 'left_crash'

        #stop slide
        else:
            self.velocity = VELOCITY_PLAYER
            self.vector.x = 0
            self.vector.y = 0
            self.slideActive = False
            self.perfectStop = False


        self.rect.center += self.velocity * self.vector


    def colisionBorder(self):
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > TAILLE_ECRAN[0]:
            self.rect.right = TAILLE_ECRAN[0]
        
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > TAILLE_ECRAN[1]:
            self.rect.bottom = TAILLE_ECRAN[1]


    def collision(self):

        for sprite in self.collide_sprite.sprites():
            if sprite.rect.colliderect(self.rect):

                # collide middleimage
                if sprite.sprite_name == "middle_image":
                    if self.vector.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.vector.x < 0:
                        self.rect.left = sprite.rect.right
                    if self.vector.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.vector.y < 0:
                        self.rect.top = sprite.rect.bottom