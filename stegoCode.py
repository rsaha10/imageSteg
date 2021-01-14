import numpy as np
import PIL
from PIL import Image

filename = "green.jpg"
width, height = Image.open(filename).size
totalPix =  width * height


image = PIL.Image.open(filename) #fillinfilename
imageRGB = image.convert("RGB")
pixelRGBval = imageRGB.getpixel((10,15))

numpy_array = np.array(image)
print (numpy_array)

def userInput(input):
    binary = ''.join(format(ord(i), 'b') for i in input)
    #print(binary)


def imageInfo(input, imgName):
    msgBits = len(input) * 8

userInput("ABCdefg")

#def rgbValue (image):
