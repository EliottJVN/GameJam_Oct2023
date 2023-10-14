import pygame
from settings import *

class Sprite_Animation(pygame.sprite.Sprite):
    def __init__(self, sprite_name, state="down", list_state=[], scale=1, fps = 1):
        super().__init__()
        self.sprite_name = sprite_name
        self.fps = fps
        if self.sprite_name != "collectable":
            self.image = pygame.transform.scale_by(pygame.image.load(f'assets/images/{sprite_name}/{sprite_name}_{state}/{sprite_name}_{state}0.png'), scale) # Image par défaut
        self.current_img = 0 # Frame début d'animation
        self.images = load_animation_images(sprite_name,list_state, scale) #Danger

    def animate(self, vect=pygame.math.Vector2((0,0)), key=None):
        # Active l'animation si et seulement si il y a déplacement
        images = self.images[key]
        if vect.magnitude() > 0:
            # Anime le sprite
            if self.current_img < len(images):
                # Change d'image
                self.image = images[int(self.current_img)]
            else:
                # Remise début d'animation
                self.current_img = 0
            # Passe au sprite suivant
            self.current_img += self.fps
        else: 
            self.image = images[0]


def load_animation_images(sprite_name,list_state, scale):
    load = {}
    for state in list_state:
        try:
            i = 0
            images = []
            while True:
                # Redimension des images.
                img = pygame.image.load(f"assets\images\{sprite_name}\{sprite_name}_{state}\{sprite_name}_{state}{i}.png")
                img = pygame.transform.scale_by(img,scale)
                images.append(img)
                load[state] = images
                i += 1
            
        except:
            pass
    return load
    

