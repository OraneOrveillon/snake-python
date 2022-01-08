import pygame


class Mixer:
    """Deals with application's sounds and musics"""
    def __init__(self):
        """Initializes pygame's mixer"""
        pygame.mixer.init()

    @staticmethod
    def play_sound(sound_name):
        """
        Plays a sound with pygame's mixer
        :param sound_name: The sound's filename
        """
        sound = pygame.mixer.Sound("assets/{}".format(sound_name))
        sound.set_volume(0.25)
        sound.play()
        return sound

    @staticmethod
    def stop_sound(sound):
        """
        Stops the sound currently playing
        Used to better render sounds when several are played together
        """
        sound.stop()

    @staticmethod
    def play_background_music():
        """Plays a background music with pygame's mixer"""
        pygame.mixer.music.load("assets/jingle-bells.mp3")
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play()

    @staticmethod
    def pause_background_music():
        """
        Pauses the background music with pygame's mixer
        """
        pygame.mixer.music.pause()
