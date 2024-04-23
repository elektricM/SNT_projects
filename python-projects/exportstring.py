from PIL import Image

# Open the image
try:
    img = Image.open('tulipe.png')
    img = img.convert('RGB')
except IOError:
    print("Error: Unable to load image.")
    exit(1)

# Get the dimensions of the image
width, height = img.size

# Dictionary to store colors and their assigned letters
color_letters = {}

# Counter for assigning letters
letter_counter = ord('a')

# Extract pixel data for faster processing
pixels = list(img.getdata())

# Iterate through each pixel in the image
for pixel in pixels:
    color = pixel
    # Check if the color is already assigned a letter
    if color not in color_letters:
        # Assign a new letter to the color
        color_letters[color] = chr(letter_counter)
        letter_counter += 1

# Create a string of letters representing colors in the image
color_string = ''
idx = 0
while idx < len(pixels):
    color = pixels[idx]
    color_count = 1
    while idx + color_count < len(pixels) and pixels[idx + color_count] == color:
        color_count += 1
    if color_count > 1:
        color_string += str(color_count) + color_letters[color]
    else:
        color_string += color_letters[color]
    idx += color_count

# Save the string of letters to a file
with open('color_letters.txt', 'w') as file:
    file.write(color_string)

# Output information
print("Number of colors used in the image:", len(color_letters))
print("Color letters mapping:", color_letters)
print("String of letters representing colors saved to color_letters.txt")
