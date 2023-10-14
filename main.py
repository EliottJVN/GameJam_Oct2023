import pygame
from settings import *
from menu import Menu
from level import Level
from map import Map

class Main():
    def __init__(self):

        # initiation pyagme
        pygame.init()
    
        self.display = pygame.display
        self.display.set_mode(TAILLE_ECRAN, pygame.RESIZABLE)
        self.display.set_caption("GameJam 2023")

        self.running = 1
        self.clock = pygame.time.Clock()

        # gère le game state
        self.game_state = "intro"

        # création des objets
        self.menu = Menu()
        self.level = Level()
        self.map = Map()
        
    
    # event loop de intro + menu
    def intro(self):
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        self.menu.run()
        
        if self.menu.clickJouer:
            self.game_state = "map"
        if self.menu.quit:
            self.running = False
            pygame.quit()


    # event loop de level
    def mapLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        self.map.run()


    # event loop de level
    def levelLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        self.level.run()


    def game_State_Management(self):

        while self.running:
             
            if self.game_state == "intro":
                self.intro()
            elif self.game_state == "map":
                self.mapLoop()
            elif self.game_state == "level":
                self.levelLoop()

            pygame.display.update()
            self.clock.tick(FPS)




if __name__ == "__main__":
    main = Main()
    main.game_State_Management()