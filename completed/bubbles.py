# Displays bubbles where you click.

# Before you begin, install the guizero package by entering the following command into the terminal:
# pip3 install guizero

# guizero documentation: https://lawsie.github.io/guizero


# Import App and Drawing from the guizero module. Import the random module.
from guizero import App, Drawing
import random


# Create variables to represent the application and a drawing that fills the application.
app = App()
drawing = Drawing(app, width=app.width, height=app.height)


# A function to get a random color.
def get_random_color():
	return random.choice(['red', 'blue', 'green'])


# A function to draw a circle at a given position and with a given radius and a random color.
def draw_circle(x, y, radius):
	drawing.oval(x - radius, y - radius, x + radius, y + radius, color = get_random_color())


# A function that draws a bubble where the mouse is clicked.
def draw_bubble(event_data):

	# Set a radius to be a random integer from 10 to 60.
	radius = random.randint(10, 60)

	# Draw a circle at the x and y position of the mouse with the random radius.
	draw_circle(event_data.x, event_data.y, radius)


# Have the application calls the draw_bubble function when the left mouse button is clicked.
app.when_left_button_pressed = draw_bubble

# Display the application.
app.display()
