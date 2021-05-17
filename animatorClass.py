import cv2
import numpy
import sys
class imageAnimation():
    imgPath = ""
    def __init__(self):
        print("class is loaded successfully")

    def loadImage(self, path):
        self.imgPath = path
        image = cv2.imread(self.imgPath,cv2.IMREAD_COLOR)
        print("image path is set to: ", self.imgPath)
        return image

    def effect_draw_circular(self, image, canvas, outputFolderPath, frameCount=30,tellorance = 50, baseColor = (255,255,255)):
        rows, cols = image.shape[0], image.shape[1]
        canvas_noisy = canvas
        pts_flag = numpy.zeros([rows,cols])

        for i in range(frameCount):
            pts_unTouched_rows, pts_unTouched_cols = numpy.where(pts_flag[:][:]==0)

            index_pts_random = numpy.arange(len(pts_unTouched_rows))
            numpy.random.shuffle(index_pts_random)

            correction_steps = rows*cols//frameCount
            for step in range(correction_steps):
                j = index_pts_random[step]
                
                tB=abs(baseColor[0]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][0])
                tG=abs(baseColor[1]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][1])
                tR=abs(baseColor[2]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][2])
                if not False:#(tB<tellorance and tG<tellorance and tR<tellorance):#image[pts_unTouched_rows[j],pts_unTouched_cols[j]][2]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][0] <tellorance and image[pts_unTouched_rows[j],pts_unTouched_cols[j]][2]- image[pts_unTouched_rows[j],pts_unTouched_cols[j]][1]<tellorance:
                    #canvas_noisy[pts_unTouched_rows[j],pts_unTouched_cols[j]] = image[pts_unTouched_rows[j],pts_unTouched_cols[j]]

                    #rand_nums = numpy.random.randint(1,255,size=3)
                    color = image[pts_unTouched_rows[j],pts_unTouched_cols[j]]
                    color = (int(color[0]),int(color[1]),int(color[2]))#(int(rand_nums[0]),int(rand_nums[1]),int(rand_nums[2]))
                    #color = (0,0,255)
                    if i<3*frameCount/4: r = round((20*frameCount)//(((i+1)*1/3)**2))+1
                    else: r = round((200/(frameCount-i+1)))+1
                    """if i<5 : r = 255
                    elif i<10: r = 180
                    elif i<15: r = 120
                    elif i<20: r = 70
                    elif i<30: r = 30
                    elif i<40: r = 20
                    elif i<50: r = 13
                    elif i<55: r = 8
                    else: r = 4"""
                    
                    rand_radius = int(numpy.random.randint(0,r,size=1)[0])
                    center = (pts_unTouched_cols[j], pts_unTouched_rows[j])
                    #print(color)
                    cv2.circle(canvas_noisy, center, rand_radius, color,2)
                                
                else:
                    if step%10 == 0:
                        rand_nums = numpy.random.randint(1,255,size=3)
                        color = (int(rand_nums[0]),int(rand_nums[1]),int(rand_nums[2]))
                        rand_radius = int(numpy.random.randint(1,5,size=1)[0])
                        center = (pts_unTouched_cols[j], pts_unTouched_rows[j])
                        #print(color)
                        cv2.circle(canvas_noisy, center, rand_radius, color,2)
                #sys.stdout.write("\r{0}>".format(str(step)+" out of "+str(correction_steps)))
                #sys.stdout.flush()
                pts_flag[pts_unTouched_rows[j],pts_unTouched_cols[j]] = 1

            cv2.imwrite(outputFolderPath + str(i) + ".jpg", canvas_noisy)

            sys.stdout.write("\r{0}>".format(str(i)+" out of "+str(frameCount)))
            sys.stdout.flush()
        print("images saved to: ", outputFolderPath)
        return canvas_noisy

    def effect_draw_liniear(self, image, canvas, outputFolderPath, frameCount=30,tellorance = 50, baseColor = (255,255,255)):
        rows, cols = image.shape[0], image.shape[1]
        canvas_noisy = canvas
        pts_flag = numpy.zeros([rows,cols])

        for i in range(frameCount):
            pts_unTouched_rows, pts_unTouched_cols = numpy.where(pts_flag[:][:]==0)

            index_pts_random = numpy.arange(len(pts_unTouched_rows))
            numpy.random.shuffle(index_pts_random)

            correction_steps = rows*cols//frameCount
            for step in range(correction_steps):
                j = index_pts_random[step]
                
                tB=abs(baseColor[0]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][0])
                tG=abs(baseColor[1]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][1])
                tR=abs(baseColor[2]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][2])
                if not False:#(tB<tellorance and tG<tellorance and tR<tellorance):#image[pts_unTouched_rows[j],pts_unTouched_cols[j]][2]-image[pts_unTouched_rows[j],pts_unTouched_cols[j]][0] <tellorance and image[pts_unTouched_rows[j],pts_unTouched_cols[j]][2]- image[pts_unTouched_rows[j],pts_unTouched_cols[j]][1]<tellorance:
                    #canvas_noisy[pts_unTouched_rows[j],pts_unTouched_cols[j]] = image[pts_unTouched_rows[j],pts_unTouched_cols[j]]

                    #rand_nums = numpy.random.randint(1,255,size=3)
                    color = image[pts_unTouched_rows[j],pts_unTouched_cols[j]]
                    color = (int(color[0]),int(color[1]),int(color[2]))#(int(rand_nums[0]),int(rand_nums[1]),int(rand_nums[2]))
                    #color = (0,0,255)
                    if i<5*frameCount/6: r = round((frameCount/(i+1))*5)+1#(20*frameCount)//(((i+1)*1/3)**2))+1
                    else: r = round((200/(frameCount-i+1)))+1
                    """if i<5 : r = 255
                    elif i<10: r = 180
                    elif i<15: r = 120
                    elif i<20: r = 70
                    elif i<30: r = 30
                    elif i<40: r = 20
                    elif i<50: r = 13
                    elif i<55: r = 8
                    else: r = 4"""
                    if r<1: 
                        r =1
                        print(" r is set to: 1 ")
                    rand_dist = numpy.random.randint(0,r,size=8)
                    #print(rand_dist)
                    start = (pts_unTouched_cols[j], pts_unTouched_rows[j])
                    end = (pts_unTouched_cols[j]+int(rand_dist[0]), pts_unTouched_rows[j]+int(rand_dist[1]))
                    cv2.line(canvas_noisy, start, end, color, 2)
                    end = (pts_unTouched_cols[j]-int(rand_dist[2]), pts_unTouched_rows[j]-int(rand_dist[3]))
                    cv2.line(canvas_noisy, start, end, color, 2)
                    end = (pts_unTouched_cols[j]+int(rand_dist[4]), pts_unTouched_rows[j]-int(rand_dist[5]))
                    cv2.line(canvas_noisy, start, end, color, 2)
                    end = (pts_unTouched_cols[j]-int(rand_dist[6]), pts_unTouched_rows[j]+int(rand_dist[7]))
                    cv2.line(canvas_noisy, start, end, color, 2)

                   
                    #print(color)
                    #cv2.circle(canvas_noisy, center, rand_radius, color,2)
                                
                else:
                    if step%10 == 0:
                        rand_nums = numpy.random.randint(1,255,size=3)
                        color = (int(rand_nums[0]),int(rand_nums[1]),int(rand_nums[2]))
                        rand_radius = int(numpy.random.randint(1,5,size=1)[0])
                        center = (pts_unTouched_cols[j], pts_unTouched_rows[j])
                        #print(color)
                        cv2.circle(canvas_noisy, center, rand_radius, color,2)
                #sys.stdout.write("\r{0}>".format(str(step)+" out of "+str(correction_steps)))
                #sys.stdout.flush()
                pts_flag[pts_unTouched_rows[j],pts_unTouched_cols[j]] = 1

            cv2.imwrite(outputFolderPath + str(i) + ".jpg", canvas_noisy)

            sys.stdout.write("\r{0}>".format(str(i)+" out of "+str(frameCount)))
            sys.stdout.flush()
        print("images saved to: ", outputFolderPath)
        return canvas_noisy

    def effect_transform(self, imagesrc, image_dst, outputFolderPath, frameCount=30):
        rows, cols = imagesrc.shape[0], imagesrc.shape[1]

        pts_flag = numpy.zeros([rows,cols])

        for i in range(frameCount):
            pts_unTouched_rows, pts_unTouched_cols = numpy.where(pts_flag[:][:]==0)

            index_pts_random = numpy.arange(len(pts_unTouched_rows))
            numpy.random.shuffle(index_pts_random)

            correction_steps = rows*cols//frameCount
            for step in range(correction_steps):
                j = index_pts_random[step]
                if imagesrc[pts_unTouched_rows[j],pts_unTouched_cols[j]][2]-imagesrc[pts_unTouched_rows[j],pts_unTouched_cols[j]][0] >50 and imagesrc[pts_unTouched_rows[j],pts_unTouched_cols[j]][2]- imagesrc[pts_unTouched_rows[j],pts_unTouched_cols[j]][1]>50:
                    image_dst[pts_unTouched_rows[j],pts_unTouched_cols[j]] = imagesrc[pts_unTouched_rows[j],pts_unTouched_cols[j]]
                pts_flag[pts_unTouched_rows[j],pts_unTouched_cols[j]] = 1
            cv2.imwrite(outputFolderPath + str(i) + ".jpg", image_dst)


        print("images saved to: ", outputFolderPath)
#import main