# Import Libraries
import cv2

# Open the system camera 
cap = cv2.VideoCapture(0)

#Mentioning the width and height of the camera window
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
output=cv2.VideoWriter('myvideo.mkv',
                       cv2.VideoWriter_fourcc(*'DIVX'),
                       20,
                       (width, height))
while True:
    ret, frame=cap.read()
    
    # Operations
    output.write(frame)
    
    # Show it
    
    # If you want a Gray Frame
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    cv2.imshow('frame',frame)
    # 27 == esc button. You can use any other button like ord('q')
    # If you try to close the window pressing the x you'll get in trouble (^_^)
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Never forget first to release
# And then to destroy
cap.release()
output.release()
cv2.destroyAllWindows()