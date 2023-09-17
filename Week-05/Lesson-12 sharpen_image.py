# Basic image sharpening concept

import numpy as np

def sharpen_image(rgb_array):
    processed_data = []

    # Create 3 x 3 kernel for sharpening
    kernel = [[-1, -1, -1],
              [-1,  9, -1],
              [-1, -1, -1]]
    
    # Get the width and height of the image
    width = len(rgb_array[0])
    height = len(rgb_array)

    # Create an empty array to store the sharpened image
    sharpened_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Apply the sharpening filter
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            for c in range(3):  # Loop through RGB channels
                value = 0
                for ky in range(3):
                    for kx in range(3):
                        value += rgb_array[y + ky - 1][x + kx - 1][c] * kernel[ky][kx]
                sharpened_image[y][x][c] = max(0, min(value, 255))

    return sharpened_image

# Generate a 20x20 RGB array for debugging
width = 20
height = 20
rgb_array = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the array with random RGB values
for y in range(height):
    for x in range(width):
        rgb_array[y, x, 0] = np.random.randint(0, 256)  # Red channel
        rgb_array[y, x, 1] = np.random.randint(0, 256)  # Green channel
        rgb_array[y, x, 2] = np.random.randint(0, 256)  # Blue channel

print("Generated RGB Array:")
processed_data = sharpen_image(rgb_array)



'''
Let's break down the line value += rgb_array[y + ky - 1][x + kx - 1][c] * kernel[ky][kx] step by step:

value: This variable keeps track of the value that will be used to calculate the intensity of the sharpened pixel at position [y, x] and RGB channel c.

rgb_array[y + ky - 1][x + kx - 1][c]: This part of the code retrieves the color value of the original image at a specific pixel. y and x represent the current pixel's coordinates, while ky and kx are loop variables that iterate over the 3x3 kernel. Subtracting 1 from ky and kx is done to align the kernel with the pixel in the image. This way, the kernel's center matches the current pixel's position.

kernel[ky][kx]: This part of the code retrieves the corresponding weight from the sharpening kernel. The weight indicates how much influence the neighboring pixel's color should have on the final sharpened pixel's color. The center weight is 9, and the surrounding weights are -1.

Multiplication: We multiply the color value from the original image (rgb_array) with the weight from the kernel (kernel[ky][kx]). This operation essentially amplifies or reduces the color contribution based on the weight.

value += ...: This is an accumulator operation. It adds up the calculated weighted color values for all surrounding pixels in the 3x3 kernel around the current pixel. The loop iterates through all combinations of ky and kx, computing the weighted contribution from each neighboring pixel and accumulating it in the value variable.

sharpened_image[y][x][c] = max(0, min(value, 255)): Once we've accumulated the weighted color values from all surrounding pixels, we assign the result to the corresponding pixel in the sharpened image (sharpened_image). However, we ensure that the final value is within the valid color range of 0 to 255 by using the max(0, min(value, 255)) function.

In simpler terms, this line of code takes a central pixel, considers the color values of its neighboring pixels, and multiplies each color value with a weight from the kernel. The result is accumulated, and the accumulated value is used to set the color of the sharpened pixel, making the image look sharper.

Feel free to use analogies like baking or mixing colors to help the kid understand the concept of weighted contributions and how the kernel enhances the image.
'''