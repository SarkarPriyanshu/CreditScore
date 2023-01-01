from flask import Flask,request
from flask_cors import CORS,cross_origin
import pandas as pd
import pickle
import utils.cleaner as cleaner

app = Flask(__name__)
CORS(app)

# Loading the model of XGboostClassifier.
XGBoostClassifier_model = pickle.load(open('Model/XGBoostClassifierPipeline.pkl','rb'))

# Get Info route.
@app.route('/',methods=['GET'])
def home():
    return {
        'resultStatus': 'SUCCESS',
        'message': {
                    'header':"Credit score classification",
                    'summary':'Given a person’s credit-related information, build a machine learning model that.',
                    'content':"""Problem Statement You are working as a data scientist in a global finance company. Over the years, the company has collected basic bank details and gathered a lot of credit-related information. The management wants to build an intelligent system to segregate the people into credit score brackets to reduce the manual efforts.""",
                    }            
        }
# Predict random predictions from dataset.
@app.route('/predict_auto',methods=['POST'])
@cross_origin()
def predict_auto():
    clean = cleaner.Cleaner()
    dataset = pd.read_csv('Data/train.csv')
    data = pd.DataFrame(list([list(clean.handleRandom(dataset)[0]),list(clean.handleRandom(dataset)[1])]),columns=clean.handleRandom(dataset)[0].keys())
    result = XGBoostClassifier_model.predict(data)
    return {'result':str(result[0])}

# Predict user value to credict score.
@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    data = dict(request.json)
    clean = cleaner.Cleaner()
    dataset = pd.read_csv('Data/train.csv')
    data = clean.handleclean(df=dataset,userData=pd.Series(data))
    randomData = clean.handleRandom(dataset) 
    data = pd.DataFrame(list([data,randomData[0]]),columns=randomData[0].keys())
    result = XGBoostClassifier_model.predict(data)
    return {'result':str(result[0])}

if __name__=="__main__":
    app.run(debug=True)
