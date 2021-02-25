''' OpenCV corner detection notes '''

### imports ### 
import numpy as np 
import cv2

''' how to detect corners in an image  '''
### read in the image file to use ### 
img = cv2.imread('/Users/cvanchieri/Documents/CS/GitHub/Repos/CS_Notes/ComputerVision_Notes/OpenCV_Notes/assets/chessboard.png')
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75) ### resize the image 
### convert a copy to greyscale ###
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grayscale for function use 
N = 100 # set number of best corners to return
### shi-Tomashi corner detector ###
# euclidian distance 
# strait line distance between 2 points
corners = cv2.goodFeaturesToTrack(gray, N, 0.01, 10) # source image, # of best corners to return, minimum quality of corners 0-1, minimum distance between 2 corners 
corners = np.int0(corners) # corners come as 'float', convert to 'int'
### draw circles at each corner ### 
for corner in corners: # loop through corners 
    x, y = corner.ravel() # flattens the array 
    ### draw a circle at each corner found ### 
    cv2.circle(img, (x, y), 8, (255, 0, 0), -1) # image to use, data point, radius, color, thickness
### draw lines between all corners ###
for i in range(len(corners)): # loop through all ther corners, 1st corner
    for j in range(i + 1, len(corners)): #  # loop through all corners + 1, 2nd corner 
        corner1 = tuple(corners[i][0]) # use interior array, start corner 
        corner2 = tuple(corners[j][0])# use interior array, end corner 
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) # generate a random color, map values, convert to tuple 
        cv2.line(img, corner1, corner2, (color), 1) # draw the lines, image, start corner, end corner, color, thinkness

cv2.imshow('Frame', img) # show the image with title 
cv2.waitKey(0) # set wait key for any key 
cv2.destroyAllWindows() # destroy all windows on key hit