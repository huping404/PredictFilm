# coding:utf-8
import pandas as pd
from sklearn import datasets,linear_model

def get_data(file_name):
    data = pd.read_csv(file_name)
    flash_x = []
    flash_y = []
    arrow_x = []
    arrow_y = []
    for x1,y1,x2,y2 in zip(data['flash_episode_number'], data['flash_viewers'],
                           data['arrow_episode_number'], data['arrow_viewers']):
        flash_x.append([float(x1)])
        flash_y.append(float(y1))
        arrow_x.append([float(x2)])
        arrow_y.append(float(y2))
    return flash_x,flash_y,arrow_x,arrow_y


# function to predict which Tv show will have more viewers
def more_viewers(x1, y1, x2, y2, predict_value):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1, y1)
    predict_value1 = regr1.predict(predict_value) # the episode_number 9
    print predict_value1

    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)
    predict_value2 = regr2.predict(predict_value)
    print predict_value2

    if predict_value1 > predict_value2:
        print "flash > arrow"
    else :
        print "flash < arrow"


x1,y1,x2,y2 = get_data('input_data.csv')
predict_value = 21
more_viewers(x1, y1, x2, y2, predict_value)
