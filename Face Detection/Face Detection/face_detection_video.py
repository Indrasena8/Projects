#importing libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Pre-Trained Frontal-Face DataSet 
face_detect = cv2.CascadeClassifier('dataset.xml')

# Open the video filee 
cap=cv2.VideoCapture('myvideo.mkv')
def detectface(frame):
    #detecting the face through the dataset and drawing a rectangle over the face co-ordinated
    face_rectangle = face_detect.detectMultiScale(frame)
    for x,y,w,h in face_rectangle:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (255,255,255),10)
    return frame

while True:
    #starting to capture the video on opening camera
    ret, frame = cap.read(0)

    #calling function to detect the front-face
    detectface(frame)

    # If you want a Gray Frame
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    cv2.imshow('Face Detection Video',frame)

    # 27 == esc button. You can use any other button like ord('q')
    # If you try to close the window pressing the x you'll get in trouble (^_^)
    if cv2.waitKey(3) & 0xFF==27:
        break

# Never forget first to release
# And then to destroy
cap.release()
cv2.destroyAllWindows()