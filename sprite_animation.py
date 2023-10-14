import pygame
from settings import *

class Sprite_Animation(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.sprite_name = sprite_name
        self.image = pygame.image.load(f'assets/images/{sprite_name}/{sprite_name}0.png') # Image par défaut
        self.current_img = 0 # Frame début d'animation
        self.images = load_animation_images(sprite_name)

    def animate(self, vect):
        # Active l'animation si et seulement si il y a déplacement
        if vect.magnitude() > 0:
            # Anime le sprite
            self.current_img += 1
            if self.current_img >= len(self.images):
                # Change d'image
                self.image = self.images[self.curent_img]
            else:
                # Remise début d'animation
                self.current_img = 0
        else: 
            self.image = self.images[0]


def load_animation_images(sprite_name,list_state):
    images = {}
    
    
    for state in list_state:
        #try:
        i = 0
        while True:
            
            print("load")
            print(sprite_name)
            # Redimension des images.
            img = pygame.image.load(f"assets\images\{sprite_name}\{sprite_name}_{state}\{sprite_name}_{state}{i}.png")
            print('pass1')
            img = pygame.transform.scale(img,(img.get_width()*SCALE,img.get_length()*SCALE))
            print('pass2')
            images.append(img)
            i += 1
        #except:
            pass
    return images
    

