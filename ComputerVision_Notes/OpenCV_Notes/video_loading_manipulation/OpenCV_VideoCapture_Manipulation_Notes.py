### imports ### 
import numpy as np
import cv2

''' capture a video & loading a video''' 
# must use local terminal, vscode did not work
### initiate the video capture ### 
cap = cv2.VideoCapture(0) # represents which camera to use, takes hold of camera 
# cap = cv2.VideoCapture('filename') # name of the mp4 video to use 
### loop until a key is hit ###
while True:
  ret, frame = cap.read() # read() returns frame(np array of image), ret tells if it worked properly
  cv2.imshow('frame', frame) # give image name and frame data
  
  if cv2.waitKey(1) == ord('q'): # wait 1ms, if the 'q' is hit break loop 
    break

cap.release() # releases the use of the camera 
cv2.destroyAllWindows() # closes all windows once done


''' 4 quadrants from a video, rotate a quadrant ''' 
### initiate the video capture ### 
cap = cv2.VideoCapture(0) # represents which camera to use, takes hold of camera 
# cap = cv2.VideoCapture('filename') # name of the mp4 video to use 
### loop until a key is hit ###
while True:
  ret, frame = cap.read() # read() returns frame(np array of image), ret tells if it worked properly
  width = int(cap.get(3)) # get(3) gets width, default come in float must change
  height = int(cap.get(4)) # get(4) gets height, default come in float must change
  image = np.zeros(frame.shape, np.uint8) # fills array with zeros, pass in shape wanted = to frame shape, type of data
  smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # create smaller frame, reduce size by fractions
  image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # can rotate image in size is same 
  image[height//2:, :width//2] = smaller_frame # slicing for location and size, bottom left,  add smaller_frame
  image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # can rotate image in size is same 
  image[height//2:, width//2:] = smaller_frame # slicing for location and size, bottom right, add smaller_frame
  cv2.imshow('frame', image) # give image name and frame data

  if cv2.waitKey(1) == ord('q'): # wait 1ms, if the 'q' is hit break loop 
    break

cap.release() # releases the use of the camera 
cv2.destroyAllWindows() # closes all windows once done


