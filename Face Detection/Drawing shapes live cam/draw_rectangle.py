# Import Library
import cv2

# Callback Function for the Mouse, Rectangle
def draw_rectangle(event,
                  x,
                  y,
                  flags,
                  param):
    
    # write your global params.  
    # Check the Project Computer Vision - Image Basics with OpenCV and Python
    # to get an idea how you can do it
    # pt1, pt2, tope_left_clicked, bottom_right_clicked
    global pt1, pt2, top_left_clicked, bottom_right_clicked
    
    # Create an event for Left Button Down and assigned it to event
    if event == cv2.EVENT_LBUTTONDOWN:

        # Reset your Rectangle
        if top_left_clicked == True and bottom_right_clicked==True:
            # Give 0 values to pt1 & pt2
            pt1=(0,0)
            pt2=(0,0)

            # Give False value to your Trackers
            top_left_clicked=False
            bottom_right_clicked=False

    # Check the top_left_clicked if it's False
    if top_left_clicked==False:
        pt1=(x,y)
        top_left_clicked=True


            # Check the bottom_right_clicked if it's False
    elif bottom_right_clicked==False:
        pt2=(x,y)
        bottom_right_clicked=True
    
    
    
# pt1, pt2 Global Variables
pt1=(0,0)
pt2=(0,0)



# Trackers are False
top_left_clicked=False
bottom_right_clicked=False


# Take a video
cap=cv2.VideoCapture(0)


# Create a Named Window for the Connections
cv2.namedWindow('Test')


# Set a Mouse Callback
cv2.setMouseCallback('Test',draw_rectangle)


# Time for Magic
while True:
    
    # Capture the frame
    ret, frame=cap.read()
    
    # Based on the Global Variables Draw the Frame
    if top_left_clicked==True:
        cv2.circle(frame,
                  center=pt1,
                  radius=5,
                  color=(255,0,255),
                  thickness=-1)
    
        # Draw a Circle on the Frame
    if top_left_clicked == True and bottom_right_clicked==True:
        cv2.rectangle(frame,
                     pt1,
                     pt2,
                     (0,0,255),
                     3)
        
    # Show the Frame
    cv2.imshow('Test',frame)
    
    # 27 == esc button. You can use any other button like ord('q')
    # If you try to close the window pressing the x you'll get in trouble (^_^)
    if cv2.waitKey(3) & 0xFF == 27:
        break
    
    
# Never forget first to release
# And then to destroy   
cap.release()
cv2.destroyAllWindows()


