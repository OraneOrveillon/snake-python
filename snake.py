import pygame
import random

import constants


class Snake:
    """The object that the player is going to control"""
    def __init__(self, parent_screen):
        """
        - Start with a length of 1 and the speed defined in constants.py
        - Load the snake image
        - Initialize it's first coordinates x, y at the middle of the screen
        - Start at a random direction
        :param parent_screen: The parent window
        """
        self._length = 1
        self._speed = constants.SNAKE_SPEED
        self.parent_screen = parent_screen
        # Load the image
        self.block = pygame.image.load("resources/blue-ball.png").convert_alpha()
        # Initialize the coordinates with arrays -> [528, 528, 528, 528] for length == 4 and SIZE = 48
        self.x = [528] * self._length
        self.y = [384] * self._length
        self.direction = constants.DIRECTIONS[random.randint(0, 3)]

    def draw(self):
        """Draw all snake's blocks at corresponding positions"""
        for i in range(self._length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        """Change the snake's direction to up"""
        self.direction = constants.DIRECTIONS[0]

    def move_down(self):
        """Change the snake's direction to down"""
        self.direction = constants.DIRECTIONS[1]

    def move_left(self):
        """Change the snake's direction to left"""
        self.direction = constants.DIRECTIONS[2]

    def move_right(self):
        """Change the snake's direction to right"""
        self.direction = constants.DIRECTIONS[3]

    def walk(self):
        """
        Increase the snake's length and change its block's position
        Each block takes the position of the previous one
        Redraw it with the new coordinates
        """
        for i in range(self._length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == constants.DIRECTIONS[0]:
            self.y[0] -= constants.BLOCK_SIZE
        if self.direction == constants.DIRECTIONS[1]:
            self.y[0] += constants.BLOCK_SIZE
        if self.direction == constants.DIRECTIONS[2]:
            self.x[0] -= constants.BLOCK_SIZE
        if self.direction == constants.DIRECTIONS[3]:
            self.x[0] += constants.BLOCK_SIZE

        self.draw()

    def increase_length(self):
        """Increase the snake's length by 1"""
        self._length += 1
        self.x.append(-1)
        self.y.append(-1)

    # ---------- GETTERS / SETTERS SPACE ---------- #
    @property
    def length(self):
        return self._length

    @property
    def speed(self):
        return self._speed
