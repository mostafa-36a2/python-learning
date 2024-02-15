"""
pytesseract.image_to_string
"""
import cv2
import numpy as np
import pytesseract
img = cv2.imread("../01_ocr_perfect.jpg")
print(img.shape)

scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
text = pytesseract.image_to_string(resized)
print('pytesseract text ',text)
print('Resized Dimensions : ',resized.shape)

cv2.imshow("resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()