import PIL
from PIL import Image
from turtle import *


def resize_and_reduce_colors(image_path, new_height=240, target_width=320, target_height=240, num_colors=10):
    # Open the image
    img = Image.open(image_path)
    
    # Resize image to new height
    ratio = new_height / img.size[1]
    img = img.resize((int(img.size[0] * ratio), new_height))
    
    # Crop the image to target width and height
    left = (img.size[0] - target_width) / 2
    top = (img.size[1] - target_height) / 2
    right = (img.size[0] + target_width) / 2
    bottom = (img.size[1] + target_height) / 2
    img = img.crop((left, top, right, bottom))
    
    # Convert image to RGB if it's grayscale
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Reduce number of colors
    img = img.quantize(colors=num_colors)
    
    return img

# Set up Turtle
screen = Screen()
screen.tracer(0)

t = Turtle()
t.speed(0)
t.penup()
t.hideturtle()

# Process the image
processed_img = resize_and_reduce_colors('tulipe.jpg')

# Get image dimensions
width, height = processed_img.size

# Scale down the image to fit within the turtle window
scale_factor = max(width, height) / max(screen.window_width(), screen.window_height())

# Loop through rows and draw lines for consecutive pixels of the same color
for y in range(height):
    x = 0
    while x < width:
        color_index = processed_img.getpixel((x, y))
        if isinstance(color_index, int):  # For grayscale images
            r, g, b = color_index, color_index, color_index
        else:
            r, g, b = color_index
        start_x = x

        # Find the end of the segment with the same color
        while x < width and processed_img.getpixel((x, y)) == color_index:
            x += 1

        # Draw a line for the segment
        t.color(r / 255, g / 255, b / 255)
        t.penup()
        t.goto(start_x - width / 2, height / 2 - y)
        t.pendown()
        t.goto(x - width / 2, height / 2 - y)

    screen.update()

screen.mainloop()
