from flask import Flask, request, jsonify, render_template
import numpy as np

def calculate(values):
    credits = values[0]+values[2]+values[4]+values[6]+values[8]+values[10]+values[12]+values[14]+values[16]

    GP = ((values[0]*values[1]) + (values[2]*values[3]) + (values[4]*values[5]) + (values[6]*values[7]) + (values[8]*values[9]) + (values[10]*values[11]) + (values[12]*values[13]) + (values[14]*values[15]) + (values[16]*values[17]))

    return (GP/credits)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    prediction = calculate(int_features)
    output = round(prediction, 2)
    return render_template('index.html', prediction_text='Your GPA should be {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)