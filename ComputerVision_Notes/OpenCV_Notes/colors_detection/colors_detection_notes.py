
''' OpenCV colors detection notes '''

### imports ### 
import numpy as np 
import cv2

'''  extract a color from an image ''' 
### initiate the video capture ### 
cap = cv2.VideoCapture(0) # represents which camera to use, takes hold of camera 
# cap = cv2.VideoCapture('filename') # name of the mp4 video to use 
### loop until a key is hit ###
while True:
  ret, frame = cap.read() # read() returns frame(np array of image), ret tells if it worked properly
  width = int(cap.get(3)) # get(3) gets width, default come in float must change
  height = int(cap.get(4)) # get(4) gets height, default come in float must change
  ### convert BGR image to HSV ### 
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert image to HSV
  ### convert your own colors ### 
  # bgr_color = np.array([[[255, 0, 0]]])
  # x = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV) # convert image to HSV
  # x[0][0]
  ### define colors for extraction, set range ### 
  lower_blue = np.array([90, 50, 50]) # set lower color 
  upper_blue = np.array([130, 255, 255]) # set upper color 
  ### create a mask ### 
  mask = cv2.inRange(hsv, lower_blue, upper_blue) # image to use, colors range, which pixels to keep 
  result = cv2.bitwise_and(frame, frame, mask=mask) # comparing bits from image to bits of mask, if true keep 

  cv2.imshow('frame', result) # give image name and frame data

  if cv2.waitKey(1) == ord('q'): # wait 1ms, if the 'q' is hit break loop 
    break

cap.release() # releases the use of the camera 
cv2.destroyAllWindows() # closes all windows once done