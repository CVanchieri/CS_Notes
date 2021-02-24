
''' OpenCV Drawing '''
 # lines 
 # images 
 # circles
 # text 

### imports ### 
import numpy as np 
import cv2

''' drawing capabilities, lines, shapes, text ''' 
### initiate the video capture ### 
cap = cv2.VideoCapture(0) # represents which camera to use, takes hold of camera 
# cap = cv2.VideoCapture('filename') # name of the mp4 video to use 
### loop until a key is hit ###
while True:
  ret, frame = cap.read() # read() returns frame(np array of image), ret tells if it worked properly
  width = int(cap.get(3)) # get(3) gets width, default come in float must change
  height = int(cap.get(4)) # get(4) gets height, default come in float must change
  ### draw a line ### 
  img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10) # image to use, starting coord, ending coord, color, thickness 
  img = cv2.line(img, (0,height), (width, 0), (0, 255, 0), 5) # image to use, starting coord, ending coord, color, thickness 
  ### draw a rectangle ###
  img = cv2.rectangle(img, (100, 100), (200, 200) ,(128, 128, 128), (5)) # image to use, starting coord, ending coord, color, thickness 
  ### draw a circle ### 
  img = cv2.circle(img, (300, 300), 60, (0, 0, 255), (-1)) # image to use, center position, radius, color, thickness(-1 fill)
  ### draw text ### 
  # create font first 
  font = cv2.FONT_HERSHEY_SIMPLEX
  img = cv2.putText(img, 'Keep it up!!!', (300, height - 200), font, 4, (0, 0, 0), 3, cv2.LINE_AA) # image to use, text to place, bottom right coord, font, scale for font size, color, thickness(-1 fill), use for best look
  cv2.imshow('frame', img) # give image name and frame data

  if cv2.waitKey(1) == ord('q'): # wait 1ms, if the 'q' is hit break loop 
    break

cap.release() # releases the use of the camera 
cv2.destroyAllWindows() # closes all windows once done