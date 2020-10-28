from flask import Flask, Response, request, render_template, jsonify
import numpy as np
import pickle

app = Flask("myApp")

#Home Page
@app.route('/')
def home():
    return render_template('form2.html')

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

@app.route('/California')

def camap():
    import numpy as np
    import pandas as pd
    import folium
    import json

    m_ca = folium.Map(location = [36.17, -119.7462], zoom_start = 6, tiles = 'Stamen Toner')

    return m_ca._repr_html_()

@app.route('/Florida')
def flmap():
    import numpy as np
    import pandas as pd
    import folium
    import json

    m_fl = folium.Map(location = [27.8333, -81.717], zoom_start = 6, tiles = 'Stamen Toner')

    return m_fl._repr_html_()

@app.route('/Illinois')
def ilmap():
    import numpy as np
    import pandas as pd
    import folium
    import json

    m_il = folium.Map(location = [40.3363,-89.0022], zoom_start = 6, tiles = 'Stamen Toner')

    return m_il._repr_html_()

@app.route('/New York')
def nymap():
    import numpy as np
    import pandas as pd
    import folium
    import json

    m_ny = folium.Map(location = [42.1497, -74.9384], zoom_start = 6, tiles = 'Stamen Toner')

    return m_ny._repr_html_()

@app.route('/Texas')
def txmap():
    import numpy as np
    import pandas as pd
    import folium
    import json

    m_tx = folium.Map(location = [31.1060,-97.6475], zoom_start = 6, tiles = 'Stamen Toner')

    return m_tx._repr_html_()


if __name__ == '__main__':
    app.run(debug = True)
