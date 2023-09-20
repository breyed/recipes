# Draw a city landscape filled with fancy houses.
# Turtle methods: https://docs.python.org/3/library/turtle.html#turtle-methods


# Import everything from the random module and everything from the turtle module.
import random
from turtle import *

# Function for draw_flat_roof:

	# Turn the turtle 90 degrees to the right.

	# Move the turtle 30 pixels.

	# Turn the turtle 90 degrees to the right.


# Function for draw_pointy_roof:

	# Turn the turtle 45 degrees to the right.

	# Move the turtle 20 pixels.

	# Turn the turtle 90 degrees to the right.

	# Move the turtle 20 pixels.

	# Turn the turtle 45 degrees to the right.


# Function for draw_house, which takes as input the house hight:

	# Tell the turtle to use a random color.

	# Move the turtle the height of a house.

	# If the current height is greater than 55, then:

		# Draw a flat roof.

	# Otherwise:

		# Draw a pointy roof.

	# Move the turtle the height of the house.

	# Turn the turtle 90 degrees to the left.

	# Tell the graphics window to use a green pen.

	# Move the turtle 20 pixels.

	# Turn the turtle 90 degrees to the left.


# Function to tell the turtle to use a random color:
def set_random_pen_color():
	color(random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']))


# ---- Main part of program -----

# Use a pen with width 5.

# Draw houses with heights of 50, 120, 20, 60, 40, 80, 20, 105, and 70 pixels

# Tell the turtle that it is done drawing.
