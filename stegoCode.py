import numpy

def userInput(input):
    binary = ''.join(format(ord(i), 'b') for i in input)
    print(binary)


def imageInfo(input, imgName):
    msgBits = len(input) * 8

userInput("ABCdefg")
