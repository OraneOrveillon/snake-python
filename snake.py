import pygame
import random

import constants


class Snake:
    def __init__(self, parent_screen):
        self._length = 1
        self._speed = constants.SNAKE_SPEED
        self.parent_screen = parent_screen
        # Load the image
        self.block = pygame.image.load("resources/block.jpg").convert()
        # Initialize the coordinates with arrays -> [480, 480, 480, 480] for length == 4 and SIZE = 40
        self.x = [480] * self._length
        self.y = [400] * self._length
        # The takes a random direction
        self.direction = constants.DIRECTIONS[random.randint(0, 3)]

    def draw(self):
        """Draw a snake with x and y coordinates"""
        for i in range(self._length):
            # Draw the image at a position
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):

        for i in range(self._length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == constants.DIRECTIONS[0]:
            self.y[0] -= constants.SIZE
        if self.direction == constants.DIRECTIONS[1]:
            self.y[0] += constants.SIZE
        if self.direction == constants.DIRECTIONS[2]:
            self.x[0] -= constants.SIZE
        if self.direction == constants.DIRECTIONS[3]:
            self.x[0] += constants.SIZE

        self.draw()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def increase_length(self):
        self._length += 1
        self.x.append(-1)
        self.y.append(-1)

    @property
    def length(self):
        return self._length

    @property
    def speed(self):
        return self._speed
