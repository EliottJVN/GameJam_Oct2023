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
        self.inventory = None
        self.vector = pygame.math.Vector2(VECTOR) # Vérifie le déplacement
        self.state = STATE
        self.afficher_pickable = False

        # attributs joueur slide
        self.slide = SLIDE
        self.slideBegin = False
        self.slideActive = False
        self.perfectStop = False
        self.walk = False
        self.space_bar_pressed = False

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)

        # timer glissade
        self.curentTimeSlide = 0
        self.curentTimeSlideBegin = 0

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
        
        # si commence a marcher
        if any([key[pygame.K_d], key[pygame.K_z], key[pygame.K_s], key[pygame.K_q]]) and not self.slideBegin and not self.walk:
            self.slideBegin = True
            self.curentTimeSlideBegin = pygame.time.get_ticks()
            self.velocity = 0

        if any([key[pygame.K_d], key[pygame.K_z], key[pygame.K_s], key[pygame.K_q]]) and pygame.time.get_ticks() - self.curentTimeSlideBegin > 500 and self.slideBegin:
            self.velocity = VELOCITY_PLAYER
            self.slideBegin = False
            self.walk = True
        elif any([key[pygame.K_d], key[pygame.K_z], key[pygame.K_s], key[pygame.K_q]]) and pygame.time.get_ticks() - self.curentTimeSlideBegin > 100 and self.slideBegin:
            self.velocity = 1
        elif any([key[pygame.K_d], key[pygame.K_z], key[pygame.K_s], key[pygame.K_q]]) and pygame.time.get_ticks() - self.curentTimeSlideBegin > 200 and self.slideBegin:
            self.velocity = 3

        # En fonction des clés mises à jour du vecteur position.
        if not self.slideActive:
            if key[pygame.K_d] and not any([key[pygame.K_z], key[pygame.K_s], key[pygame.K_q]]):
                self.state = 'right'
                self.vector.x = 1
                self.vector.y = 0
            elif key[pygame.K_z] and not any([key[pygame.K_d], key[pygame.K_s], key[pygame.K_q]]):
                self.state = 'up'
                self.vector.x = 0
                self.vector.y = -1
            elif key[pygame.K_s] and not any([key[pygame.K_d], key[pygame.K_z], key[pygame.K_q]]):
                self.state = 'down'
                self.vector.x = 0
                self.vector.y = 1
            elif key[pygame.K_q] and not any([key[pygame.K_d], key[pygame.K_z], key[pygame.K_s]]):
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
                self.walk = False     

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
            if key[pygame.K_SPACE] and not self.space_bar_pressed:
                self.perfectStop = True
                self.space_bar_pressed = True
            elif not key[pygame.K_SPACE]:
                self.space_bar_pressed = False

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

        goesInLoop = False

        for sprite in self.collide_sprite.sprites():
            if sprite.rect.colliderect(self.rect):
                # collide middleimage
                if sprite.sprite_name == "middle_image":
                    self.test_collision(sprite)
                    if self.inventory != None:
                        sprite.current_img += 1
                        sprite.image = sprite.images[sprite.state][sprite.current_img]
                        self.inventory = None

                
                elif sprite.sprite_name == "collectable":
                    self.afficher_pickable = True
                    goesInLoop = True
                    key = pygame.key.get_pressed()
                    # En fonction des clés mises à jour du vecteur position.
                    if key[pygame.K_e]:
                        if self.inventory == None:
                            self.inventory = sprite.type
                            sprite.kill()
                
                else: goesInLoop = False

            elif self.afficher_pickable and not goesInLoop:
                self.afficher_pickable = False


    def test_collision(self,sprite):
        if self.vector.x > 0:
            self.rect.right = sprite.rect.left
        if self.vector.x < 0:
            self.rect.left = sprite.rect.right
        if self.vector.y > 0:
            self.rect.bottom = sprite.rect.top
        if self.vector.y < 0:
            self.rect.top = sprite.rect.bottom       