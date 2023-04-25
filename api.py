from flask import Flask 
app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def returnascii():
    d = {}
    inputchr = str(request.args['query'])
    answer = str(ord(inputchr))
    d['output'] = answer
    return d

@app.route('/predict', methods=['POST'])
def predict():
    lr = joblib.load("model.pkl")
    if lr:
        try:
            json = request.get_json()  
            model_columns = joblib.load("model_cols.pkl")
            temp=list(json[0].values())
            vals=np.array(temp)
            prediction = lr.predict(temp)
            print("here:",prediction)        
            return jsonify({'prediction': str(prediction[0])})
        except:        
            return jsonify({'trace': traceback.format_exc()})
    else:
        return ('No model here to use')



if __name__ =="__main__":
    app.run()