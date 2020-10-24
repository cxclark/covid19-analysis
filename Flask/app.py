from flask import Flask, Response, request, render_template, jsonify
import numpy as np
import pickle

app = Flask("myApp")

#Home Page
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit')

def make_prediction():
    user_input = request.args

    data = [
        int(user_input['Input']),
        int(user_input['Input']),
        int(user_input['Input']),
        int(user_input['Input']),
    ]
    #Changing the inputs into array to use for prediction
    #X_test = np.array([
     #   int(user_input['Input']),
      #  int(user_input['Input']),
       # int(user_input['Input']),
        #int(user_input['Input']),
    #]).reshape(1, -1)

    #Insert the model
    #model = pickle.load(open('data/model.p', 'rb'))
    #pred = model.predict(X_test)
    #pred = pred[0]

    return jsonify({'data': data})
    #return render_template('result.html', prediction = pred)

if __name__ == '__main__':
    app.run(debug = True)
