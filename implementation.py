import cv2
import numpy as np



def makePicture(pic):
    img1 = []
    img2 = []
    row = pic[-1][0] + 1
    col = pic[-1][1] + 1
    for i in range(row):
        for j in range(col):
            index = i * col + j
            img1 += [[np.uint8(pic[index][4]), np.uint8(pic[index][3]), np.uint8(pic[index][2])]]
        img2 += [img1]
        img1 = []
    return np.array(img2)


def getTextFromFile(filename):
    file = open(filename, 'r')
    return file.read()


def getPicture(filename):
    img = cv2.imread(filename)
    lis = img.shape
    piclist = []
    row = lis[0]
    col = lis[1]
    for i in range(row):
        for j in range(col):
            pix_b = img[i][j][0]
            pix_g = img[i][j][1]
            pix_r = img[i][j][2]
            piclist += [[i, j, pix_r, pix_g, pix_b]]
    return piclist


def putDataInPixel(index, sixBinary):
    pixels[index][2] |= int(sixBinary[0:2], 2)
    pixels[index][3] |= int(sixBinary[2:4], 2)
    pixels[index][4] |= int(sixBinary[4:6], 2)


def stg(message):
    messageLength = len(message)
    messageLengthBin = bin(messageLength)[2:]
    messageLengthBin = (24 - len(messageLengthBin)) * "0" + messageLengthBin
    pixelIndex = 0
    for i in range(0, 24, 6):
        putDataInPixel(pixelIndex, messageLengthBin[i: i + 6])
        pixelIndex += 1
    messageInBin = ""
    for char in message:
        binaryStr = bin(ord(char))[2:]
        binaryStr = (8 - len(binaryStr)) * "0" + binaryStr
        messageInBin += binaryStr
        messageInBin += (6 - (len(messageInBin) % 6)) * "0"
    for i in range(0, len(messageInBin), 6):
        putDataInPixel(pixelIndex, messageInBin[i: i + 6])

def main():
    pixels = []
    pictureName = "testing.jpeg"
    messageText = getTextFromFile("message.txt")
    pixels += getPicture(pictureName)
    stg(messageText)
    cv2.imwrite('encrypted_' + pictureName, makePicture(pixels))

if __name__ == "main":
    main()