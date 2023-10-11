
# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# Create high pass filtering effect

# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"

mage=Image.open("Lessons/images/bird.jpg")

# Get the pixel value of the image
pixel_data = list(image.getdata())

# Create an empty array to store RGB values
rgb_array = []

# Iterate through each pixel's RGB values and store in the array
for pixel in pixel_data:
    r, g, b = pixel

    # Create high pass filtering effect, if the pixel value is less than 128, set it to 0, otherwise set it as original value
    # Set high pass threshold as 128
    high_pass_threshold = 128

    if r < high_pass_threshold :
        r = 0
    else:
        r = r
    if g < high_pass_threshold :
        g = 0
    else:
        g = g
    if b < high_pass_threshold :
        b = 0
    else:
        b = b

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
