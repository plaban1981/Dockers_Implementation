# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 20:22:01 2021

@author: INTEL
"""
from flask  import Flask,request
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
app = Flask(__name__)
Swagger(app)
pickle_in = open("isolationforest.pkl","rb")
model = pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "Credit Card Fraud Prediction"

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Credit Card Transactions Fraud Predictions 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test = pd.read_csv(request.files.get("file"))
    pred = model.predict(df_test)
    def mapper(x):
        if x == -1:
            return "Anomalus Transaction"
        else:
            return "Normal Transaction"
    predictions = []
    
    for item in pred:
        predictions.append(mapper(item))
    df_test['Predictions'] = predictions
    df_test.to_csv('Predictions.csv',index=False)
    return str(predictions)
          
if __name__=='__main__':
    app.run(host='127.0.0.1',port=8000)
    
