import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model1.sav', 'rb'))


cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    

    ls = []
    features = [x for x in request.form.values()]
    for i in range(len(features)):
        if i in [5,6,7,8,9]:
            ls.append(int(features[i]))
        else:
            ls.append(features[i])

    df = pd.DataFrame([ls], columns=cols)
    prediction =model.predict_proba(df)

    
    if prediction[0].argmax() == 0:
        output = f'There is a {round(prediction[0][prediction[0].argmax()]*100, 1)}% chance that your loan application will be REJECTED'
    else:
        output = f'There is a {round(prediction[0][prediction[0].argmax()]*100, 1)}% chance that your loan application will be APPROVED'


    return render_template('index.html', prediction_text=output)

@app.route('/predict_api',methods=['POST'])
def predict_api():

    data = request.get_json(force=True)
    df = pd.DataFrame([data.values()], columns=cols)

    prediction =model.predict_proba(df)
    if prediction[0].argmax() == 0:
        output = f'There is a {round(prediction[0][prediction[0].argmax()]*100, 1)}% chance that your loan application will be REJECTED'
    else:
        output = f'There is a {round(prediction[0][prediction[0].argmax()]*100, 1)}% chance that your loan application will be APPROVED'

    return output

   
    

    # data = request.get_json(force=True)
    # prediction = model.predict([np.array(list(data.values()))])

    # output = prediction[0]
    # return jsonify(output)



if __name__ == "__main__":
    app.run(debug=True)
    
    