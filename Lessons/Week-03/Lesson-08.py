from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Open the image files
print("Load image")
image = Image.open("Lessons/images/ironman-green.jpg")
background = Image.open("Lessons/images/sky-background.jpg")

# Resize the background image to match the dimensions of the input image
background = background.resize(image.size)

# Convert images to NumPy arrays
print("Convert images to NumPy arrays")
rgb_array = np.array(image, dtype=np.uint8)
rgb_array_background = np.array(background, dtype=np.uint8)

def adjust_rgb_with_green(rgb_array, rgb_array_background):
    start_time = datetime.datetime.now()

    # Define color thresholds for detecting green
    green_threshold = np.array([20, 253, 74])  # Adjust the green threshold to match your image
    
    # Create mask to identify green pixels
    green_mask = np.all(rgb_array == green_threshold, axis=-1)
    
    # Create mask to identify pixels with green value greater than 160
    high_green_mask = rgb_array[:, :, 1] > 160
    
    # Combine both masks
    replace_mask = green_mask | high_green_mask
    
    # Replace pixels based on the combined mask
    rgb_array[replace_mask] = rgb_array_background[replace_mask]
    
    # Calculate the processing time
    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    print(f"Processing time: {time_diff.seconds} seconds")

    return rgb_array

processed_data = adjust_rgb_with_green(rgb_array, rgb_array_background)

# Display the processed image using matplotlib
plt.imshow(processed_data)
plt.axis('off')
plt.show()
