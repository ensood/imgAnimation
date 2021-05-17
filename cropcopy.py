import cv2
import numpy

img = cv2.imread("./16.jpg",cv2.IMREAD_COLOR)
cols = int(img.shape[1] * 1)
rows = int(img.shape[0] * 1)

canvas_copy = numpy.zeros([rows,cols,3])
canvas_copy = numpy.float32(canvas_copy)

def isInArea(point):
    y = point[0]
    x = point[1]
    if 120<x<400 and 250<y<410: return True
    else: return False

for row in range(rows):
    for col in range(cols):
        if isInArea((row,col)):
            canvas_copy[row,col] = (1,1,1)#img[row,col]
"""for row in range(rows):
    for col in range(cols):
        canvas_copy[row,col]= canvas_copy[row,col].all() or img[row,col].all()
"""

canvas_copy = numpy.multiply(img,canvas_copy)
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
canvas_copy = cv2.warpAffine(canvas_copy,M,(cols,rows))
canvas_copy = numpy.multiply(img,canvas_copy)
#img = cv2.bitwise_or(img,img,canvas_copy)
cv2.imwrite("./out.jpg",canvas_copy)
