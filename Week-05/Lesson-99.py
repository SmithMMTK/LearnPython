
# Read jpg image and get R, G, B pixel value of the image and store in 2 dimensional array
# # Replace green background with sky background
# Put the image into numpy array and process the image using numpy array
# Appy Gussian blur to the image

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
# Create a function to apply Gaussian blur to an image
########################################
def apply_gaussian_blur(image, kernel_size):
    height, width, channels = image.shape
    blurred_image = np.zeros((height, width, channels), dtype=np.uint8)
    
    # Get Total pixel of the image
    total_pixels = height * width
    print("Processing: ", total_pixels, " pixels")

    padding = kernel_size // 2  # Padding size
    sigma = 1.0  # Gaussian standard deviation
    
    # Loop through width and height of the image
    processed_pixel = 0
    
    for i in range(padding, height - padding):
        for j in range(padding, width - padding):
            for c in range(channels):
                total = 0
                weight_sum = 0
                for ki in range(-padding, padding + 1):
                    for kj in range(-padding, padding + 1):
                        weight = np.exp(-(ki**2 + kj**2) / (2 * sigma**2))
                        total += image[i + ki, j + kj, c] * weight
                        weight_sum += weight
                
                blurred_image[i, j, c] = int(total / weight_sum)
        
        # Calculate the progress in percentage in integer
        processed_pixel += width - 2 * padding  # Counting processed pixels in the current row

        # Print process in percentage in interger in same line for replacement of previous progress value in same line
        progress = processed_pixel / total_pixels * 100
        print(f"\rProgress: {progress:.2f}%", end="")

    return blurred_image

kernel_size = 5  # Kernel size for Gaussian blur

# Apply Gaussian blur to the processed pixel data
blurred_image = apply_gaussian_blur(rgb_array , kernel_size)
 # Print process in percentage in interger in same line for replacement of previous progress value in same line
progress = 100
print(f"\rProgress: {progress:.2f}%", end="")

# Display the original and blurred images side by side using matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(rgb_array )
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(blurred_image)
plt.title('Blurred Image')
plt.axis('off')

plt.tight_layout()
plt.show()