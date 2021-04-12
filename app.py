import numpy as np
from flask import Flask, request, render_template
import joblib
import math

app = Flask(__name__)
model = joblib.load('uber_rides.sav')

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    int_features  = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text="Number of Weekly Rides Should be {}".format(math.floor(output)))

if __name__ == '__main__':
    app.run(debug=True)
