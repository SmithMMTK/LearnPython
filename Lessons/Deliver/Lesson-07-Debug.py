from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from imagelib import merge_image

# Open image file 
#image = Image.open("Lessons\images\ironman-green.jpg")
#background = Image.open("Lessons\images\sky-background.jpg")

image = Image.open("Lessons/images/ironman-green.jpg")
background = Image.open("Lessons/images/sky-background.jpg")

# Get pixel value of image
pixelData=list(image.getdata()) 
backgData=list(background.getdata()) 

# Create empty array to store RGB value and background 
rgbArray=[]
backgArray=[]

for pixel in pixelData: 
    r,g,b = pixel
    rgbArray.append((r,g,b))

for pixel_b in backgData: 
    r,g,b = pixel_b
    backgArray.append((r,g,b))
    
rgbArray = np.array(rgbArray,dtype=np.uint8)
width,height = image.size
rgbArray = rgbArray.reshape(height,width,3)

backgArray = np.array(backgArray,dtype=np.uint8)
width,height = background.size
backgArray = backgArray.reshape(height,width,3)

resultArray = merge_image(rgbArray, backgArray)

plt.subplot(1,3,1)
plt.title("original image")
plt.imshow(rgbArray)
plt.axis('off')


plt.subplot(1,3,2)
plt.title("background image")
plt.imshow(backgArray)
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Combine image")
plt.imshow(resultArray)
plt.axis('off')

plt.show()