from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Load the machine learning model
model = joblib.load('model.pkl')

# @app.route('/predict', methods = ['GET'])
# def go_home():
#     return "Hello"

#Define a route for the API
@app.route('/')
def check():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    # data = request.get_json()
    result = request.form
      
    stuff = result.getlist("key")
    clean_stuff = [int(numeric_string) for numeric_string in stuff]
    ls = [clean_stuff]
    #data = 
    print(ls)
    # Convert the data to a numpy array
    data_array = model.predict(ls)
    print(data_array)
    # Get the crop name from the prediction
    #crop_name = ['rice', 'wheat', 'maize', 'barley', 'oats'][prediction[0]]
    crop_name = data_array[0]
    # Return the prediction as JSON
    return jsonify({'crop_recommendation': crop_name})





if __name__ == '__main__':
    app.run(debug=True)
