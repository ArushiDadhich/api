from flask import Flask, request, jsonify
import joblib
import numpy as np


app = Flask(__name__)
# Load the machine learning model
model = joblib.load('model.pkl')

# @app.route('/predict', methods = ['GET'])
# def go_home():
#     return "Hello"

#Define a route for the API
@app.route('/', methods=['POST','GET'])
def check():
    print('I am Alive')
@app.route('/predict', methods=['POST','GET'])
def predict():
    # Get the data from the request
    data = request.get_json()
    #data = 
    # Convert the data to a numpy array
    data_array = model.predict([np.array(list(data.values()))])

    #data_array = np.array([data['N'], data['P'], data['K'], data['temperature'], data['humidity'], data['ph'], data['rainfall']])

    # Reshape the data to match the model's input shape
    data_reshaped = data_array.reshape(1, -1)

    # Make a prediction with the model
    prediction = model.predict(data_reshaped)

    # Get the crop name from the prediction
    #crop_name = ['rice', 'wheat', 'maize', 'barley', 'oats'][prediction[0]]
    crop_name = prediction[0]
    # Return the prediction as JSON
    return jsonify({'crop_recommendation': crop_name})





if __name__ == '__main__':
    app.run(debug=True)
