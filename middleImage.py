import pygame
from sprite_animation import Sprite_Animation


class Middle_Image(Sprite_Animation):

    def __init__(self, name, state, list_state):

        # animation burning
        self.state = state
        super().__init__(name,self.state,list_state, scale=2, fps = 0.15)
        self.inventory = {}
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)


class Campfire(Middle_Image):

    def __init__(self, name, state, list_state):

        super().__init__(name,state, list_state)

        # attributs
        self.isBurning = False

        # "animation" building
        self.list_images = [pygame.transform.scale_by(pygame.image.load(f"assets/images/middle_image/middle_image_campfire_building/middle_image_campfire_building{i}.png").convert_alpha(), 2) for i in range(6)]
        self.image = self.list_images[0]
