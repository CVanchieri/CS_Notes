''' OpenCV object detection (template matching) notes '''

### imports ### 
import numpy as np 
import cv2 

''' locate an object in an image '''
### read in the image file to use ### 
# sizing must be the same 
img = cv2.imread('/Users/cvanchieri/Documents/CS/GitHub/Repos/CS_Notes/ComputerVision_Notes/OpenCV_Notes/assets/soccer_practice.jpg', 0) # 0 for grayscale
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75) ### resize the image 
template = cv2.imread('/Users/cvanchieri/Documents/CS/GitHub/Repos/CS_Notes/ComputerVision_Notes/OpenCV_Notes/assets/shoe.png', 0) # 0 for grayscale
# template = cv2.imread('/Users/cvanchieri/Documents/CS/GitHub/Repos/CS_Notes/ComputerVision_Notes/OpenCV_Notes/assets/ball.png', 0) # 0 for grayscale
template = cv2.resize(template, (0,0), fx=0.75, fy=0.75) ### resize the image 
height, width = template.shape
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
        cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods: # loop through each method
    img2 = img.copy() # copy image to draw the rectangle 

    result = cv2.matchTemplate(img2, template, method) # 2d array showing rough match in each region
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) # returns min max for values and locations
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: # these methods take min values 
        location = min_loc # set min loc
    else:
        location = max_loc # set max loc
    
    bottom_right = (location[0] + width, location[1] + height) # set the sizing the rectangle
    cv2.rectangle(img2, location, bottom_right, 255, 5) # image, rectangle corner locations, color, thickness
    cv2.imshow('match', img2) # show the image with title 
    cv2.waitKey(0) # set wait key for any key 
    cv2.destroyAllWindows() # destroy all windows on key hit


