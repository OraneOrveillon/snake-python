from pygame.locals import *
import pygame


class Game:
    def __init__(self, window):
        self._window = window

    def draw(self):
        self._window.screen.fill((50, 50, 50))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self._window.menu.draw()
                        self._window.menu.run()
