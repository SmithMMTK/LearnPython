
# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# Manipulate R, G, B pixel value of the image

# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
image=Image.open("Lessons\\Lesson-01 Image Processing\\bird.jpg")

# Get the pixel value of the image
pixel_data = list(image.getdata())

# Create an empty array to store RGB values
rgb_array = []

# Iterate through each pixel's RGB values and store in the array
for pixel in pixel_data:
    r, g, b = pixel
    r_adjusted = r * 0.7 # Reduce the red color by 30%
    b_adjusted = b * 1.3 # Increase the blue color by 30%
    rgb_array.append((r_adjusted, g, b_adjusted))

# Convert the rgb_array to a NumPy array
rgb_array = np.array(rgb_array, dtype=np.uint8)

# Reshape the array to match the original image dimensions
width, height = image.size
rgb_array = rgb_array.reshape(height, width, 3)

# Display the image using matplotlib
plt.imshow(rgb_array)
plt.axis('off')  # Turn off axis labels and ticks
plt.show()
