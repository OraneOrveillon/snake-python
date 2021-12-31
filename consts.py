"""FIle containing all necessary constants for the project"""

"""The size of one snake's block and an apple --> a square of side x"""
BLOCK_SIZE = 48
"""
Coefficients used for the window's dimensions
HAS TO BE AN EVEN NUMBER
"""
WIDTH_COEFFICIENT = 20
HEIGHT_COEFFICIENT = 18
"""Window's dimensions, always are a multiple of BLOCK_SIZE thanks to the coefficients above"""
WINDOW_WIDTH = WIDTH_COEFFICIENT * BLOCK_SIZE
WINDOW_HEIGHT = HEIGHT_COEFFICIENT * BLOCK_SIZE
"""The snake's move speed"""
SNAKE_SPEED = 0.075
"""The 4 directions taken by the snake"""
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
# TODO Docstring
BUTTON_WIDTH = BLOCK_SIZE * 8
BUTTON_HEIGHT = BLOCK_SIZE * 2
BUTTON1_Y = BLOCK_SIZE * 5
BUTTON2_Y = BLOCK_SIZE * 9
BUTTON3_Y = BLOCK_SIZE * 13

BUTTON_COLOR = 'white'
BUTTON_FONT_NAME = 'impact'
BUTTON_FONT_SIZE = 50
BUTTON_FONT_COLOR = 'black'
SELECTED_BUTTON_COLOR = 'grey'
SELECTED_BUTTON_FONT_COLOR = 'white'


