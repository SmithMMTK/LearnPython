import numpy as np

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