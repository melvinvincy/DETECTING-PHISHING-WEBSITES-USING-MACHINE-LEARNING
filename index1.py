# -*- coding: utf-8 -*-

#importing libraries
import joblib
import inputScript
import whois
from datetime import datetime

#load the pickle file
classifier = joblib.load('final_models/rf_final.pkl')

#input url
print("enter url")
url = input()

#checking and predicting
checkprediction = inputScript.main(url)
prediction = classifier.predict(checkprediction)
print(prediction)
