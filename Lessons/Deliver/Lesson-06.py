
# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# Remove the green background and replace with space background

# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
image=Image.open("Lessons\images\ironman-green.jpg")
background=Image.open("Lessons\images\space-background.jpg")

# Get the pixel value of the image
pixel_data = list(image.getdata())

# Create an empty array to store RGB values
rgb_array = []

# Iterate through each pixel's RGB values and store in the array
for pixel in pixel_data:
    r, g, b = pixel



    # rgb(20, 253, 74)
    # Detect rgb(20, 253, 74) from pixcel data and set it to black
    if r == 20 and g == 253 and b == 74:
        r = 0
        g = 0
        b = 0

    if g > 200:
        r = 0
        g = 0
        b = 0



    rgb_array.append((r, g, b))

# Convert the rgb_array to a NumPy array
rgb_array = np.array(rgb_array, dtype=np.uint8)

# Reshape the array to match the original image dimensions
width, height = image.size
rgb_array = rgb_array.reshape(height, width, 3)

# Display the image using matplotlib
plt.imshow(rgb_array)
plt.axis('off')  # Turn off axis labels and ticks
plt.show()
