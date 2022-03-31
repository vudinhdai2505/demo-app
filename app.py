#Import main library
import numpy as np
import math

#Import Flask modules
from flask import Flask, request, render_template

#Import pickle to save our regression model
import pickle

#Initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder = 'templates')

#Open our model
model = pickle.load(open('model.pkl','rb'))

#create our "home" route using the "index.html" page
@app.route('/')
def home():
    return render_template('index.html')

#Set a post method to yield predictions on page
@app.route('/', methods = ['POST'])
def predict():

    #obtain all form values and place them in an array, convert into integers
    int_features = [int(x) for x in request.form.values()]
    #Combine them all into a final numpy array
    final_features = [np.array(int_features)]
    #predict the price given the values inputted by user
    prediction = model.predict(final_features)

    #Round the output to 2 decimal places
    output = round(prediction[0], 2)

    #If the output is negative, the values entered are unreasonable to the context of the application
    #If the output is greater than 0, return prediction
    if output < 0:
        return render_template('index.html', prediction_text = "Predicted Price is negative, values entered not reasonable")
    elif output >= 0:
        return render_template('index.html', prediction_text = 'Predicted Price of the house is: ${}'.format(output))

@app.route('/test')
def test():
    a = int(math.pow(6,6))
    result = 0
    for i in range(a):
        result += math.atan(i) * math.tan(i)
    int_features = [79545, 6, 7, 7, 23086]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    # If the output is negative, the values entered are unreasonable to the context of the application
    # If the output is greater than 0, return prediction
    if output < 0:
        return render_template('index2.html',
                               prediction_text="Predicted Price is negative, values entered not reasonable")
    elif output >= 0:
        return render_template('index2.html', prediction_text='Predicted Price of the house is: ${}'.format(output))
#Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
