from flask import Flask,request, render_template
import pickle
import numpy as np

model=pickle.load(open('email_classifier.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    email=[x for x in request.form.values()]
    final=email
    prediction=model.predict(final)
    #output='{0:.{1}f}'.format(prediction[0][1], 2)

    if int(prediction)==1:
        return render_template('index.html',pred='The Email has a more probablity of being a Spam.',email_text = email[0])
    else:
        return render_template('index.html',pred='The Email has a less probablity of being a Spam.',email_text = email[0])


if __name__ == '__main__':
    app.run(debug=True)
