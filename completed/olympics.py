# Displays bubble outlines where you click. Try to make the olympic rings.
# guizero documentation: https://lawsie.github.io/guizero

# Before you begin, install the guizero package by entering the following commands into the terminal:
# pip3 install guizero
# pip3 install "guizero[images]"

# Import the random module.
import random

# Import App and Drawing from the guizero module.
from guizero import App, Drawing

# Create variables to represent the application
# and a drawing that fills the application.
app = App()
drawing = Drawing(app, width=app.width, height=app.height)

# Set the application's background to white.
app.bg = "white"

# A variable to store the index of the next color within the list of colors.
color_index = 0


# A function to get the next color in a sequence.
def get_next_color():
  # Indicate that this function uses the global color index variable.
  global color_index

  # Make a list of the olympic ring colors:
  # blue, yellow, black, green, and red.
  colors = ['blue', 'yellow', 'black', 'green', 'red']

  # Create a variable for the next color.
  color = colors[color_index]

  # Increment the color index.
  color_index += 1

  # Return the color to the caller of this function.
  return color


# A function to draw a circle at a given position and with a given radius.
# It should have an outline with thickness 12 of the next color in the sequence.
def draw_circle(x, y, radius):
  drawing.oval(
    x - radius, y - radius,
    x + radius, y + radius,
    color = None,
    outline = 12,
    outline_color = get_next_color())


# A function that draws a bubble where the mouse is clicked.
def draw_bubble(event_data):

  # Draw a circle at the x and y position of the mouse with radius of 70.
  draw_circle(event_data.x, event_data.y, 70)


# A function that draws a random image where the mouse is clicked.
def draw_image():

  # Set a variable a list of image file names.
  images = ["natalie", "cauldron", "canoeing", "torch"]

  # Store a randomly selected image file name into a variable.
  image = random.choice(images)

  # Draw the image at position x=90 and y=240.
  drawing.image(90, 240, "bubbles_image_" + image + ".png")


# Have the application calls the draw_bubble function
# when the left mouse button is clicked.
app.when_left_button_pressed = draw_bubble

# Have the application calls the draw_image function when a key is pressed.
app.when_key_pressed = draw_image

# Display the application.
app.display()
