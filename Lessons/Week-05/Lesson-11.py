
# Create a 20x20 NumPy array with random values between 0 and 100
# Loop through the array in x, y coordinates and print the value of the array at x, y coordinates with red color
# Get average value of the surrounding cells in 3 x 3 area and store the value in blurred_image[y][x]


import numpy as np
from colorama import Fore, init

# Create a 20x20 NumPy array with random values between 0 and 100
array_20x20 = np.random.randint(0, 101, size=(20, 20))

# Loop through the array in x, y coordinates
for y in range(0, 20):
    print("[", end="")
    for x in range(0, 20):
        # Print the value of the array at x, y coordinates
        print(array_20x20[y][x],",", end=" ")
    print("]")

print("========================================")
print("Blurred Image")
print("========================================")


# Get the width and height of the image
width = len(array_20x20[0])
height = len(array_20x20)

# Create an empty array to store the blurred image
blurred_image = np.zeros((height, width), dtype=np.uint8)

# Loop through the array in x, y coordinates
for y in range(0, height):
    for x in range(0, width) :
# Loop through the array in x, y coordinates to display focus area in red
        for y1 in range(0, height) :
            for x1 in range(0, width):
                # Check if the current cell is [y][x]
                if y == y1 and x == x1:
                    # Print [y][x] in red text
                    print(f"{Fore.RED}{array_20x20[y1][x1]}{Fore.RESET}", end="  ")
                else:
                    # Print other cells in white text
                    print(f"{array_20x20[y1][x1]}", end="  ")
            print()
        print()

        # Loop surrounding cells to calculate the average value of the surrounding cells in 3 x 3 area and store the value in blurred_image[y][x]
        # Calculate the average value of the surrounding cells in 3 x 3 area
        # Store the value in blurred_image[y][x]
        
        newvalue = 0
        for ky in range(-1, 2):
            for kx in range(-1, 2):
                vy = y + ky
                vx = x + kx

                if vy < 0 or vy >= height or vx < 0 or vx >= width:
                    vx = x
                    vy = y

             #   print(f"ky = {ky}, kx = {kx}")
             #   print(f"array_20x20[{vy}][{vx}] = {array_20x20[vy][vx]}")
                newvalue += array_20x20[vy][vx]
             #   print(f"blurred_image[{y}][{x}] = {blurred_image[y][x]}")
             #   print()

        kernal_size = 9
        print(f"newvalue = {newvalue}")
        blurred_image[y][x] = newvalue / kernal_size
        print(f"blurred_image[{y}][{x}] = {blurred_image[y][x]}")
        print()


    print()
        
                    
# Loop through the array in x, y coordinates
for y in range(0, height):    
    print("[", end="")
    for x in range(0, width):
        # Print the value of the array at x, y coordinates
        print(blurred_image[y][x],",", end=" ")
    print("]")