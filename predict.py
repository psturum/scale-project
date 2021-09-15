from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from tensorflow.python.ops.gen_array_ops import where
# import matplotlib.pyplot as plt


#List of classes trained in model
food_list = ['apple_pie','pizza','omelette','caesar_salad','ceviche', 'grilled_cheese_sandwich', 'hamburger','macaroni_and_cheese',
             'pulled_pork_sandwich','risotto','seaweed_salad','spaghetti_carbonara','tiramisu','waffles']

#Method for predicting food
def predict_class(model, images):
    list = []  
    for img in images:
        img = image.load_img(img, target_size=(299, 299))
        img = image.img_to_array(img)                    
        img = np.expand_dims(img, axis=0)         
        img /= 255.                                    
        pred = model.predict(img)
        index = np.argmax(pred)
        food_list.sort()
        list += [food_list[index]]
    return list
    # print("Tallerkenen indeholder " + food_list[index])
    # if show:
    #     plt.imshow(img[0])                           
    #     plt.axis('off')
    #     plt.title(pred_value)
    #     plt.show()


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

