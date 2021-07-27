# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 19:24:29 2021

@author: INTEL
"""
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

data = pd.read_csv("creditcard.csv")
print(data.head())
#
X = data.drop('Class',axis=1)
Y = data['Class']
train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
model = IsolationForest(n_estimators=100, max_samples='auto', 
                                       contamination=0.2,
                                       random_state=42, 
                                       verbose=0)
model.fit(X)
print(model.get_params())
data['scores'] = model.decision_function(X)
data['anomaly_score'] = model.predict(X)
print('Anomalous Data')
print(data[data['anomaly_score'] == -1].head())
df_anom = data[data['Class'] == 1 and data['anomaly_score']]
#model evaluation
accuracy = 100 * list(data['anomaly_score']).count(-1)/(data.shape[0])
print(f'accuracy of the model : {accuracy} %')
