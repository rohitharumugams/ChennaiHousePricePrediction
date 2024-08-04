import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
data = pd.read_csv('Final_Chennai_House_Data.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))



@app.route('/')
def index():

    area = sorted(data['area'].unique())
    return render_template('index.html', area = area)


@app.route('/predict', methods = ['POST'])
def predict():
    areas = request.form.get('areas')
    bedrooms = request.form.get('bedrooms')
    bathrooms = request.form.get('bathrooms')
    area_sqft = request.form.get('area_sqft')

    print(areas, bedrooms, bathrooms, area_sqft)
    input = pd.DataFrame([[areas, area_sqft, bathrooms, bedrooms]], columns = ['area', 'area_sqft', 'bathrooms', 'bedrooms'])
    prediction = pipe.predict(input)[0]

    return str(np.round(prediction, 2))

if __name__ == "__main__":
    app.run(debug = True, port = 5001)