import cv2

my_input = [["", "", ""], [80, 100, 120], ""]

# Function to take picture with enter
def take_pictures():
    for i in range(3):
        pic1 = cv2.imread("pictures/temporary_pics/cam" + str(i+1) + ".png")
        cv2.imshow('image', pic1)
        cv2.waitKey(1)
        cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
        key = input("Tryk Enter for at tage billede")
        if key == "q":
            quit()
        ret,frame = cap.read() # return a single frame in variable `frame`
        #Save the picture in "camera_pics"
        cv2.imwrite("pictures/camera_pics/pic" + str(i) + ".png", frame)
    cap.release()

# Function preparing camera input to game
def prepare_input():
    name = input("Insæt holdnavn: ")
    if(name != ""):
        take_pictures()
        my_input[0][0] = "pictures/camera_pics/pic0.png"
        my_input[0][1] = "pictures/camera_pics/pic1.png"
        my_input[0][2] = "pictures/camera_pics/pic2.png"
        my_input[2] = name
    else:
        print("Insæt validt holdnavn")
        prepare_input()

    return my_input

