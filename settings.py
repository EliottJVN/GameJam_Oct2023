import random as rd
# settings base
TAILLE_ECRAN = (800, 800)
FPS = 60


# settings text
FONT_SIZE_INTRO = 15
FONT_SIZE_INTRO_POS = (30, 675)

FONT_SIZE_TITLE = 60
FONT_SIZE_TITLE_POS = (400, 200)

FONT_SIZE_STOP = 100
FONT_SIZE_STOP_POS = (400, 400)

FONT_SIZE_NBRSTICK = 20
FONT_SIZE_NBRSTICK_POS = (400, 440)

INTRO_TEXT_1 = "OU ET QUAND AI-JE BIEN PU ARRIVER...?"
INTRO_TEXT_2 = "CET ENDROIT NE M'A PAS L'AIR INHOSPITALIER;"
INTRO_TEXT_3 = "HO NON! MON PISTO-PORTAIL S'EST CASSE!"
INTRO_TEXT_4 = "LE CHEMIN SERA LONG POUR POUVOIR REPARER LE PISTO-PORTAIL"


# settings pos button
BUTONS_POS = {"intro next": (750, 600), "menu jouer": (400, 500), "menu continuer": (400, 600), "menu quit": (400, 700)}
BUTON_MAP_POS = [(200, 290), (200, 500), (400, 400)]


# settings player
HEALTH = 3
MAX_HEALTH = 3
VELOCITY_PLAYER = 5
VECTOR = (0,0) # Vérifie le déplacement
SLIDE = False
X_PLAYER = 400
Y_PLAYER = 400
STATE = 'down'
LIST_STATE = ['idle','right','left','up','down', 'right_crash', 'left_crash', 'right_crash_begin', 'left_crash_begin']

# settings running ENNEMY
VELOCITY_ENNEMY = 5
VECTOR_ENNEMY = (0,0) # Vérifie le déplacement
LIST_STATE_ENNEMY = ['right','left','right_dash','left_dash']
SCALE_ENNEMY = 3

# settings falling ENNEMY
LIST_STATE_F_ENNEMY = ['hit','idle']
SCALE_F_ENNEMY = [2.5,2.5]
FPS_ENNEMY = [0.2,2]
WAIT = 500
REFRESH = 2000

# settings middle image
LIST_MIDDLE_IMAGE = ['campfire_burning','campfire_building', "crafing_pickaxe", "crafting_table"]

# settings collectable
SCALE_COLLECTABLE = 3
POSITION_STICK = [(100,100),(700,100), (100,700), (700,700),(400,200)]
POSITION_STICK_L2 = [(120,101),(710,769), (350,710)]
POSITION_STONE = [(710,101),(101,760), (350,90)]