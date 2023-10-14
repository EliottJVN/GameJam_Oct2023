import pygame
from settings import *

class Sprite_Animation(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super.__init__(self, sprite_name)
        self.image = pygame.image.load(f'assets/images/{sprite_name}/{sprite_name}.png') # Image par défaut
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


def load_animation_images(sprite_name):
    images = []
    path = "assets/{}/{}".format(sprite_name)
    try:
        i = 0
        while True:
            images.append(pygame.image.load(path+str(i)+".png"))
            i += 1
    except:
        pass
    
    return images

if __name__ == '__main__':
    # Création de la fenêtre
    pygame.init()
    screen = pygame.display
    screen.set_mode(TAILLE_ECRAN, pygame.RESIZABLE)
    screen.set_caption("GameJam 2023")
    running = True
    while running:
        bg = pygame.display.get_surface()
        bg.fill("green")
        screen.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        pygame.time.Clock().tick(60)
    

