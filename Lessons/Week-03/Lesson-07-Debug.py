from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open image file 
image = Image.open("Lessons\images\ironman-green.jpg")
background = Image.open("Lessons\images\sky-background.jpg")

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

####################################################################

# Create function to combine pixel between image and background
##### resultArray = rgbArray
#### 

def merge_image(rgbArray_input, backroundArray):
    
    # Create empty array that store [r,g,b] value zero with same size of rbArray_input 
    resultArray = np.zeros((len(rgbArray_input),len(rgbArray_input[0]),3),dtype=np.uint8)

    ### LINE OF CODE TO COMBINE TWO IMAGES ###
    for height in range (len(rgbArray_input)):
        for width in range (len(rgbArray_input[height])):
            r,g,b = rgbArray_input[height][width]
            if r == 20 and g == 253 and b == 74:
                resultArray[height][width] = backroundArray[height][width]
            else:
                resultArray[height][width] = rgbArray_input[height][width]

    return resultArray

####################################################################

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