import PIL
from PIL import Image
from turtle import *

# Open the image
img = Image.open('tulipe.png')
img = img.convert('RGB')

# Get image dimensions
width, height = img.size

# Set up Turtle
screen = Screen()
screen.setup(width, height)
screen.tracer(0)

t = Turtle()
t.speed(0)
t.penup()
t.hideturtle()


# Loop through rows and draw lines for consecutive pixels of the same color
for y in range(height):
    x = 0
    while x < width:
        r, g, b = img.getpixel((x, y))
        start_x = x

        # Find the end of the segment with the same color
        while x < width and img.getpixel((x, y)) == (r, g, b):
            x += 1

        # Draw a line for the segment
        t.color(r / 255, g / 255, b / 255)
        t.penup()
        t.goto(start_x - width / 2, height / 2 - y)
        t.pendown()
        t.goto(x - width / 2, height / 2 - y)

    screen.update()

screen.mainloop()
