# Initializing scoreboards
from predict import predict_class, predict_emission
from leaderboard import load_score, load_score_1
from tensorflow.keras.models import load_model

#Big number
inf = 999999

#Initiate leaderboard
highest_3 = [(0, "NA"), (0, "NA"), (0, "NA")]
worst_3 = [(inf, "NA"), (inf, "NA"), (inf, "NA")]

#Preparing input, should come from external sources(camera, weight)
my_input = [["pics/pizza2.jpeg", "pics/test.jpeg", "pics/pulled_pork.jpeg"], [80, 100, 120], "Patrick"]
my_input2 = [["pics/seaweed.jpeg", "pics/risotto.jpeg", "pics/caeser.jpeg"], [120, 80, 100], "Kabbas"]

#Loading model
model_best = load_model('best_model_14class.hdf5',compile = False)

def main(input):
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

    return predicted_emission

print(main(my_input))
print(main(my_input2))
print(highest_3)
print(worst_3)
    


    
