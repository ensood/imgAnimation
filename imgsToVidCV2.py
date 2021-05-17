
import numpy as np
import cv2
import moviepy.editor as mpe
import imageio

pathIn= './out/'
pathOut = './out/alimahtabkian10.mp4'
fps = 10
frame_array = []
#size = (220,266)
numberOfFrames =89
print("starting")
for i in range(1,numberOfFrames+1):
    if i<numberOfFrames:
        img = cv2.imread(pathIn+''+str(i)+'.jpg', cv2.IMREAD_UNCHANGED)
        #img = img//64+64//2
        #img = imageio.read(pathIn+'image'+str(i)+'.jpg')


        #print(i)
        height, width, layers = img.shape
        size = (width,height)
        frame_array.append(img)
        if i%101 ==0: print("(N): %Loading imgs: ", str(int(i*100/numberOfFrames)))
#kargs = { 'duration': 0.06}
#imageio.mimsave('./out/output.gif', frame_array, 'GIF', **kargs)
print("(N): loading image writer..")
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'MP4V'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
    if i%10 ==0: print("(N): %Writing frames to output video: ", str(int(i*100/numberOfFrames)))
out.release()
"""
#audio
clip = []
clip.append(mpe.VideoFileClip(pathOut))
final_clip =  mpe.concatenate_videoclips(clip)
audio_background = mpe.AudioFileClip('./imgs_s1/1.mp3')
final_clip = final_clip.set_audio(audio_background)
final_clip.set_duration(15).write_videofile("./imgs_s1/outputAudio.mp4",fps=fps)
"""