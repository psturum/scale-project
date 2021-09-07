from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from tensorflow.python.ops.gen_array_ops import where
# import matplotlib.pyplot as plt


#List of classes trained in model
food_list = ['apple_pie','pizza','omelette','caesar_salad','ceviche', 'grilled_cheese_sandwich', 'hamburger','macaroni_and_cheese',
             'pulled_pork_sandwich','risotto','seaweed_salad','spaghetti_carbonara','tiramisu','waffles']
prediction = ""

#Helper function for predicting 
def predict_class(model, image1, show = True):
    img = image.load_img(image1, target_size=(299, 299))
    img = image.img_to_array(img)                    
    img = np.expand_dims(img, axis=0)         
    img /= 255.                                      

    pred = model.predict(img)
    index = np.argmax(pred)
    food_list.sort()
    return food_list[index]
    # print("Tallerkenen indeholder " + food_list[index])
    # if show:
    #     plt.imshow(img[0])                           
    #     plt.axis('off')
    #     plt.title(pred_value)
    #     plt.show()


#Loading model
model_best = load_model('best_model_14class.hdf5',compile = False)
test_image = ('pizza2.jpeg')
prediction = predict_class(model_best, test_image, True)

#Using conversion table to get gCO2e per 100g of given food class
df = pd.read_csv (r'conversion_table.csv',header=0)
df1 = (df.loc[df['food'] == prediction])
emission = df1['emission'].values


print(prediction)
print("Tallerkenen indeholder {}, som udleder {} gCO2 per 100g".format(prediction, emission[0]))