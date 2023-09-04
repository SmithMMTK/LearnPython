
# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array


# Import the necessary packages
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the image file name "bird.jpg" from the subfolder "Lessons\Lesson-01 Image Processing"
# image=Image.open("Lessons\\Lesson-01 Image Processing\\bird.jpg")
image=Image.open("Lessons/images/bird small.jpg")

# Get the pixel value of the image
pixel_data = list(image.getdata())

# Create an empty array to store RGB values
rgb_array = []


# Adjust the RGB values of each pixel with the average RGB values of its neighbors
def adjust_rgb_with_neighbors(pixel_data):
    processed_data = []
    total_pixels = len(pixel_data)

    for i in range(len(pixel_data)):
        if i < 5 or i >= len(pixel_data) - 5:
            processed_data.append(pixel_data[i])  # Keep edge pixels unchanged
        else:
            avg_r = sum(pixel[0] for pixel in pixel_data[i - 5 : i + 6]) / 11
            avg_g = sum(pixel[1] for pixel in pixel_data[i - 5 : i + 6]) / 11
            avg_b = sum(pixel[2] for pixel in pixel_data[i - 5 : i + 6]) / 11
            
            new_pixel = (
                int(avg_r),
                int(avg_g),
                int(avg_b)            
            )

            

             # Calculate progress percentage and print dots
            progress = (i + 1) / total_pixels * 100
            print(f"\rProgress: [{'.' * int(progress // 10)}{' ' * (10 - int(progress // 10))}] {progress:.1f}%", end="")

            processed_data.append(new_pixel)


    return processed_data

# Adjust the RGB values of each pixel with the average RGB values of its neighbors
process_pixel_data = adjust_rgb_with_neighbors(pixel_data)

# Iterate through each pixel's RGB values and store in the array
for pixel in process_pixel_data:
    r, g, b = pixel
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