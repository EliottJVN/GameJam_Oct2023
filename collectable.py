import pygame
from settings import *
from sprite_animation import Sprite_Animation

class Collectable(Sprite_Animation):
    def __init__(self, pos, type, group=None): # + groupe voir ligne27
        # type 3 valeurs possibles "ore", "stick" et "stone".
        # pos tuples de coord.
        # Adaptation à la classe Sprite_Animation
        super().__init__("collectable", scale=SCALE_COLLECTABLE) 
        img = pygame.image.load(f"assets\images\collectables\{type}.png")
        img = pygame.transform.scale_by(img,SCALE_COLLECTABLE)
        self.images = {
            type: [img]
        }
        
        self.image = self.images[type][0]
        self.type = type

        # Création du rectangle
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # group to collide
        self.collide_sprite = group[0]
        
    

    def update(self):
        self.collision()
        Sprite_Animation.animate(self, key = self.type)
    
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
    def colision(self):
        pass
    