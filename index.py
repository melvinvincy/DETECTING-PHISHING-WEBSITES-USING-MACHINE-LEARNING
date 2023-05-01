from flask import Flask, request, render_template,redirect
import joblib
import inputScript
import whois
from datetime import datetime

#from imblearn.ensemble import BalancedBaggingClassifier

app = Flask(__name__,template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method=="POST":
        #load the pickle file
        classifier = joblib.load('final_models/rf_final.pkl')

        #input url
        # print("enter url")
        # url = input()
        url = request.form.get("url")

        #checking and predicting
        checkprediction = inputScript.main(url)
        prediction = classifier.predict(checkprediction)
        # print(prediction)
        if prediction==0:
            d="This is a Suspicious URL"
        elif prediction==-1:
            d="This is a Legitimate URL"
            m=url
            return render_template("website.html",d=d,m=m)
        else:
            d="This is a Phishing URL"
           
        return render_template("website.html",d=d)
    return render_template("website.html")




if __name__ == '__main__':
    app.run(debug = True)
