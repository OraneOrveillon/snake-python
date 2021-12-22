import pygame


class Mixer:
    def __init__(self):
        """Initialize pygame's mixer"""
        pygame.mixer.init()

    @staticmethod
    def play_sound(sound):
        """
        Play a sound with pygame's mixer
        :param sound: The sound's filename
        """
        sound = pygame.mixer.Sound("resources/{}.mp3".format(sound))
        pygame.mixer.Sound.play(sound)

    @staticmethod
    def play_background_music():
        """
        Play a background music with pygame's mixer
        """
        pygame.mixer.music.load("resources/jingle-bells.mp3")
        pygame.mixer.music.play()