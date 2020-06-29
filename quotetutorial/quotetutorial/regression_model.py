import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy 
import sklearn
import seaborn as sns 
import re 

dataset = pd.read_csv(r"C:\Users\charan\Desktop\NewScraping\quotetutorial\newitem.csv")
dataset.drop(['product_name'],axis=1, inplace = True)
dataset = dataset[['Product_Dimensions','RAM','camera','finalbattery','Storage','price']]
dataset['price'] = dataset['price'].astype(float)
dataset['Product_Dimensions'] = dataset['Product_Dimensions'].astype(float)
dataset['camera'] = dataset['camera'].astype(int)
dataset['finalbattery'] = dataset['finalbattery'].astype(int)
dataset['RAM'] = dataset['RAM'].astype(int)
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1] 
print(x)
print(y)

from sklearn.model_selection import train_test_split
X_train ,X_test ,Y_train,Y_test = train_test_split(x,y, test_size = 0.2,random_state = 0)
print(X_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

y_pred = regressor.predict(X_test)
y_pred

from sklearn.metrics import r2_score
score=r2_score(Y_test,y_pred)

print(score)
