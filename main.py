import pygame

class Main():
    def __init__(self):

        pygame.init()
    
        self.display = pygame.display
        self.display.set_mode((500,500), pygame.RESIZABLE)
        self.display.set_caption("GameJam 2023")

        self.game_state = "intro"
        self.running = 1
        self.clock = pygame.time.Clock()
        
    
    def intro(self):
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


    def game_State_Management(self):
        
        while self.running:
             
            if self.game_state == "intro":
                self.intro()

        pygame.display.update()
        self.clock.tick(60)



main = Main()

if __name__ == "__main__":

    main.game_State_Management()