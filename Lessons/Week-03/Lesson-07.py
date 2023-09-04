
# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# Create high pass filtering effect

# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
image=Image.open("Lessons\images\ironman-green.jpg")
background=Image.open("Lessons\images\sky-background.jpg")

#image=Image.open("Lessons\images\green.jpg")
#background=Image.open("Lessons\images\\blue.jpg")

# Get start date and time into variable
start_time = datetime.datetime.now()

# Get the pixel value of the image
pixel_data = list(image.getdata())
pixel_background = list(background.getdata())

# Create an empty array to store RGB values
rgb_array = []

i = -1

# Iterate through each pixel's RGB values and store in the array
for pixel in pixel_data:
    r, g, b = pixel

    # rgb(20, 253, 74)
    # Detect rgb(20, 253, 74) from pixcel data and set it to black
    if r == 20 and g == 253 and b == 74:
        # if this condition is meet, get the pixel value from the background image in same position
        #r, g, b = pixel_background[pixel_data.index(pixel)]
        r, g, b = pixel_background[i]

    if g > 200:
       # if this condition is meet, get the pixel value from the background image in same position
        #r, g, b = pixel_background[pixel_data.index(pixel)]
        r, g, b = pixel_background[i]


    rgb_array.append((r, g, b))

     # Get index value of the current pixel
    i = i + 1

    # get total pixel_data to calculate the progress in percentage in interger
    total = len(pixel_data)
    progress = (i) / total * 100

    # print progress in percentage in interger in same line for replacement of previous progress value in same line
    print(f"\rProgress: {progress:.2f}%", end="")


    #print(f"\processing pixel: {i} of {total}", end="")
          
   # print(f"\rProgress: [{'.' * int(progress // 10)}{' ' * (10 - int(progress // 10))}] {progress:.1f}%", end="")

# Get end date and time into variable
end_time = datetime.datetime.now()

# Calculate the time difference between start and end time
time_diff = end_time - start_time

# Print the time difference in seconds
print(f"\nProcessing time: {time_diff.seconds} seconds")

# Convert the rgb_array to a NumPy array
rgb_array = np.array(rgb_array, dtype=np.uint8)

# Reshape the array to match the original image dimensions
width, height = image.size
rgb_array = rgb_array.reshape(height, width, 3)

# Display the image using matplotlib
plt.imshow(rgb_array)
plt.axis('off')  # Turn off axis labels and ticks
plt.show()
