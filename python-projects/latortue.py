from turtle import Screen, Turtle

# Define the color letters mapping dictionary
color_letters_mapping = {
    (38, 31, 29): 'a', (142, 34, 14): 'b', (114, 89, 28): 'c', (92, 83, 72): 'd', 
    (158, 138, 113): 'e', (231, 112, 68): 'f', (230, 66, 55): 'g', (230, 177, 89): 'h', 
    (238, 202, 147): 'i', (187, 22, 23): 'j'
}

# Read the input string from the file
with open('color_letters.txt', 'r') as file:
    color_string = file.read()

# Initialize screen and turtle
screen = Screen()
screen.setup(320, 240)
screen.tracer(0)

turtle = Turtle()
turtle.speed(0)
turtle.penup()
turtle.hideturtle()

# Decode the input string and draw corresponding lines
x, y = 0, 0
for char in color_string:
    if char.isdigit():
        count = int(char)
        color = color_letters_mapping[color_string[color_string.index(char) + 1]]
        for _ in range(count):
            turtle.color(color)
            turtle.goto(x - 320 / 2, 240 / 2 - y)
            turtle.pendown()
            turtle.forward(1)
            x += 1
            if x == 320:
                x = 0
                y += 1
    else:
        color = color_letters_mapping[char]
        turtle.color(color)
        turtle.goto(x - 320 / 2, 240 / 2 - y)
        turtle.pendown()
        turtle.forward(1)
        x += 1
        if x == 320:
            x = 0
            y += 1

screen.update()
screen.mainloop()
