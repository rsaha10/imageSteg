import numpy as np
import PIL
from PIL import Image

def userInput(msg):
    binary = ''.join(format(ord(i), 'b') for i in msg)
    
    #print(binary)

def imageInfo(msg, filename):
    image = Image.open()
    width, height = image.size
    totalPix =  width * height
    binary = userInput(msg)
    bitlength = len(binary)
    if (bitlength + 48 < totalPix):
        encode(binary, image)

userInput("ABCdefg")

def encode (binary, image):
    imageRGB = image.convert("RGB")
    pixelRGBval = imageRGB.getpixel((10,15))
    numpy_array = np.array(image)
    #print (numpy_array[1][2][2])
    for i in range (width):
        for j in range (height):
            if (numpy_array[i][j][2]%2 != 0):
                numpy_array[i][j][2] -=1 
    PIL_image = Image.fromarray(numpy_array.astype('uint8'), 'RGB')
    #PIL_image.save("test.jpg")
