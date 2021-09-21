# Initializing scoreboards
from visualization import load_emission_pic, load_submission_pic, combine_pics, combine_pics1
from user_interaction import prepare_input
from numpy.core.numeric import False_
from predict import predict_class, predict_emission
from leaderboard import load_score, load_score_1
from tensorflow.keras.models import load_model
from PIL import Image

#Big number
inf = 999999

#Initiate leaderboard
highest_3 = [(0, "NA"), (0, "NA"), (0, "NA")]
worst_3 = [(inf, "NA"), (inf, "NA"), (inf, "NA")]

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

    #Updates scoreboard
    load_score(highest_3, (predicted_emission[0][0], username))
    load_score_1(worst_3, (predicted_emission[0][0], username))

    #Loading emission-picture corresponding to current emission prediction
    load_emission_pic(predicted_emission[0][0])
    print(predicted_emission[0][0])

    #Combining visuals
    load_submission_pic(username, int(predicted_emission[0][0]))
    combine_pics("temporary_pics/top_3.png", "temporary_pics/worst_3.png", 0)
    combine_pics("temporary_pics/team_score.png", "temporary_pics/emission.png", 1)
    combine_pics1("temporary_pics/combined0.png", "temporary_pics/combined1.png")
    print(predicted_food)
    

while True:
    # Initiating game
    input("Press enter to play")
    user_input = prepare_input()
    game(user_input)

    # Show visualization
    visuals = Image.open("temporary_pics/combined2.png")
    visuals.show()







    


    
