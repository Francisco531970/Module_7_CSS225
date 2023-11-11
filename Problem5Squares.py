# Francisco Sanchez
# 11/09/23

import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle for drawing
pen = turtle.Turtle()

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

# Set initial positions
outer_square_size_1 = 200
inner_square_size_2 = 160
inner_square_size_3 = 120
inner_square_size_4 = 80
inner_square_size_5 = 40

# Set the position for the outer square 1
pen.penup()
pen.goto(-outer_square_size_1 / 2, -outer_square_size_1 / 2)
pen.pendown()

# Draw the outer square 1
draw_square(outer_square_size_1)

# Set positions for the inner square 2
pen.penup()
pen.goto(-inner_square_size_2 / 2, -inner_square_size_2 / 2)
pen.pendown()

# Draw the inner square 2
draw_square(inner_square_size_2)

# Set positions for the inner square 3
pen.penup()
pen.goto(-inner_square_size_3 / 2, -inner_square_size_3 / 2)
pen.pendown()

# Draw the inner square 3
draw_square(inner_square_size_3)

# Draw positions for inner square 4
pen.penup()
pen.goto(-inner_square_size_4 / 2, -inner_square_size_4 / 2)
pen.pendown()

# Draw the inner square 4
draw_square(inner_square_size_4)

# Draw positions for inner square 5
pen.penup()
pen.goto(-inner_square_size_5 / 2, -inner_square_size_5 / 2)
pen.pendown()

# Draw the inner square 5
draw_square(inner_square_size_5)


# Close the window on click
screen.exitonclick()