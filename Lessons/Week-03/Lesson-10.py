# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# Put the image into numpy array and process the image using numpy array
# Count color pixels in the image and plot histogram of the image

# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
image=Image.open("Lessons\images\\bird small.jpg")


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


########################################
# Function Template
########################################
def template_function(rgb_array):
    processed_data = []
    total_pixels = len(rgb_array) * len(rgb_array[0])
    print("Processing ", total_pixels, " pixels")

    # Get start date and time into variable
    start_time = datetime.datetime.now()

    # Loop through width and height of the image
    processed_pixel = 0
    for i in range(len(rgb_array)):
        for j in range(len(rgb_array[i])):
            # Get the RGB value of the pixel
            r, g, b = rgb_array[i][j]

            
            # Calculate the progress in percentage in interger
            processed_pixel = processed_pixel + 1

            # Print process in percentage in interger in same line for replacement of previous progress value in same line
            progress = processed_pixel / total_pixels * 100
            print(f"\rProgress: {progress:.2f}%", end="")
    
    # Get end date and time into variable
    end_time = datetime.datetime.now()

    # Calculate the time difference between start and end time
    time_diff = end_time - start_time

    # Print the time difference in seconds
    print(f"\nProcessing time: {time_diff.seconds} seconds")

    return rgb_array


process_pixel_data = template_function(rgb_array)

# Display the image using matplotlib
plt.imshow(rgb_array)
plt.axis('off')  # Turn off axis labels and ticks
plt.show()