import pygame
from settings import *
from menu import Menu, Game_Over, Animated_Win
from level import Level
from map import Map
from sound_manager import Sound_Manager

class Main():
    def __init__(self):

        # initiation pyagme
        pygame.init()
        self.sound_manager = Sound_Manager()
        self.musique = self.sound_manager.play_music('intro')
        
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
        self.animatedWin = Animated_Win()
        
    
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
            self.sound_manager.stop_music('intro')
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


    # animate loo
    def animatedLoop(self):

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        self.animatedWin.run(self.level.levelName)

        if self.animatedWin.end:
            self.game_state = "map"
            self.level.levelName = None
            self.animatedWin.end = False

    
    # event loop de level
    def levelLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        self.level.run()

        # si le niveau est finit on repasse sur la map
        if self.level.won:
            self.game_state = "animated"
            self.animatedWin.startAnimationTimer = pygame.time.get_ticks()
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
            elif self.game_state == "animated":
                self.animatedLoop()

            pygame.display.update()
            self.clock.tick(FPS)




if __name__ == "__main__":
    main = Main()
    main.game_State_Management()