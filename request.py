import requests

cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

url = "http://127.0.0.1:5000/predict_api"

r = requests.post(url, json={"Gender":"Male", 
                            "Married": "Yes", 
                            "Dependents": "0", 
                            "Education": "Graduate", 
                            "Self_Employed": "Yes", 
                            "ApplicantIncome": 5849, 
                            "CoapplicantIncome": 0, 
                            "LoanAmount": 128, 
                            "Loan_Amount_Term": 360, 
                            "Credit_History": 1, 
                            "Property_Area": "Rural"})


                        

print(r.text)