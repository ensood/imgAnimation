import animatorClass
import cv2
import numpy

anim = animatorClass.imageAnimation()

img = cv2.imread("./16.jpg",cv2.IMREAD_COLOR)
width = int(img.shape[1] * 1)
height = int(img.shape[0] * 1)
dim = (width, height)
 

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
rows, cols = img.shape[0], img.shape[1]
canvas_noisy = numpy.random.randint(255,size = (rows,cols,3))
canvas_noisy = numpy.float32(canvas_noisy)
#canvas_noisy = anim.effect_draw_circular( img,canvas_noisy,  "./out/",100,80,(50,50,200))
canvas_noisy = anim.effect_draw_liniear( img,canvas_noisy,  "./out/",90,80,(50,50,200))
#anim.effect_transform( img,image_dst,  "./out/") #changed comment