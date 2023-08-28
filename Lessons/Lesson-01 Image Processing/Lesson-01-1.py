
# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array

# Import the necessary packages
from PIL import Image
import numpy as np

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
image=Image.open("Lessons\\Lesson-01 Image Processing\\bird.jpg")

# Get the pixel value of the image
pixel_data = list(image.getdata())

# Create an empty array to store RGB values
rgb_array = []

# Iterate through each pixel's RGB values and store in the array
for pixel in pixel_data:
    r, g, b = pixel
    rgb_array.append((r, g, b))

# Print the RGB array
print(rgb_array)
