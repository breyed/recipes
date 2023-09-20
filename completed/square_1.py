# https://github.com/breyed/recipes

# Draw a square using the turtle.
# Turtle methods: https://docs.python.org/3/library/turtle.html#turtle-methods


# Import everything from the turtle package.
from turtle import *

# Use a blue pen.
color('blue')

# Do the following for 4 sides:
for line in ['top', 'right', 'bottom', 'left']:

	# Move the turtle 200 pixels.
	forward(200)

	# Turn the turtle 90 degrees to the right.
	right(90)

# Tell the turtle you're done.
done()
