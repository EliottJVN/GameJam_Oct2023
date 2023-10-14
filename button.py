import pygame



class Bouton_Image(pygame.sprite.Sprite):

    #importe l'image la redimensionne et lui donne une position
    def __init__(self, coordonee, image_path, group = None, clickable = False, survolable = False, image_path_survolee = None, resize = None, point_position = "topleft", name = None):

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
                self.images_animation = [pygame.image.load(self.image_path).convert_alpha(),
                                         pygame.image.load(self.image_path_survolee).convert_alpha()]
                self.image = self.images_animation[0]
            if self.resize:
                self.image = pygame.image.load(self.image_path).convert_alpha()
        else:
            self.image = pygame.image.load(self.image_path).convert_alpha()
        if point_position == "topleft": self.rect = self.image.get_rect(topleft = self.coordonee)
        elif point_position == "center": self.rect = self.image.get_rect(center = self.coordonee)


    # methode qui gere l'animation
    def animation(self, state):

        if state == "idle": self.image = self.images_animation[0]
        if state == "survolee": self.image = self.images_animation[1]


    # methode modifiant la taille de l'image
    def resize_image(self, size = None):

        if size:
            self.image = pygame.transform.smoothscale(self.image, size)
            self.rect = self.image.get_rect(center = self.coordonee)
        else:
            self.image = pygame.image.load(self.image_path).convert_alpha()
            self.rect = self.image.get_rect(center = self.coordonee)


    # change image survolee si le bouton est survolee ou renvoie True si le bouton est clicke
    def check_click(self):

        mouse_pos = pygame.mouse.get_pos()

        if not self.killed:
            if self.rect.collidepoint(mouse_pos):

                if self.survolable: 
                    if self.image_path_survolee: self.animation("survolee")
                    if self.resize: self.resize_image(self.resize)

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
                    if self.resize: self.resize_image()