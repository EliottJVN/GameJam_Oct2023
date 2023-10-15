import random as rd
# settings base
TAILLE_ECRAN = (800, 800)
FPS = 60


# settings text
FONT_SIZE_INTRO = 60
FONT_SIZE_INTRO_POS = (400, 400)

FONT_SIZE_TITLE = 60
FONT_SIZE_TITLE_POS = (400, 200)

FONT_SIZE_STOP = 100
FONT_SIZE_STOP_POS = (400, 400)

FONT_SIZE_NBRSTICK = 20
FONT_SIZE_NBRSTICK_POS = (400, 440)

INTRO_TEXT_1 = "Où et quand ai-je bien pu arriver...?"
INTRO_TEXT_2 = "Cet endroit ne m'a pas l'air inhospitalié. Tant mieux, mon Pisto-portail vient juste de me lâcher !"
INTRO_TEXT_3 = "J'ai malheureusement perdu toutes mes affaires donc le chemin sera long pour pouvoir réparer le Pisto-portail."


# settings pos button
BUTONS_POS = {"intro next": (700, 700), "menu jouer": (400, 500), "menu continuer": (400, 600), "menu quit": (400, 700)}
BUTON_MAP_POS = [(200, 300), (200, 500), (400, 400)]


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
LIST_STATE_ENNEMY = ['right','left']

# settings falling ENNEMY
LIST_STATE_F_ENNEMY = ['hit','idle']
SCALE_F_ENNEMY = 2.5
WAIT = 1000
REFRESH = 2000

# settings middle image
LIST_MIDDLE_IMAGE = ['campfire_burning','campfire_building']

# settings collectable
SCALE_COLLECTABLE = 3
POSITION_STICK = [(100,100),(700,100), (100,700), (700,700),(400,200)]