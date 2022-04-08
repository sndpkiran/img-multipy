import cv2 as cv
import math
import numpy as np
import time

imgsize = (1000, 1000) #The size of the image

image = np.zeros((1000,1000,3), np.uint8) #Create the image

innerColor = [243,161,131] #Color at the center
outerColor = [236,111,102] #Color at the corners

for y in range(imgsize[1]):
    for x in range(imgsize[0]):

        #Find the distance to the center
        distanceToCenter = math.sqrt((x - imgsize[0]/2) ** 2 + (y - imgsize[1]/2) ** 2)

        #Make it on a scale from 0 to 1
        distanceToCenter = float(distanceToCenter) / (math.sqrt(2) * imgsize[0]/2)

        #Calculate r, g, and b values
        r = outerColor[0] * distanceToCenter + innerColor[0] * (1 - distanceToCenter)
        g = outerColor[1] * distanceToCenter + innerColor[1] * (1 - distanceToCenter)
        b = outerColor[2] * distanceToCenter + innerColor[2] * (1 - distanceToCenter)

        #Place the pixel
        image[x][y] = (int(b), int(g), int(r))

cv.imwrite('gradient_' + str(int(time.time())) +'.jpg', image)