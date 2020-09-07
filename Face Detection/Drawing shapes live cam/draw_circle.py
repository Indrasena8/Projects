# Import Library
import cv2

# Callback Function for the Mouse, Circle
def draw_circle(event,
               x,
               y,
                flags,
                param):
    global center, clicked


    # Get the Mouse Click Down & Up
    # and Track the Center
    if event==cv2.EVENT_LBUTTONDOWN:
        center=(x,y)
        clicked=False
        
    if event==cv2.EVENT_LBUTTONUP:
        clicked=True
    
    
# Zero Drawing of the Circle
center=(0,0)
clicked=False


# Take a video
cap=cv2.VideoCapture(0)


# Create a Named Window for the Connections
cv2.namedWindow('Testing')

# Bind our Function with the Mouse Clicks
cv2.setMouseCallback('Testing',draw_circle)


# Time for Magic
while True:
    
    
    # Capture the frame
    ret, frame=cap.read()
    
    # Check if Clicked is True
    if clicked:
    
        # Draw a Circle on the Frame
        cv2.circle(frame,
                  center=center,
                  radius=50,
                  color=(255,0,255),
                  thickness=3)
        
    # Display the Frame
    cv2.imshow('Testing',frame)
    
    # 27 == esc button. You can use any other button like ord('q')
    # If you try to close the window pressing the x you'll get in trouble (^_^)
    if cv2.waitKey(3) & 0xFF==27:
        break
    
    
# Never forget first to release
# And then to destroy   
cap.release()
cv2.destroyAllWindows()


