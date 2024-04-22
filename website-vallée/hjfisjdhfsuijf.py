from PIL import Image

# Encode function
def encode_pixels(image):
    width, height = image.size
    encoded_data = ""
    current_pixel = image.getpixel((0, 0))
    count = 1
    for y in range(height):
        for x in range(1, width):
            pixel = image.getpixel((x, y))
            if pixel == current_pixel:
                count += 1
            else:
                encoded_data += f"{current_pixel[0]},{current_pixel[1]},{current_pixel[2]},{count};"
                current_pixel = pixel
                count = 1
        encoded_data += f"{current_pixel[0]},{current_pixel[1]},{current_pixel[2]},{count};"  # Add remaining pixels in the row
        if y < height - 1:
            current_pixel = image.getpixel((0, y + 1))  # Move to the next row
            count = 1
    return encoded_data

# Decode function
def decode_pixels(encoded_string):
    pixel_data = []
    for pixel in encoded_string.split(";")[:-1]:
        color_r, color_g, color_b, count = map(int, pixel.split(","))
        pixel_data.extend([(color_r, color_g, color_b)] * count)
    return pixel_data

# Open the image
img = Image.open('tulipe.png')
img.convert('RGB')

# Encode the image pixels
encoded_data = encode_pixels(img)

# Save encoded data to a file
with open("encoded_image.txt", "w") as f:
    f.write(encoded_data)

# Decode the data from the file
with open("encoded_image.txt", "r") as f:
    encoded_data = f.read()

decoded_pixels = decode_pixels(encoded_data)
print(decoded_pixels[:10])  # Print first 10 decoded pixels
