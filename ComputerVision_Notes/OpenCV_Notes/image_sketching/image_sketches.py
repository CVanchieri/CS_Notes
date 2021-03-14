import cv2

color_image = cv2.imread("images/cryptokitty.jpeg")
cartoon_image = cv2.stylization(color_image, sigma_s=150, sigma_r=0.25)  
sketch_image1, sketch_image2 = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
#cv2.imshow('cartoon', cartoon_image)
cv2.imshow('pencil', sketch_image1)
#cv2.imshow('pencil', sketch_image2)
cv2.waitKey()  
cv2.destroyAllWindows() 