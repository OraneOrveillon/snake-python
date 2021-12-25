"""The size of one snake's block and an apple --> a square of side x"""
BLOCK_SIZE = 48
"""
Coefficients used for the window's dimensions
HAS TO BE AN EVEN NUMBER
"""
WIDTH_COEFFICIENT = 20
LENGTH_COEFFICIENT = 18
"""Window's dimensions, always are a multiple of BLOCK_SIZE thanks to the coefficients above"""
WINDOW_WIDTH = WIDTH_COEFFICIENT * BLOCK_SIZE
WINDOW_LENGTH = LENGTH_COEFFICIENT * BLOCK_SIZE
"""The snake's move speed"""
SNAKE_SPEED = 0.075
"""The 4 directions taken by the snake"""
DIRECTIONS = ('up', 'down', 'left', 'right')


