import pygame
from pygame.locals import *
import time

import consts
from mixer import Mixer
from text import Text
from snake import Snake
from apple import Apple


class Game:
    def __init__(self, window):
        self._window = window
        self._snake = Snake(self._window.screen)
        self._apple = Apple(self._window.screen)
        self._pause = False
        self._mixer = Mixer()

    def draw(self):
        self._mixer.play_background_music()
        self._snake.draw()
        self._apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Closed with escape key
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        if self._pause:
                            running = False
                            self._window.menu.draw()
                            self._window.menu.run()

                    # Move the snake following the direction's key
                    if not self._pause:
                        if event.key == K_UP:
                            self._snake.move_up()

                        if event.key == K_DOWN:
                            self._snake.move_down()

                        if event.key == K_LEFT:
                            self._snake.move_left()

                        if event.key == K_RIGHT:
                            self._snake.move_right()

                # Closed with the cross
                elif event.type == QUIT:
                    running = False

            if not self._pause:
                self.play()
            else:
                self.show_game_over()

            # Basically the snake's speed
            time.sleep(self._snake.speed)

    def play(self):
        self._window.screen.fill('#071A30')
        self.draw_grid()
        self._snake.walk()
        self._apple.draw()
        self.display_score()

        # If the snake's head is touching the apple
        if self._snake.is_colliding_object(self._apple.x, self._apple.y):
            # Play the sound corresponding to eating an apple
            self._mixer.play_sound("ding.mp3")
            self._snake.increase_length()
            # Move the apple and continue doing it while it is on the snake's body
            self._apple.move()
            while self._snake.is_colliding_object_body(self._apple.x, self._apple.y):
                self._apple.move()

        # If the snake's head is touching its body -> Game over
        # Starting at index 1 because the snake cannot collide its own head
        for i in range(1, self._snake.length):
            if self._snake.is_colliding_object(self._snake.x[i], self._snake.y[i]):
                # Play the sound corresponding to colliding its own body
                self._mixer.play_sound("crash.mp3")
                self._pause = True

        # If the snake's head is touching a wall -> Game over
        if self._snake.is_colliding_wall_x() or self._snake.is_colliding_wall_y():
            self._mixer.play_sound("crash.mp3")
            self._pause = True

        pygame.display.flip()

    def draw_grid(self):
        """Draw a grid on the window"""
        for i in range(0, consts.WINDOW_WIDTH, consts.BLOCK_SIZE):
            pygame.draw.line(self._window.screen, '#0E2F56', (i, 0), (i, consts.WINDOW_HEIGHT))
        for i in range(0, consts.WINDOW_HEIGHT, consts.BLOCK_SIZE):
            pygame.draw.line(self._window.screen, '#0E2F56', (0, i), (consts.WINDOW_WIDTH, i))

    def display_score(self):
        """Display the actual score on the screen"""
        text = Text(self._window.screen, 'impact', 50, "Score : {}".format(self._snake.length), '#6184E3')
        text.display_text((consts.WINDOW_WIDTH / 2 - text.width / 2, 15))

    def show_game_over(self):
        """Display the Game Over interface"""
        # Clear the surface
        self._window.screen.fill('#071A30')

        # Display the 3 texts
        game_over_text = Text(self._window.screen, consts.FONT_NAME, 50, "Game Over !", '#6184E3')
        game_over_text.display_text((consts.WINDOW_WIDTH / 2 - game_over_text.width / 2, 300))

        score_text = Text(self._window.screen, consts.FONT_NAME, 50, "Your score : {}".format(self._snake.length), '#6184E3')
        score_text.display_text((consts.WINDOW_WIDTH / 2 - score_text.width / 2, 350))

        try_again_text = Text(self._window.screen, consts.FONT_NAME, 50, "Press Enter to try again", '#6184E3')
        try_again_text.display_text((consts.WINDOW_WIDTH / 2 - try_again_text.width / 2, 400))

        pygame.display.flip()
        # Stop playing the background music
        self._mixer.pause_background_music()
