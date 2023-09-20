# Draw a city landscape with a few simple houses.
# Turtle methods: https://docs.python.org/3/library/turtle.html#turtle-methods


# Import everything from the turtle module.
from turtle import *

# Function for draw_house, which takes as input the house hight:
def draw_house(height):

	# Move the turtle the height of a house.
	forward(height)

	# Turn the turtle 90 degrees to the right.
	right(90)

	# Move the turtle 30 pixels.
	forward(30)

	# Turn the turtle 90 degrees to the right.
	right(90)

	# Move the turtle the height of the house.
	forward(height)

	# Turn the turtle 90 degrees to the left.
	left(90)

	# Move the turtle 20 pixels.
	forward(20)

	# Turn the turtle 90 degrees to the left.
	left(90)


# ---- Main part of program -----

# Use a pen with width 5.
width(5)

# Turn the turtle 90 degrees to the left.
left(90)

# Draw a house with a height of 40.
draw_house(40)

# Draw a house with a height of 120.
draw_house(120)

# Draw a house with a height of 90.
draw_house(90)

# Draw a house with a height of 20.
draw_house(20)

# Tell the turtle that it is done drawing.
done()
