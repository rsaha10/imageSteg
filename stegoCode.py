import numpy as np
import PIL
from PIL import Image
def userInput(msg):
    msg += "aspscv"
    binary = '0' + '0'.join(format(ord(i), 'b') for i in msg)
    count = 0
    for i in range (len(binary)//8):
        count +=1
        print("check")
        print (chr(int(binary[8*(count-1):8*count],2)))
    print(binary)
    return binary

def encode(msg, filename):
    image = Image.open(filename)
    width, height = image.size
    totalPix =  width * height
    binary = userInput(msg)
    bitlength = len(binary)
    if (bitlength < totalPix):
        numpy_array = np.array(image)
        image.close()
        encodeBit(binary, numpy_array, width, height)
        print("Encoded")
    else:
        print("message too long or image too small")

def encodeBit(binary, numpy_array, width, height):
    for i in range(len(binary)):
        h = i%height
        w = i//height
        if (numpy_array[w, h, 1]%2 != 0):
            numpy_array[w, h, 1] = numpy_array[w, h, 1] - 1
        numpy_array[w, h, 1] += int(binary[w + h])
        #print(int(binary[w + h]))
##        print ("w: ", w, "h: ", h, "value ", numpy_array[w, h, 1])
        #print(numpy_array[w][h][2])
    PIL_image = Image.fromarray(numpy_array.copy().astype(np.uint8))
    PIL_image.save("test.png")
    PIL_image.close()
##    image = Image.open("test.png")
##    newarr = np.array(image)
##    image.close()
##    for i in range(len(binary)):
##        h = i%height
##        w = i//height
##        print ("w: ", w, "h: ", h, "value ", newarr[w, h, 1])
    

def decode(filename):
    Dimage = Image.open(filename)
    width, height = Dimage.size
    numpy_array = np.array(Dimage)
    binary = ""
    answer = ""
    found = False
    for i in range(80):
        h = i%height
        w = i//height
##        print ("w: ", w, "h: ", h, "value ", numpy_array[w, h, 1])
    for w in range (width):
        if (not found):
            for h in range (height):
                binary += str(numpy_array[w][h][1]%2)
                #print(binary)
                if (len(binary)==8):
                    answer += chr(int(binary,2))
                    #print (binary)
                    #print (chr(int(binary,2)))
                    binary = ""
                if ("aspscv" in answer):
                    found = True
                    break
    print (answer[:len(answer)-6])

encode("test", "green.jpg")
decode("test.png")
