import pygame
from sprite_animation import Sprite_Animation



class Bouton_Image(pygame.sprite.Sprite):

    #importe l'image la redimensionne et lui donne une position
    def __init__(self, coordonee, image_path, group = None, clickable = False, survolable = False, image_path_survolee = None, resize = None, point_position = "center", name = None):

        if group != None: 
            super().__init__(group)
        else: super().__init__()

        # general
        self.ecran = pygame.display.get_surface()
        self.pressed = False
        self.clickable = clickable
        self.survolable = survolable
        self.image_path = image_path
        self.image_path_survolee = image_path_survolee
        self.resize = resize
        self.coordonee = coordonee
        self.killed = False
        if name: self.name = name

        # affichage
        if self.survolable:
            if self.image_path_survolee:
                self.images_animation = [pygame.transform.scale_by(pygame.image.load(self.image_path).convert_alpha(), resize),
                                         pygame.transform.scale_by(pygame.image.load(self.image_path_survolee).convert_alpha(), resize)]
                self.image = self.images_animation[0]
        else:
            self.image = pygame.transform.scale_by(pygame.image.load(self.image_path).convert_alpha(), resize)

        if point_position == "topleft": self.rect = self.image.get_rect(topleft = self.coordonee)
        elif point_position == "center": self.rect = self.image.get_rect(center = self.coordonee)
        


    # methode qui gere l'animation
    def animation(self, state):

        if state == "idle": self.image = self.images_animation[0]
        if state == "survolee": self.image = self.images_animation[1]


    # change image survolee si le bouton est survolee ou renvoie True si le bouton est clicke
    def check_click(self):

        mouse_pos = pygame.mouse.get_pos()

        if not self.killed:
            if self.rect.collidepoint(mouse_pos):

                if self.survolable: 
                    if self.image_path_survolee: self.animation("survolee")

                if self.clickable:
                    if pygame.mouse.get_pressed()[0]:
                        self.pressed = True
                    else:
                        if self.pressed == True:
                            self.pressed = False
                            return True

            else:
                
                if self.clickable: self.pressed = False
                if self.survolable:
                    if self.image_path_survolee: self.animation("idle")



# animation bouton press !!!!!!!!!!!!
class Space_Buton(Sprite_Animation):

    def __init__(self):

        super().__init__("button_space",'animated',['animated'], 4, fps = 0.5)

        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

    def update(self):
        Sprite_Animation.animate(self, pygame.math.Vector2(1,1), 'animated')

# animation bouton press !!!!!!!!!!!!
class E_Buton(Sprite_Animation):

    def __init__(self):

        super().__init__("button_E",'animated',['animated'], 2, fps = 0.5)

        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

    def update(self):
        Sprite_Animation.animate(self, pygame.math.Vector2(1,1), 'animated')