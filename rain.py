from typing import Any
import pygame
from random import randint, choice
from settings import *


class Rain:

    def __init__(self, all_sprite):
        
        # attributs pygame
        self.screen = pygame.display.get_surface()
        self.all_sprite = all_sprite

        # listes surface
        self.drops_list = [pygame.transform.scale_by(pygame.image.load(f"assets/images/rain/rain{i}.png").convert_alpha(),3) for i in range(3)]
        self.floor_list = [pygame.transform.scale_by(pygame.image.load(f"assets/images/rain/rain{i}.png").convert_alpha(),3) for i in range(3, 6)]

    def create_floor(self):

        Drop(self.all_sprite, False, choice(self.floor_list), (randint(0,TAILLE_ECRAN[0]),randint(0,TAILLE_ECRAN[1])))

    def create_drop(self):

        Drop(self.all_sprite, True, choice(self.drops_list), (randint(50,TAILLE_ECRAN[0]),randint(-50,TAILLE_ECRAN[1]-50)))

    def update(self):

        self.create_drop()
        self.create_floor() 



class Drop(pygame.sprite.Sprite):

    def __init__(self, all_sprite, moving, surf, pos):

        super().__init__(all_sprite)

        self.image = surf
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.lifetime = randint(400, 500)
        self.start_time = pygame.time.get_ticks()

        # moving 
        self.moving = moving
        if self.moving:
            self.pos = pygame.math.Vector2(self.rect.topleft)
            self.direction = pygame.math.Vector2(-2,4)
            self.speed = randint(4,7)

    def update(self):
        # moovement
        if self.moving:
            self.rect.topleft += self.direction * self.speed
        #timer
        if pygame.time.get_ticks() - self.start_time > self.lifetime:
            self.kill()