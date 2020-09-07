# Import Libraries
import cv2


# Take a video. 0 means the camera of my computer
cap=cv2.VideoCapture(0)


# Get the Width and Height of the Video Frame
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Top Left Corner
# We devide with // the Width and Height of the Frame
# in order to get an Integer as a Result
x=width//2
y=height//2

# Rectangle Width and Height
# 1/4 of the Actual Video Screen
w=width//4
h=height//4

# Bottom Right Corner == x + w, y + h



# It's a kind of Magic!
while True:
    ret, frame = cap.read()

    # Rectangle Frame
    cv2.rectangle(frame,(x,y),
                 (x+w, y+h),
                 color=(255,0,255),
                 thickness=5)
    
    # Show it
    cv2.imshow('frame',frame)
    
    # 27 == esc button. You can use any other button like ord('q')
    # If you try to close the window pressing the x you'll get in trouble (^_^)
    if cv2.waitKey(3) & 0xFF == 27:
        break
    
    
# Never forget first to release
# And then to destroy
cap.release()
cv2.destroyAllWindows()
