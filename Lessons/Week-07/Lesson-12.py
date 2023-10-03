# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# Put the image into numpy array and process the image using numpy array

# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
import myimagelib as myimg


# Define the path of the image file
image_path = os.path.join("Lessons","images", "bird small.jpg")

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
image=Image.open(image_path)

#image=Image.open("Lessons\images\green.jpg")


# Get the pixel value of the image
pixel_data = list(image.getdata())

# Create an empty array to store RGB values
rgb_array = []

i = -1

# Iterate through each pixel's RGB values and store in the array
print("Load image")
for pixel in pixel_data:
    r, g, b = pixel
    rgb_array.append((r, g, b))



# Convert the rgb_array to a NumPy array
rgb_array = np.array(rgb_array, dtype=np.uint8)


# Reshape the array to match the original image dimensions
print("Reshape image")
width, height = image.size
rgb_array = rgb_array.reshape(height, width, 3)


process_pixel_data = myimg.blurImage(rgb_array)

# Display the image using matplotlib
plt.subplot(1, 2, 1)
plt.imshow(rgb_array)
plt.axis('off')  # Turn off axis labels and ticks

plt.subplot(1, 2, 2)
plt.imshow(process_pixel_data)
plt.axis('off')  # Turn off axis labels and ticks

plt.show()