import pygame
from settings import *
from menu import Menu, Game_Over
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
        self.gameOverDisplay = Game_Over()
        
    
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

        #si un bouton a été cliqué alors lancer la création d'un niveau
        if self.map.niveau:
            self.level.setup(self.map.niveau)
            self.game_state = "level"
            self.map.niveau = None


    # event loop de level
    def gameOver(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        self.gameOverDisplay.run()

        # si le niveau est finit on repasse sur la masp
        if self.gameOverDisplay.quit:
            self.__init__()

    
    # event loop de level
    def levelLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        self.level.run()

        # si le niveau est finit on repasse sur la map
        if not self.level.levelName:
            self.game_state = "map"
        if self.level.levelName == "RESET":
            self.game_state = "game over"


    def game_State_Management(self):

        while self.running:
             
            if self.game_state == "intro":
                self.intro()
            elif self.game_state == "map":
                self.mapLoop()
            elif self.game_state == "level":
                self.levelLoop()
            elif self.game_state == "game over":
                self.gameOver()

            pygame.display.update()
            self.clock.tick(FPS)




if __name__ == "__main__":
    main = Main()
    main.game_State_Management()