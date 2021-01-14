import numpy

def userInput(input):
    for char in input:
        binary = ''.join(format(ord(i), 'b') for i in input)
        for power in range (7, -1, -1):
            yield 1 if binary & 2 ** power else 0


def imageInfo(input, imgName):
    msgBits = len(input) * 8


print ("yo tanzir")
