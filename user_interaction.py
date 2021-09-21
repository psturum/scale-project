import cv2

my_input = [["", "", ""], [80, 100, 120], ""]

# Function to take picture with enter
def take_pictures():
    for i in range(3):
        input("Tryk Enter for at tage billede")
        cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
        ret,frame = cap.read() # return a single frame in variable `frame`
        #Save the picture in "camera_pics"
        cv2.imwrite("camera_pics/pic" + str(i) + ".png", frame)

    cap.release()

# Function preparing camera input to game
def prepare_input():
    name = input("Insæt holdnavn: ")
    if(name != ""):
        take_pictures()
        my_input[0][0] = "camera_pics/pic0.png"
        my_input[0][1] = "camera_pics/pic1.png"
        my_input[0][2] = "camera_pics/pic2.png"
        my_input[2] = name
    else:
        print("Insæt validt holdnavn")
        prepare_input()

    return my_input

