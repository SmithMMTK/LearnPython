
import numpy as np
import datetime


########################################
# Create function Adjust the RGB value of rgb_array to detect the green color
########################################
def adjust_rgb_with_green(rgb_array):
    processed_data = []
    total_pixels = len(rgb_array) * len(rgb_array[0])
    print("Processing ", total_pixels, " pixels")

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

    return rgb_array


def blurImage(rgb_array):
    
    width = len(rgb_array[0])
    height = len(rgb_array)

    blurred_image = rgb_array.copy()
    total_pixels = height * width
    print("Processing ", total_pixels, " pixels")


    # Loop through width and height of the image in x, y coordinates
    processed_pixel = 0
    for y in range(0, len(rgb_array)):
        for x in range(0, len(rgb_array[y])):
            # Loop surrounding cells to calculate the average value of the surrounding cells in 3 x 3 area and store the value in blurred_image[y][x]
            # Calculate the average value of the surrounding cells in 3 x 3 area
            # Store the value in blurred_image[y][x]
            
            # Calculate the progress in percentage in interger
            processed_pixel = processed_pixel + 1

            newRedValue = 0
            newGreenValue = 0
            newBlueValue = 0
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    vy = y + ky
                    vx = x + kx

                    if vy < 0 or vy >= height or vx < 0 or vx >= width:
                        vx = x
                        vy = y
                    
                    r, g, b = rgb_array[vy][vx]

                    newRedValue +=  r
                    newGreenValue += g
                    newBlueValue += b
            
            kernal_size = 9
            blurred_image[y][x] = (newRedValue / kernal_size, newGreenValue / kernal_size, newBlueValue / kernal_size)
            # Print process in percentage in interger in same line for replacement of previous progress value in same line
            progress = processed_pixel / total_pixels * 100
            print(f"\rProgress: {progress:.2f}%", end="")

    return blurred_image