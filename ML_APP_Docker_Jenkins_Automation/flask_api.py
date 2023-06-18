# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 13:53:00 2023
@author: Bala Senapathi
"""

from flask import Flask, request
import numpy 
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in, encoding="latin1")


@app.route('/')
def welcome():
    return "Welcome All"


@app.route('/predict', methods=["GET"])
def predict_note_authentication():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    variance = float(request.args.get("variance"))
    skewness = float(request.args.get("skewness"))
    curtosis = float(request.args.get("curtosis"))
    entropy = float(request.args.get("entropy"))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "Hello, the answer is " + str(prediction)


@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note
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
    print(df_test.head())
    prediction = classifier.predict(df_test)

    return str(list(prediction))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
