import pygame


class Mixer:
    def __init__(self):
        """Initialize pygame's mixer"""
        pygame.mixer.init()

    @staticmethod
    def play_sound(sound_name):
        """
        Play a sound with pygame's mixer
        :param sound_name: The sound's filename
        """
        sound = pygame.mixer.Sound("assets/{}".format(sound_name))
        sound.set_volume(0.25)
        sound.play()
        return sound

    @staticmethod
    # TODO Docstring
    def stop_sound(sound):
        sound.stop()

    @staticmethod
    def play_background_music():
        """
        Play a background music with pygame's mixer
        """
        pygame.mixer.music.load("assets/jingle-bells.mp3")
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play()

    @staticmethod
    def pause_background_music():
        """
        Pause the background music with pygame's mixer
        """
        pygame.mixer.music.pause()
