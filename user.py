from camera import take_pictures
import keyboard

my_input = [["", "", ""], [80, 100, 120], ""]

def prepare_input():
    # print("Insæt holdnavn og tryk enter: ")
    # recorded = keyboard.record(until='enter')
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
