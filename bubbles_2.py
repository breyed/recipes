# Displays bubble outlines where you click. Try to make the olympic rings.

# Before you begin, install the guizero package by entering the following commands into the terminal:
# pip3 install guizero
# pip3 install "guizero[images]"

# guizero documentation: https://lawsie.github.io/guizero


# Import App and Drawing from the guizero module. Import the random module.
from guizero import App, Drawing
import random

# Create variables to represent the application and a drawing that fills the application.

# Set the application's background to white.

# A variable to store the index of the next color within the list of colors.


# A function to get the next color in a sequence.

	# Indicate that this function uses the global color index variable.

	# Make a list of the olympic ring colors: blue, yellow, black, green, and red.

	# Create a variable for the next color.

	# Increment the color index.

	# Return the color to the caller of this function.


# A function to draw a circle at a given position and with a given radius. It should have an online with thickness 12 of the next color in the sequence.


# A function that draws a bubble where the mouse is clicked.

	# Draw a circle at the x and y position of the mouse with radius of 70.


# A function that draws a random image where the mouse is clicked.

	# Set a variable a list of image file names: ["natalie.jpg", "cauldron.jpg", "canoeing.jpg", "torch.jpg"]

	# Store a randomly selected image file name into a variable.

	# Draw the image at position x=90 and y=240.
	

# Have the application calls the draw_bubble function when the left mouse button is clicked.

# Have the application calls the draw_image function when a key is pressed.

# Display the application.
