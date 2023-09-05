import numpy as np

def template_function(rgb_array):
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
