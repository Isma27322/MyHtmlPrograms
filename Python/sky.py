import turtle
import random

# Create turtle object
my_turtle = turtle.Turtle()

# Set initial speed and background color
my_turtle.speed(0)
turtle.bgcolor("black")

# Define colors for the stars
colors = ["white", "yellow", "cyan", "magenta", "orange", "lime", "red", "blue", "purple", "green", "pink"]

# Get the dimensions of the Turtle graphics window
window_width = turtle.window_width() // 2 - 50
window_height = turtle.window_height() // 2 - 50

# Draw stars
for _ in range(100):
    x = random.randint(-window_width, window_width)
    y = random.randint(-window_height, window_height)

    # Draw the star
    my_turtle.pendown()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.color(random.choice(colors))
    my_turtle.begin_fill()
    for _ in range(5):
        my_turtle.forward(50)
        my_turtle.right(144)
    my_turtle.end_fill()

# Hide the turtle
my_turtle.hideturtle()

# Exit on click
turtle.done()
