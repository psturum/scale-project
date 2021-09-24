from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

#List of classes trained in model
food_list = ['apple_pie','pizza','omelette','caesar_salad','ceviche', 'grilled_cheese_sandwich', 'hamburger','macaroni_and_cheese',
             'pulled_pork_sandwich','risotto','seaweed_salad','spaghetti_carbonara','tiramisu','waffles']

food_list1 = ['Tærte','Pizza','Omelette','Caesar salat','Ceviche', 'Toast', 'Hamburger','Macaroni',
             'Pulled pork','Risotto','Tang salat','Carbonara','Tiramisu','Vafler']

def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2))

#Method for predicting food in images
def predict_class(model, images):
    list = []  
    for img in images:
        img = image.load_img(img, target_size=(299, 299))
        img = image.img_to_array(img)                    
        img = np.expand_dims(img, axis=0)         
        img /= 255.                                    
        pred = model.predict(img)
        index = np.argmax(pred)
        merged_list = listOfTuples(food_list, food_list1)
        merged_list.sort()
        list += [merged_list[index][1]]
    return list

#Method given list of food predictions as input, transforms into emission as output
def predict_emission(list_food, weights):
    emission = 0
    df = pd.read_csv (r'conversion_table.csv',header=0)
    i = 0
    for food in list_food:
        #Using conversion table to get gCO2e per 100g of given food class
        df = pd.read_csv (r'conversion_table.csv',header=0)
        df1 = (df.loc[df['food'] == food])
        emission += df1['emission'].values * weights[i]/100
        i += 1
    return emission, list_food
