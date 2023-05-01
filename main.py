from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)
app.secret_key = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
    return render_template("submission.html")

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    depature_delay = float(request.form['DepDelay'])

    unpickled_linear_model = pickle.load(open('linearModel.pkl', 'rb'))
    prediction = unpickled_linear_model.predict([[depature_delay]])

    return render_template('prediction.html', prediction = prediction[0][0])

if __name__ == "__main__":
    app.run(debug=True)