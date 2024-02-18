import cv2
import numpy as np

edges = [
    [0, 0, 0, 0, 2, 3, 3, 0, 0, 0],
    [0 ,1, 1, 0, 2, 3, 3, 0, 0, 0],
    [0 ,1, 1, 0, 4, 5, 5, 0, 0, 0],
    [0 ,0, 0, 0, 4, 5, 5, 0, 0, 0],
    [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 3, 3, 0, 0, 0],
    [0 ,1, 1, 0, 2, 3, 3, 0, 0, 0],
    [0 ,1, 1, 0, 4, 5, 5, 0, 0, 0],
    [0 ,0, 0, 0, 4, 5, 5, 0, 0, 0],
    [0 ,0, 0, 0, 0, 0, 0, 0, 0, 8],
]
#https://stackoverflow.com/questions/10346336/list-of-lists-into-numpy-array
edges = np.vstack(edges)

#https://stackoverflow.com/questions/49390112/opencv-error-215-depth-cv-8u-depth-cv-16u-depth-cv-32f-in-func
edges = np.uint8(edges)

(numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(edges, 4 , cv2.CV_32S)
print(numLabels)#Number of labels
print(labels)#The image, but as labels
print(stats)#[left, top, width, height, STAT_AREA]
print(centroids)