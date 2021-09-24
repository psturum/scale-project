# Initializing scoreboards
from visualization import load_emission_pic, load_input_output, load_submission_pic, combine_pics, combine_pics1, resize_pics
from user_interaction import prepare_input
from predict import predict_class, predict_emission
from leaderboard import load_score, load_score_1
from tensorflow.keras.models import load_model
import cv2


#Big number
inf = 999999

#Initiating
highest_3 = [(0, "NA"), (0, "NA"), (0, "NA")]
worst_3 = [(inf, "NA"), (inf, "NA"), (inf, "NA")]
resize_pics("game_start.png")
resize_pics("hold_navn.png")
resize_pics("cam1.png")
resize_pics("cam2.png")
resize_pics("cam3.png")
game_start = cv2.imread("pictures/temporary_pics/game_start.png")
team_name = cv2.imread("pictures/temporary_pics/hold_navn.png")
first = cv2.imread("pictures/temporary_pics/cam1.png")
second = cv2.imread("pictures/temporary_pics/cam2.png")
thid = cv2.imread("pictures/temporary_pics/cam3.png")

#Loading model
model_best = load_model('best_model_14class.hdf5', compile = False)

def game(input):
    #Preparing input
    food = input[0]
    weights = input[1]
    username = input[2]

    #Make prediction / calculate emission
    predicted_food = predict_class(model_best, food)
    predicted_emission = predict_emission(predicted_food, weights)

    #Load input/output pick
    camera_pics = ["pictures/camera_pics/pic0.png", "pictures/camera_pics/pic1.png", "pictures/camera_pics/pic2.png"]
    load_input_output(camera_pics, predicted_food)

    #Updates scoreboard
    load_score(highest_3, (predicted_emission[0][0], username))
    load_score_1(worst_3, (predicted_emission[0][0], username))

    #Loading emission-picture corresponding to current emission prediction
    load_emission_pic(predicted_emission[0][0])

    #Combining visuals
    load_submission_pic(username, int(predicted_emission[0][0]))
    combine_pics("pictures/temporary_pics/top_3.png", "pictures/temporary_pics/worst_3.png", 0)
    combine_pics("pictures/temporary_pics/team_score.png", "pictures/temporary_pics/emission.png", 1)
    combine_pics1("pictures/temporary_pics/combined0.png", "pictures/temporary_pics/combined1.png")
    
while True:
    # Starting Game
    cv2.imshow('image', game_start)
    cv2.waitKey(1)
    
    #Exit program is char q is given
    key = input("")
    if key == "q":
        break

    #Insert name graphic
    cv2.imshow('image', team_name)
    cv2.waitKey(1)

    #Taking photoes and running game
    user_input = prepare_input()
    game(user_input)

    #Loading prediction picture
    input_output = cv2.imread("pictures/temporary_pics/input_output.png")
    cv2.imshow('image', input_output)
    cv2.waitKey(1)
    key = input("Press enter to see result")
    if key == "q":
        break

    # Show leaderboards
    leaderboard = cv2.imread("pictures/temporary_pics/combined2.png")
    cv2.imshow('image', leaderboard)
    cv2.waitKey(1)
    key = input("Press enter to see play again")
    if key == "q":
        break









    


    
