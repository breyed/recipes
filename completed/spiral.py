# Draw a spiral using the turtle.
# Turtle methods: https://docs.python.org/3/library/turtle.html#turtle-methods


# Import everything from the turtle module.
from turtle import *

# Do the following for 50 lines:
for line in range(50):

	# Set the turtle color such that it is black for the first (inside) line, ranging to bright red on the last (outside) line.
	color(line / 50, 0, 0)

	# Move the turtle 5 pixels times the number of the line it is drawing.
	forward(line * 5)

	# Turn the turtle to the right a fifth of the way around, plus 2 degrees.
	right(360 / 5 + 2)

# Tell the turtle that it is done drawing.
done()
