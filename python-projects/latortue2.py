import turtle

# Color letters mapping from the provided dictionary
color_letters_mapping = {
    'a': (38, 31, 29),
    'b': (92, 83, 72),
    'c': (158, 138, 113),
    'd': (142, 34, 14),
    'e': (231, 112, 68),
    'f': (238, 202, 147),
    'g': (230, 66, 55),
    'h': (230, 177, 89),
    'i': (114, 89, 28),
    'j': (187, 22, 23)
}

# Function to draw an image using Turtle based on the color string
def draw_image_from_color_string(color_string):
    turtle.setup(width=320, height=240)  # Set up Turtle screen size
    turtle.speed(0)  # fastest drawing speed
    turtle.hideturtle()
    
    width, height = 300, 240  # image dimensions
    
    x = 0
    y = 0

    while y < height:
        x = 0
        while x < width:
            char = color_string[0]
            if char.isdigit():  # check if the character is a digit (represents pixel count)
                pixel_count = int(char)
                color_letter = color_string[1]
                color_string = color_string[2:]  # remove processed characters from color_string
            else:
                pixel_count = 1
                color_letter = char
                color_string = color_string[1:]  # remove processed character from color_string

            if color_letter in color_letters_mapping:
                r, g, b = color_letters_mapping[color_letter]
                turtle.color(r / 255, g / 255, b / 255)  # set Turtle color

                start_x = x
                end_x = min(x + pixel_count, width)  # calculate end of segment within image width

                # Draw a line segment for the current color segment
                turtle.penup()
                turtle.goto(start_x - width / 2, height / 2 - y)
                turtle.pendown()
                turtle.goto(end_x - width / 2, height / 2 - y)

                x += pixel_count  # move x to the end of the processed segment
        y += 1  # move to the next row

    turtle.done()

# Read color string from the text file
def read_color_string_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            color_string = file.read().strip()
        return color_string
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

if __name__ == "__main__":
    # Specify the path to the color string text file
    file_path = 'color_letters.txt'

    # Read the color string from the text file
    color_string = read_color_string_from_file(file_path)

    if color_string:
        # Draw the image based on the color string
        draw_image_from_color_string(color_string)
