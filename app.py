from wsgiref import simple_server
from flask import Flask, request, app, render_template
from flask import Response
from flask_cors import CORS 
import pickle
import os
import bz2
import numpy as np
import pandas as pd
from joblib import load



app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

#scalerobject=bz2.BZ2File("Model\standardScalar.pkl", "rb")
#scaler=pickle.load(scalerobject)
#modelforpred=bz2.BZ2File("Model\trainedmodelrfc.pkl", "rb")
#model=pickle.load(modelforpred)

#scaler=pickle.load(open("Model\standardScalar.pkl", "rb"))
#model=pickle.load(open("Model\trainedmodelrfc.pkl", "rb"))


try:
    scaler = load("Model/standardScalar.pkl")
    # Use the scaler object
    print("Scaler loaded successfully.")
except Exception as e:
    print(f"Error loading scaler: {e}")
model=pickle.load(open("Model\sfcmodel.pkl", "rb"))


#Route for homepage

@app.route('/')
def index():
    return render_template('home.html')


#Route for Single data point prediction
@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        precipitation=float(request.form.get("precipitation"))
        temp_max=float(request.form.get("temp_max"))
        temp_min=float(request.form.get("temp_min"))
        wind=float(request.form.get("wind"))
        year=str(request.form.get("year"))
        month=str(request.form.get("month"))
        day = str(request.form.get('day'))
        


        new_data=scaler.transform([[precipitation,temp_max,temp_max,wind,str(year),str(month),str(day)]])
        predict=model.predict(new_data)

        if (predict==0):
            result = 'drizzle'
        elif (predict == 1):
            result='rainy'
        elif (predict == 2):
            result='sunny' 
        elif (predict == 3):
            result='snow'
        else:
            result='fogg'


        return render_template('result.html', result=result)

    else:
        return render_template('home.html')



if __name__=="__main__":
    app.run(debug=True)                  



            