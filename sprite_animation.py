import pygame
from settings import *

class Sprite_Animation(pygame.sprite.Sprite):
    def __init__(self, sprite_name, state, list_state):
        super().__init__()
        self.sprite_name = sprite_name
        self.image = pygame.image.load(f'assets/images/{sprite_name}/{sprite_name}_{state}/{sprite_name}_{state}0.png') # Image par défaut
        self.current_img = 0 # Frame début d'animation
        self.images = load_animation_images(sprite_name,list_state) #Danger

    def animate(self, vect, key):
        # Active l'animation si et seulement si il y a déplacement
        print(key)
        images = self.images[key]
        print(images)
        if vect.magnitude() > 0:
            # Anime le sprite
            if self.current_img < len(images):
                # Change d'image
                self.image = images[self.current_img]
            else:
                # Remise début d'animation
                self.current_img = 0
            # Passe au sprite suivant
            self.current_img += 1
        else: 
            self.image = images[0]
        print(self.image)


def load_animation_images(sprite_name,list_state):
    load = {}
       
    for state in list_state:
        try:
            i = 0
            images = []
            while True:
                print("load"+state)
                print(sprite_name)
                # Redimension des images.
                print('pass1')
                img = pygame.image.load(f"assets\images\{sprite_name}\{sprite_name}_{state}\{sprite_name}_{state}{i}.png")
                img = pygame.transform.scale(img,(SCALE,SCALE))
                print('pass2')
                images.append(img)
                load[state] = images
                i += 1
            
        except:
            pass
    
    print(load)
    return load
    

