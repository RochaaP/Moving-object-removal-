# import numpy as np
# import cv2
# import os

# cap = cv2.VideoCapture('video/1.mp4')
# framerate = cap.get(cv2.CAP_PROP_FPS)
# framecount = 0

# dirname = '1'
# os.mkdir(dirname)


# while(True):
#     # Capture frame-by-frame
#     success, image = cap.read()
#     framecount += 1

#     # Check if this is the frame closest to 10 seconds
#     if framecount == (framerate):
#         framecount = 0
#         cv2.imwrite(os.path.join(dirname, "frame%d.jpg" % framecount), image)
#         print 'Read a new frame: ', success
#       # cv2.imshow('image',image)

#     # Check end of video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#           break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

import cv2
import os

vidcap = cv2.VideoCapture('video/1.mp4')
success,image = vidcap.read()
count = 0
imcount = 0
success = True
fps = vidcap.get(cv2.CAP_PROP_FPS)
fps = int(fps)

dirname = '1'
os.mkdir(dirname)

while success:
    success,image = vidcap.read()
    if count%(fps) == 0 :
      print('read a new frame: %d '%imcount,success)
      cv2.imwrite(os.path.join(dirname, "frame%d.jpg" %imcount), image)
      imcount +=1
      # cv2.imwrite('frame%d.jpg'%count,image)
      # print('success')
    count+=1