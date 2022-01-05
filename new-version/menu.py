import pygame
from pygame.locals import *

import consts
from mixer import Mixer
from text import Text
from button import Button


class Menu:
    def __init__(self, window):
        self._window = window

        self._buttons = (Button(self._window.screen,
                                consts.WINDOW_WIDTH / 2 - consts.BUTTON_WIDTH / 2,
                                consts.BUTTON1_Y,
                                "PLAY"),
                         Button(self._window.screen,
                                consts.WINDOW_WIDTH / 2 - consts.BUTTON_WIDTH / 2,
                                consts.BUTTON2_Y,
                                "SETTINGS"),
                         Button(self._window.screen,
                                consts.WINDOW_WIDTH / 2 - consts.BUTTON_WIDTH / 2,
                                consts.BUTTON3_Y,
                                "SCORES")
                         )

        self._selected_button = 0
        self._buttons[self._selected_button].set_selected()

        self._mixer = Mixer()

    def draw(self):
        # Set background
        self._window.screen.fill("#A04C76")

        # Set title
        title = Text(self._window.screen, 'impact', 150, "Snake", 'black')
        title.display_text((consts.WINDOW_WIDTH / 2 - title.width / 2, 20))

        # Set buttons
        for i in range(len(self._buttons)):
            self._buttons[i].draw()

    def run(self):
        running = True
        switch_sound = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Closed with escape key
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        if self._selected_button > 0:
                            if switch_sound:
                                self._mixer.stop_sound(switch_sound)
                            switch_sound = self._mixer.play_sound("button-switch.wav")
                            self._buttons[self._selected_button].set_selected()
                            self._selected_button -= 1
                            self._buttons[self._selected_button].set_selected()
                    if event.key == K_DOWN:
                        if self._selected_button < len(self._buttons) - 1:
                            if switch_sound:
                                self._mixer.stop_sound(switch_sound)
                            switch_sound = self._mixer.play_sound("button-switch.wav")
                            self._buttons[self._selected_button].set_selected()
                            self._selected_button += 1
                            self._buttons[self._selected_button].set_selected()
                    if event.key == K_RETURN:
                        if self._selected_button == 0:
                            running = False
                            self._window.game.draw()
                            self._window.game.run()
                elif event.type == QUIT:
                    running = False
