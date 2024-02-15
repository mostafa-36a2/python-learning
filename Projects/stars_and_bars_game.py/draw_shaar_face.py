import cv2
import numpy
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
#170
#25

(480, 640)
(25,170)

a = np.array([[1, 1],
              [0, 1]])
n = 19
#3

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    print(type(frame))
    print(frame.shape)
    #frame = rgb2gray(frame)
    img = Image.fromarray(frame)
    # Convert the image to ASCII art
    #ascii_data = ascii_art.ascii_art(frame)
    # Display the ASCII art in the terminal
    
    #res = np.kron(gray, np.ones((19,3)))
    print(img.size)
    base_width= 170
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    print(img)
    print(type(img))
    img.show()
    img.save('somepic.png')
    #print(gray.shape)
    exit()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")