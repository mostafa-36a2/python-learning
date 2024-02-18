import cv2
import numpy as np

#https://www.youtube.com/watch?v=FbR9Xr0TVdY    
image = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0 ,0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0 ,0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0 ,0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0 ,1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0 ,1, 0, 1, 0, 0, 1, 1, 1, 0],
    [0 ,1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#https://stackoverflow.com/questions/10346336/list-of-lists-into-numpy-array
image = np.vstack(image)

#https://stackoverflow.com/questions/49390112/opencv-error-215-depth-cv-8u-depth-cv-16u-depth-cv-32f-in-func
image = np.uint8(image)

image = image * 255

image_RGB = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
cv2.imshow('image_RGB', image_RGB)
cv2.waitKey(0)

contours, hierarchy  = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

res = cv2.drawContours(image_RGB,contours,-1,(0,255,0),1)

#cv2.cvtColor(image_RGB,cv2.COLOR_GRAY2BGR)
cv2.imshow('image_RGB', image_RGB)
cv2.waitKey(0)

print(image)
print(f"Number of contours: {len(contours)}")
print(contours)
print(hierarchy)