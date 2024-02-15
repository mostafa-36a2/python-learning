import cv2
import asciimatics
from asciimatics.effects import BannerText, Print
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to the grayscale image
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    
    # Convert the thresholded image to ASCII art
    #ascii_art = cv2.convert_to_ascii(thresh)
    Print(screen, ImageFile( IMG_COWBOY, screen.height - 2,
								colours=screen.colours),
								0,
								stop_frame = 200 )
    Screen.wrapper
    
    # Display the ASCII art
    print(ascii_art)
    
    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()
cv2.destroyAllWindows()