from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('KNN_Model_gridserchCV.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Age=request.form['Age']
        Sex=request.form['Sex']
        if(Sex=='Male'):
            Sex=1
        else:
            Sex=0
        OnThyroxine=request.form['OnThyroxine']
        if(OnThyroxine=='Yes'):
            OnThyroxine=1
        else:
            OnThyroxine=0
        QueryOnThyroxine=request.form['QueryOnThyroxine']
        if(QueryOnThyroxine=='Yes'):
            QueryOnThyroxine=1
        else:
            QueryOnThyroxine=0
        OnAntiThyroidMedication=request.form['OnAntiThyroidMedication']
        if(OnAntiThyroidMedication=='Yes'):
            OnAntiThyroidMedication=1
        else:
            OnAntiThyroidMedication=0
        Sick=request.form['Sick']#np.log(Kms_Driven)
        if(Sick=='Yes'):
            Sick=1
        else:
            Sick=0
        Pregnant=request.form['Pregnant']
        if(Pregnant=='Yes'):
            Pregnant=1
        else:
            Pregnant=0
        ThyroidSurgery=request.form['ThyroidSurgery']
        if(ThyroidSurgery=='Yes'):
            ThyroidSurgery=1
        else:
            ThyroidSurgery=0
        I131_Treatment=request.form['I131']
        if(I131_Treatment=='Yes'):
            I131_Treatment=1
        else:
            I131_Treatment=0
        QueryHypothyroid=request.form['QueryHypothyroid']
        if(QueryHypothyroid=='Yes'):
            QueryHypothyroid=1
        else:
            QueryHypothyroid=0
        QueryHyperthyroid=request.form['QueryHyperthyroid']
        if(QueryHypothyroid=='Yes'):
            QueryHyperthyroid=1
        else:
            QueryHyperthyroid=0
        Lithium=request.form['Lithium']
        if(Lithium=='Yes'):
            Lithium=1
        else:
            Lithium=0
        Goitre=request.form['Goitre']
        if(Goitre=='Yes'):
            Goitre=1
        else:
            Goitre=0
        Tumor=request.form['Tumor']
        if(Tumor=='Yes'):
            Tumor=1
        else:
            Tumor=0
        Hypopituritory=request.form['Hypopituritory']
        if(Hypopituritory=='Yes'):
            Hypopituritory=1
        else:
            Hypopituritory=0
        Psych=request.form['Psych']
        if(Psych=='Yes'):
            Psych=1
        else:
            Psych=0
        T3=float(request.form['T3'])
        T4U=float(request.form['T4U'])
        ReferralSourceOther=float(request.form['ReferralSourceOther'])
        prediction=model.predict([[Age,Sex,OnThyroxine,QueryOnThyroxine,OnAntiThyroidMedication,Sick,Pregnant,ThyroidSurgery,I131_Treatment,QueryHypothyroid, QueryHyperthyroid,Lithium,Goitre,Tumor,Hypopituritory,Psych,T3,T4U,ReferralSourceOther]])
        print(prediction)
        output=round(prediction[0],2)
        print(output)
        if output==0:
            return  render_template('index.html',prediction_texts="Not having Thyroid")
        elif output==1:
            return  render_template('index.html',prediction_texts="Having Compensated Hypothyroid")
        elif output==2:
            return  render_template('index.html',prediction_texts="Having Primary Hypothyroid")
        else:
            return  render_template('index.html',prediction_texts="Having Secondary Hypothyroid")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
