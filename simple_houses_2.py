# Draw a city landscape with a few simple houses.
# Random methods: https://docs.python.org/3/library/random.html
# Turtle methods: https://docs.python.org/3/library/turtle.html#turtle-methods

# Import everything from the random module and everything from the turtle module.
import random
from turtle import *

# Function for draw_house, which takes as inputs the house hight and spacing:

	# Move the turtle the height of a house.

	# Turn the turtle 90 degrees to the right.

	# Move the turtle 30 pixels.

	# Turn the turtle 90 degrees to the right.

	# Move the turtle the height of the house.

	# Turn the turtle 90 degrees to the left.

	# Move the turtle the spacing between houses.

	# Turn the turtle 90 degrees to the left.


# Function to tell the turtle to use a random color:
def set_random_pen_color():
	color(random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']))


# ---- Main part of program -----

# Use a pen with width 5.

# Turn the turtle 90 degrees to the left (so that it starts out pointing up).

# Do the following 5 times:

	# Tell the turtle to use a random color.

	# Draw a house with a random height (from 10 to 200) and spacing (10 to 60).

# Tell the turtle that it is done drawing.
