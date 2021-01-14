import numpy as np
import PIL
from PIL import Image


#PIL_image.save("test.jpg")
#print (numpy_array[1][2][2])

def userInput(msg):
    binary = ''.join(format(ord(i), 'b') for i in msg)
    #print(binary)


def imageInfo(msg, filename):
    msgBits = len(msg) * 8
    width, height = Image.open(filename).size
    totalPix =  width * height
    image = Image.open(filename)
    image = Image.open(filename) #fillinfilename
    imageRGB = image.convert("RGB")
    pixelRGBval = imageRGB.getpixel((10,15))
    numpy_array = np.array(image)
    for i in range (width):
        for j in range (height):
            if (numpy_array[i][j][2]%2 != 0):
                numpy_array[i][j][2] -=1 
    PIL_image = Image.fromarray(numpy_array.astype('uint8'), 'RGB')

userInput("ABCdefg")

#def rgbValue (image):
