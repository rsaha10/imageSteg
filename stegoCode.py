import numpy as np
import PIL
from PIL import Image
import binascii

def userInput(msg):
    binary = '0' + '0'.join(format(ord(i), 'b') for i in msg)
    for i in range (len(binary)%8):
        print (chr(int(binary[:8],2)))
    print(len(binary))
    return binary

def encode(msg, filename):
    image = Image.open(filename)
    width, height = image.size
    totalPix =  width * height
    binary = userInput(msg)
    bitlength = len(binary)
    if (bitlength < totalPix):
        encodeBit(binary, image, width, height)
        print("Encoded")
    else:
        print("message too long or image too small")

def encodeBit(binary, image, width, height):
    imageRGB = image.convert("RGB")
    pixelRGBval = imageRGB.getpixel((10,15))
    numpy_array = np.array(image)
    for i in range(len(binary)):
        h = i%height
        w = i//height
        if (numpy_array[w][h][2]%2 != 0):
            numpy_array[w][h][2] -=1
        numpy_array[w][h][2] += int(binary[w + h])
    PIL_image = Image.fromarray(numpy_array.astype('uint8'), 'RGB')
    PIL_image.save("test.jpg")
    
def decode(filename):
    image = Image.open(filename)
    width, height = image.size
    numpy_array = np.array(image)
    binary = ""
    count = 0
##    for i in range (width):
##        for j in range (height):
##            count +=1
##            binary += str(numpy_array[i][j][2]%2)
##            if (count%8 ==0)
##    print (len(binary)%8)
##    answer = chr(int(binary, 2))
##    print (answer)
        
encode("test", "green.jpg")
decode("test.jpg")

