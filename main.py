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
my_input = [["pics/Supreme_pizza.jpeg", "pics/grilled_cheese.jpeg", "pics/pulled_pork.jpeg"], [80, 100, 120], "Patrick"]
my_input2 = [["pics/seaweed.jpeg", "pics/risotto.jpeg", "pics/caeser.jpeg"], [120, 80, 100], "Kabbas"]
my_input3 = [["pics/tiramisu.jpeg", "pics/waffles.jpeg", "pics/ceviche.jpeg"], [120, 80, 100], "Daniel"]
my_input4 = [["pics/spaghetti-carbonara.jpeg", "pics/omelette.jpg", "pics/apple_pie.jpeg"], [120, 80, 100], "Sadegh"]

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
print(main(my_input3))
print(main(my_input4))
print(highest_3)
print(worst_3)
    


    
