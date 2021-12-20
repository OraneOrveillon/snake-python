import pygame

import constants


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        # Load the image
        self.block = pygame.image.load("resources/block.jpg").convert()
        # Initialize the coordinates with arrays -> [40, 40, 40, 40] for length == 4
        self.x = [constants.SIZE] * length
        self.y = [constants.SIZE] * length
        self.direction = 'down'

    def draw(self):
        """Draw a snake with x and y coordinates"""
        for i in range(self.length):
            # Draw the image at a position
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= constants.SIZE
        if self.direction == 'down':
            self.y[0] += constants.SIZE
        if self.direction == 'left':
            self.x[0] -= constants.SIZE
        if self.direction == 'right':
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
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
