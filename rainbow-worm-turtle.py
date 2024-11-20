from turtle import *
import math

# Set up the turtle speed for faster drawing
speed(0)

#background colour

Screen().bgcolor("black")

# Function to calculate the circumference of a circle
def get_circumference(radius):
    return 2 * math.pi * radius

# List of rainbow colors
rainbow_colors = ["red", "orange", "yellow", "lightgreen", "lightblue", "blue", "purple", "magenta"]

# Function to draw an approximated circle with `n` sides
def draw_circle(n, pen_color, radius):
    color(pen_color)
    step_length = get_circumference(radius) / n  # Length of each step
    for _ in range(n):  # Loop to create `n` steps
        forward(step_length)
        left(360 / n)

# Main drawing loop for the "worm" of circles
def draw_worm(base_radius, num_circles, angle_offset, radius_decrease, inner_radius):
    current_radius = base_radius
    for i in range(num_circles):
        # Ensure the radius doesn't go below the inner boundary
        if current_radius < inner_radius:
            current_radius = inner_radius
        
        # Use modulo to cycle through rainbow colors if num_circles > len(rainbow_colors)
        color_index = i % len(rainbow_colors)
        draw_circle(40 + i, rainbow_colors[color_index], current_radius)  # Draw one circle
        
        current_radius -= radius_decrease  # Decrease the radius for the next circle
        left(angle_offset)  # Rotate for the next circle

# User inputs
radius = int(input("Please input the radius of your circle: "))
num_circles = int(input("How many circles in the worm? "))
angle_offset = int(input("What's the angle offset chief??? "))  # Angle offset between circles
radius_decrease = int(input("What should the worm shrink by each time? "))
inner_radius = int(input("What's the inner radius limit?"))

# Draw the worm
draw_worm(radius, num_circles, angle_offset, radius_decrease, inner_radius)

# Finish the drawing
done()
