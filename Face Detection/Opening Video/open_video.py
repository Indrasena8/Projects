# Import Libraries
import cv2


# Open the video from the previous lesson
cap=cv2.VideoCapture('myvideo.mkv')



# In case we wrote the path wrong
if cap.isOpened() == False:
    print('Error! Check your file path')



# Some Magic!
while cap.isOpened():
    ret, frame = cap.read()
    
    if ret==True:
    # We wrote it with 20 FPS on the previous lesson
    # So, we need a delay of 1/20 if we want to see it
    # Uncomment the line below if you want to see it
    # time.sleep(1/20)
    
    
        # Show it
        cv2.imshow('frame',frame)

        # 27 == esc button. You can use any other button like ord('q')
        # If you try to close the window pressing the x you'll get in trouble (^_^)
        if cv2.waitKey(15) & 0xFF==27:
            break
    
    
# Never forget first to release
# And then to destroy
cap.release()
cv2.destroyAllWindows()
