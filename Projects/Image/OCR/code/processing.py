import cv2
import time,sys,os
import numpy as np
from pathlib import Path

#creates a figure with 10 (width) x 5 (height) inches
np.set_printoptions(threshold=sys.maxsize)

directory='../'
index_you_want = -1#-1 for all
index_currently = 1
enable_img_show = False

def read_and_resize(file_path):
    img = cv2.imread(file_path)
    img = cv2.resize(img, (640,640), interpolation = cv2.INTER_AREA)
    if enable_img_show:
        cv2.imshow('Original Image',img)
        cv2.waitKey(0)
    return img

def gray(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if enable_img_show:
        cv2.imshow('Gray Image',img_gray)
        cv2.waitKey(0)
    return img_gray

def edge_detection(img_blur):
    #3- Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    if enable_img_show:
        cv2.imshow('Sobel X on Image',sobelx)
        cv2.waitKey(0)

    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    if enable_img_show:
        cv2.imshow('Sobel Y on Image',sobely)
        cv2.waitKey(0)

    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    if enable_img_show:
        cv2.imshow('Sobel XY on Image',sobelxy)
        cv2.waitKey(0)

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
    edges = cv2.dilate(edges, kernel)
    if enable_img_show:
        cv2.imshow('Canny Edge Detection',edges)
        cv2.waitKey(0)
    
    return edges

def blur(img_gray):
    #3- Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    #img_blur=img_gray
    if enable_img_show:
        cv2.imshow('Gaussian Blur Image',img_blur)
        cv2.waitKey(0)
    return img_blur

def show_labels_gradually(labels):
    for i in range(0, numLabels):
        if i<2:
            componentMask = (labels == i).astype("uint8") * 255
        else:
            componentMask += (labels == i).astype("uint8") * 255

        componentMaskRGB = cv2.cvtColor(componentMask.astype("uint8"),cv2.COLOR_GRAY2BGR)
        if enable_img_show:
            cv2.imshow(f'componentMask', componentMaskRGB)
            cv2.waitKey(0)

def draw_needed(numLabels,stats,labels):
    # loop over the number of unique connected component labels######################Looooop
    for i in range(0, numLabels):
        
        #enable_img_show = i%15==0
        
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        
        LENGTH = areas[i]
        AREA = w*h
        RATIO = LENGTH/AREA
        float_id = i/numLabels
        
        if RATIO < 0.03:
            print('Processing ',i,' Discard due to LENGTH/AREA ratio=',RATIO)
            continue
            
        if not (areas[i]>character_low_limit_area and areas[i]<character_high_limit_area):
            #print('Processing ',i,' Discard:',areas[i])
            continue
        
        #print('Processing ',i)
        #print("->",needed_counter,"/",needed,"/area=",stats[i, cv2.CC_STAT_AREA])

        # construct a mask for the current connected component by
        # finding a pixels in the labels array that have the current
        # connected component ID

        labels_i = (labels == i).astype("uint8")
        #length = np.sum(sum(labels_i)) #this equals area[i]
        
        componentMask = labels_i * 255
        
        contours, hierarchy  = cv2.findContours(componentMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #print(contours)
        cv2.drawContours(output, contours, -1, (255,255,255), 5)
        
        #componentMask = cv2.cvtColor(componentMask,cv2.COLOR_GRAY2BGR)
        
        edges_comononent = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
        edges_comononent[:,:,1]=componentMask
        
        cv2.putText(edges_comononent, str(needed_counter) , (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(edges_comononent, "length="+str(LENGTH)+", area="+str(AREA)+" rat: "+format(RATIO,".2f") , (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        output[:,:,1] |= (labels_i * int(255*RATIO))
        
        if enable_img_show:
            cv2.imshow('componentMask', edges_comononent)
        #cv2.rectangle(output, (x, y),((x + w),(y + h)),(255, 255, 255), -1)
        #cv2.circle(output, (int(centroids[i][0]), int(centroids[i][1])), 1, (0, 255, 255), 5)    
        
        #output[:,:,2]+= (labels_i * int(255*RATIO))
        #output[:,:,1]+= (labels_i * int(255*RATIO))
        #output[:,:,0]+= (labels_i * int(255*RATIO))
        
        #cv2.putText(output, str(needed_counter) , (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # show our output image and connected component mask
        #output = cv2.resize(output, (640,640), interpolation = cv2.INTER_AREA)
        
        cv2.rectangle(componentMask, (30, 20),(150,20),(255, 255, 255), -1)
        cv2.putText(output, 'output:'+str(i) , (30,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, int(255*float_id),int((1-float_id)*255)), 2, cv2.LINE_AA)
        
        if enable_img_show:
            #cv2.imshow('output', output)
            cv2.imshow('Image',output)
            cv2.waitKey(0)

        #https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python
        cv2.imwrite('/home/mostafa/Documents/OCR/compare_original_with_processed/{}{}.jpg'.format(Path(filename).stem,'_original'), img)
        cv2.imwrite('/home/mostafa/Documents/OCR/compare_original_with_processed/{}{}.jpg'.format(Path(filename).stem,'_processed'), output)

        needed_counter=needed_counter+1
# Main
for filename in os.listdir(directory):
    print(f"Processing {filename}")
    if index_you_want!=-1:
        if index_you_want!=index_currently:
            index_currently+=1
            continue
        index_currently+=1
    
    #ignore non images
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        continue

    file_path=os.path.join(directory, filename)
    
    #1- Read the original image
    img = read_and_resize(file_path)
    
    img_gray = gray(img)
    
    img_blur = blur(img_gray)

    edges = edge_detection(img_blur)
    
    (numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(edges, 4 , cv2.CV_32S)
    
    labels_rgb = cv2.cvtColor(labels.astype("uint8"),cv2.COLOR_GRAY2BGR)
    if enable_img_show:
        cv2.imshow('labels_colored',labels_rgb)
        cv2.waitKey(0)

    show_labels_gradually(labels)
            
    areas = stats[:, cv2.CC_STAT_AREA]
    
    #output = img.copy()
    output = cv2.cvtColor(img_blur, cv2.COLOR_GRAY2BGR)
    if enable_img_show:
            #cv2.imshow('output', output)
            cv2.imshow('Output Image',output)
            cv2.waitKey(0)
    
    #Separate letters based on componenet area
    img_width =  min(img.shape[0],img.shape[1])
    character_low_limit_area=(img_width/200)*(img_width/200)
    character_high_limit_area=(img_width/10)*(img_width/10)
    needed = sum(
        map(lambda x : x>character_low_limit_area and x<character_high_limit_area, stats[:,cv2.CC_STAT_AREA])
        )

    print("needed=",needed," numLabels=",numLabels)

    needed_counter=0
    
    draw_needed()
    
    #output now is filled with whites
    output=output>250
    output=output.astype("uint8") *255
    print("output.shape=",output.shape)
    output=255-img*output
    output_file = '/home/mostafa/Documents/OCR/compare_original_with_processed/{}{}.jpg'.format(Path(filename).stem,'_final')
    cv2.imwrite(output_file, output)
    print(f"output_file: {output_file}")
    output = cv2.resize(output, (512,512), interpolation = cv2.INTER_AREA)
    if enable_img_show:
        #cv2.imshow('output', output)
        cv2.imshow('Image',output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
    exit()
    #End processing file
