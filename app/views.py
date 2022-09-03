from this import d
from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def home(request):

    return render(request, 'home.html')

def prediction(request):

    return render(request, 'prediction.html')

def prediction_result(request):
    data = pd.read_csv(r"C:\Users\aboub\Desktop\IT\ML projects\house price prediction\app\USA_housing.csv")
    data = data.drop(['Address'],axis=1)
    x = data.drop(['Price'],axis=1)
    y = data['Price']
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.30)
    model = LinearRegression()
    model.fit(x_train,y_train)
    prediction = model.predict([[79248.642455,6.002900,6.730821,3.09,40173.072174]])

    var1 = float(request.GET['v1'])
    var2 = float(request.GET['v2'])
    var3 = float(request.GET['v3'])
    var4 = float(request.GET['v4'])
    var5 = float(request.GET['v5'])

    predict = model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
    predict = round(predict[0])
    price = f"The predicted price is {str(predict)}$"

    context = {
        'result':price
    }
    return render(request, 'prediction.html',context)