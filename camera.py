import keyboard
import cv2

def take_pictures():
    for i in range(3):
        input("Tryk Enter for at tage billede")
        cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
        ret,frame = cap.read() # return a single frame in variable `frame`
        #Save the picture in "camera_pics"
        cv2.imwrite("camera_pics/pic" + str(i) + ".png", frame)

    cap.release()


