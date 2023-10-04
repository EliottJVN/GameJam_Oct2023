import pygame

class Main:
    def __init__(self):
        pygame.init()
        
        display = pygame.display
        display.set_mode((500,500), pygame.RESIZABLE)
        display.set_caption("GameJam 2023")
        
        # Récupère la taille des écrans sous forme d'une liste de tuples
        screen = display.get_desktop_sizes()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()  
            display.flip()


if __name__ == "__main__":
    Main()