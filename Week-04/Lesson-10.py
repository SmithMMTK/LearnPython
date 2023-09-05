# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# Put the image into numpy array and process the image using numpy array
# Count color pixels in the image and plot histogram of the image

# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
#image=Image.open("Lessons\images\\bird small.jpg")
image=Image.open("Lessons\images\\ironman-green.jpg")

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
def gethistogram(rgb_array, color):

    if color not in ['r', 'g', 'b']:
        raise ValueError("Invalid color parameter. Use 'r', 'g', or 'b'.")

    # Create histogram array with 256 elements and initialize with 0
    histogram = np.zeros(256, dtype=np.uint32)

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

            if color == 'r':
                histogram[r] = histogram[r] + 1
            elif color == 'g':
                histogram[g] = histogram[g] + 1
            elif color == 'b':
                histogram[b] = histogram[b] + 1
            
            # Calculate the progress in percentage in interger
            processed_pixel = processed_pixel + 1

            # Print process in percentage in interger in same line for replacement of previous progress value in same line
            progress = processed_pixel / total_pixels * 100
            print(f"\rProgress: {color} : {progress:.2f}%", end="")
    
    # Get end date and time into variable
    end_time = datetime.datetime.now()

    # Calculate the time difference between start and end time
    time_diff = end_time - start_time

    # Print the time difference in seconds
    print(f"\nProcessing time: {time_diff.seconds} seconds")

    return histogram


processed_histogram_red = gethistogram(rgb_array,'r')
processed_histogram_green = gethistogram(rgb_array,'g')
processed_histogram_blue = gethistogram(rgb_array,'b')

# Display the image using matplotlib
plt.subplot(1, 4, 1)
plt.imshow(rgb_array)
plt.axis('off')  # Turn off axis labels and ticks


# Display the image histogram using matplotlib
plt.subplot(1, 4, 2)
# Create histogram graph from processed_histogram_data
plt.hist(processed_histogram_red, bins=256, range=(0, 256), color='red', alpha=0.4)
plt.title('Histogram Red')
plt.xlabel('Color value')
plt.ylabel('Pixels')
plt.xlim([0, 256])


# Display the image histogram using matplotlib
plt.subplot(1, 4, 3)

# Create histogram graph from processed_histogram_data
plt.hist(processed_histogram_green, bins=256, range=(0, 256), color='green', alpha=0.4)
plt.title('Histogram Green')
plt.xlabel('Color value')
plt.ylabel('Pixels')
plt.xlim([0, 256])

# Display the image histogram using matplotlib
plt.subplot(1, 4, 4)

# Create histogram graph from processed_histogram_data
plt.hist(processed_histogram_blue, bins=256, range=(0, 256), color='blue', alpha=0.4)
plt.title('Histogram Blue')
plt.xlabel('Color value')
plt.ylabel('Pixels')
plt.xlim([0, 256])

plt.show()