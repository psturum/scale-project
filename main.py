# Initializing scoreboards
from predict import predict_class, predict_emission
from leaderboard import load_score, load_score_1
from tensorflow.keras.models import load_model

#Big number
inf = 999999

highest_3 = [(0, "NA"), (0, "NA"), (0, "NA")]
worst_3 = [(inf, "NA"), (inf, "NA"), (inf, "NA")]

my_input = [["pizza2.jpeg", "test.jpeg", "pulled_pork.jpeg"], [80, 100, 120], "Patrick"]

#Loading model
model_best = load_model('best_model_14class.hdf5',compile = False)

def main(input):
    #Preparing input
    food = my_input[0]
    weights = my_input[1]
    username = my_input[2]

    #Make prediction / calculate emission
    predicted_food = predict_class(model_best, food)
    predicted_emission = predict_emission(predicted_food, weights)

    #Updates scoreboard
    load_score(highest_3, (predicted_emission[0], username))
    load_score_1(worst_3, (predicted_emission[0], username))

    return predicted_emission

print(main(my_input))
print(highest_3)
print(worst_3)
    


    
