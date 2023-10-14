import pygame
from settings import *
from player import Player


# Création de la fenêtre
pygame.init()


screen = pygame.display
screen.set_mode(TAILLE_ECRAN, pygame.RESIZABLE)
screen.set_caption("GameJam 2023")

player = Player()
running = True

while running:
    bg = pygame.display.get_surface()
    bg.fill("green")
    screen.update()
    
    player.update()
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.time.Clock().tick(60)