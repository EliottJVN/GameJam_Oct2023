import pygame
from sprite_animation import Sprite_Animation


class Middle_Image(Sprite_Animation):

    def __init__(self, name, state, list_state):

        # animation burning
        self.state = state
        super().__init__(name,self.state,list_state, fps = 0.15)

        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

        # attributs
        self.burning = False
        self.inventory = {'stick' : 0, 'rock' : 0}


class Campfire(Middle_Image):

    def __init__(self, name, state, list_state):

        super().__init__(name,state, list_state)

        # attributs
        self.isBurning = False

        # "animation" building
        self.list_images = [pygame.image.load(f"assets/images/campfire/campfire_building/campfire_building{i}.png").convert_alpha() for i in range(6)]
