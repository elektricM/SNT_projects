from turtle import *
import time

# Color letters mapping from the provided dictionary

color_letters_mapping = {}
color_letters_mapping['a'] = [ 38,  31,  29]
color_letters_mapping['b'] = [ 92,  83,  72]
color_letters_mapping['c'] = [158, 138, 113]
color_letters_mapping['d'] = [142,  34,  14]
color_letters_mapping['e'] = [231, 112,  68]
color_letters_mapping['f'] = [238, 202, 147]
color_letters_mapping['g'] = [230,  66,  55]
color_letters_mapping['h'] = [230, 177,  89]
color_letters_mapping['i'] = [114,  89,  28]
color_letters_mapping['j'] = [187,  22,  23]




# Function to draw an image using Turtle based on the color string
# Get image dimensions
width, height = 320, 240

with open('color_letters.txt', 'r') as file:
    color_string = file.read()


# Set up Turtle
screen = Screen()
screen.setup(width, height)
screen.tracer(0)

t = Turtle()
t.speed(0)
t.penup()
t.hideturtle()

y = height/2
x = -width/2
# y = -height/2
t.goto(x, y)
i = 0
while i < len(color_string):
    #print(color_string[i], end="...")
    char = color_string[i]
    count = 0
    while char.isdigit():
        count = count*10 + int(char)
        i += 1
        char = color_string[i]
    
    if count == 0:
        count = 1
    
    #print(count, end=" ")

    color = color_letters_mapping[char]
    i += 1

    #print(color[0], end=",")
    #print(color[1], end=",")
    #print(color[2], end=" ")
    t.color(color[0] / 255, color[1] / 255, color[2] / 255)
    t.goto(x, y)
    t.pendown()
    t.goto(x+count, y)
    # t.forward(count)
    t.penup()
    x += count
    if x >= width/2:
        # t.goto(-width/2, y+1)
        y -= 1
        x = -width/2
        t.goto(x, y)
        screen.update()

    #if y == height/2-10: break

screen.mainloop()
time.sleep(10)