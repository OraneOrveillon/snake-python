import pygame
from pygame.locals import *
import time

from snake import Snake
from apple import Apple
from mixer import Mixer
from text import Text
import constants


class Game:
    """Deal with the functional aspects of the game"""

    def __init__(self):
        """
        - Create a mixer and start playing background music
        - Initialize pygame library
        - Create the window with its dimensions
        - Create and draw an snake and an apple
        """
        self._mixer = Mixer()
        self._mixer.play_background_music()
        pygame.init()
        self._window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_LENGTH))
        self._snake = Snake(self._window)
        self._snake.draw()
        self._apple = Apple(self._window)
        self._apple.draw()

    def run(self):
        """Keep the game running until the game over state or when the window is closed"""
        # Keep the window running until it is closed
        # Moves the blocks when a direction key is pressed
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Closed with escape key
                    if event.key == K_ESCAPE:
                        running = False
                    # Restart the game
                    if event.key == K_RETURN:
                        # Restart the music
                        self._mixer.play_background_music()
                        # Un pause the game
                        pause = False

                    # Move the snake following the direction's key
                    if not pause:
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

            try:
                if not pause:
                    self.play()
            except Exception:
                self.show_game_over()
                pause = True
                self.reset()

            # Basically the snake's speed
            time.sleep(self._snake.speed)

    def play(self):
        """
        The snake moves forwards by 1 and the background is cleared each time this function is called
        Called continuously in run()
        Check for snake's collisions :
            - length++ and move the apple if colliding the apple
            - game over if colliding its body or a wall"""
        self.render_background()
        self._snake.walk()
        self._apple.draw()
        self.display_score()
        pygame.display.flip()

        # If the snake's head is touching the apple
        if self._snake.is_colliding_object(self._apple.x, self._apple.y):
            # Play the sound corresponding to eating an apple
            self._mixer.play_sound("ding")
            # Increasing snake's length and continue moving
            self._snake.increase_length()
            # Move the apple and continue doing it while it is on the snake's body
            self._apple.move()
            while self._snake.is_colliding_object_body(self._apple.x, self._apple.y):
                self._apple.move()

        # If the snake's head is touching its body -> Game over
        # Starting at index 1 because the snake cannot collide its ows head
        for i in range(1, self._snake.length):
            if self._snake.is_colliding_object(self._snake.x[i], self._snake.y[i]):
                # Play the sound corresponding to colliding its own body
                self._mixer.play_sound("crash")
                raise Exception("Collision Occurred")

        # If the snake's head is touching a wall -> Game over
        if self._snake.is_colliding_wall_x() or self._snake.is_colliding_wall_y():
            self._mixer.play_sound("crash")
            raise Exception("Collision Occurred")

    def render_background(self):
        """Regenerate the background at 0,0 position"""
        background = pygame.image.load("resources/background.jpg")
        self._window.blit(background, (0, 0))
        # Single color background (temporary)
        self._window.fill((7, 26, 48))

    def display_score(self):
        """Display the actual score on the screen"""
        text = Text(self._window, 'impact', 50, "Score : {}".format(self._snake.length), (97, 132, 227))
        text.display_text((constants.WINDOW_WIDTH / 2 - text.width / 2, 15))

    def show_game_over(self):
        """Display the Game Over interface"""
        # Clear the surface
        self.render_background()

        # Display the 3 texts
        game_over_text = Text(self._window, 'impact', 50, "Game Over !", (97, 132, 227))
        game_over_text.display_text((constants.WINDOW_WIDTH / 2 - game_over_text.width / 2, 300))

        score_text = Text(self._window, 'impact', 50, "Your score : {}".format(self._snake.length), (97, 132, 227))
        score_text.display_text((constants.WINDOW_WIDTH / 2 - score_text.width / 2, 350))

        try_again_text = Text(self._window, 'impact', 50, "Press Enter to try again", (97, 132, 227))
        try_again_text.display_text((constants.WINDOW_WIDTH / 2 - try_again_text.width / 2, 400))

        # Update the window
        pygame.display.flip()
        # Stop playing the background music
        self._mixer.pause_background_music()

    def reset(self):
        """Restart the game"""
        # Recreate a new snake and a new apple
        self._snake = Snake(self._window)
        self._apple = Apple(self._window)
