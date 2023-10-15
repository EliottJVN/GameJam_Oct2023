import pygame
from sprite_animation import Sprite_Animation


class Middle_Image(Sprite_Animation):

    def __init__(self, name, state, list_state, scalea):

        # animation burning
        self.state = state
        super().__init__(name,self.state,list_state, scale=scalea, fps = 0.15)
        self.inventory = {"stick": 0, "stone": 0}
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)


class Campfire(Middle_Image):

    def __init__(self, name, state, list_state):

        super().__init__(name,state, list_state, 2)

        # attributs
        self.isBurning = False

        # "animation" building
        self.list_images = [pygame.transform.scale_by(pygame.image.load(f"assets/images/middle_image/middle_image_campfire_building/middle_image_campfire_building{i}.png").convert_alpha(), 2) for i in range(6)]
        self.image = self.list_images[0]


class Crafting_Tables(Middle_Image):

    def __init__(self, name, state, list_state):

        super().__init__(name,state, list_state, 3)

        # attributs
        self.isCraftable = False

        # "animation" building
        self.list_images = [pygame.transform.scale_by(pygame.image.load(f"assets/images/middle_image/middle_image_crafting_pickaxe/middle_image_crafting_pickaxe{i}.png").convert_alpha(), 3) for i in range(6)]
        self.image = self.list_images[0]