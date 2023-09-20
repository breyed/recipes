# Draw a pair of differently colored squares using the turtle.
# Turtle methods: https://docs.python.org/3/library/turtle.html#turtle-methods


# Import everything from the turtle module.
from turtle import *

# Use a pen with width 5.
width(5)

# Use a red pen.
color('red')

# Do the following for 4 sides:
for line in ['top', 'right', 'bottom', 'left']:

	# Move the turtle 200 pixels.
	forward(200)

	# Turn the turtle 90 degrees to the right.
	right(90)

# Make the turtle turn around.
left(180)

# Use a green pen.
color('green')

# Do the following for 3 sides:
for line in ['top', 'left', 'bottom']:

	# Move the turtle 200 pixels.
	forward(200)

	# Turn the turtle 90 degrees to the left.
	left(90)

# Tell the turtle you're done.
done()