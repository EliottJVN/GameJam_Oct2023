import pygame

class Sound_Manager:
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound('assets\sounds\sfx\Click_button.wav'),
            'crow': pygame.mixer.Sound('assets\sounds\sfx\crow.mp3'),
            'fire': pygame.mixer.Sound('assets\sounds\sfx\get.mp3'),
            'goat': pygame.mixer.Sound('assets\sounds\sfx\goat.mp3'),
            'eclair': pygame.mixer.Sound('assets\sounds\sfx\lightning.mp3'),
            'put': pygame.mixer.Sound('assets\sounds\sfx\Put.wav'),
            'take': pygame.mixer.Sound('assets\sounds\sfx\Take.wav'),
            }
        self.musics = {
            'niv':pygame.mixer.Sound('assets\sounds\music\Peaceful.ogg'),
            'nivbis':pygame.mixer.Sound('assets\sounds\music\Dream.ogg'),
            'nivter':pygame.mixer.Sound('assets\sounds\music\The Cave.ogg'),
            'intro':pygame.mixer.Sound('assets\sounds\music\Intro - Adventure Begin.ogg'),
            'ee': pygame.mixer.Sound('assets\sounds\music\Musique.mp3')
        }

    def play(self,name):
        self.sounds[name].play()

    def play_music(self,name):
        self.musics[name].play(10)
    
    def stop_music(self, name):
        self.musics[name].stop()
