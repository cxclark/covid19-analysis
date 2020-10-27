from flask import Flask, Response, request, render_template, jsonify
import numpy as np
import pandas as pd
import pickle
import requests
import folium
import json
import branca

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

    url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
    df = pd.read_csv()
    county_data = f'{url}/us_county_data.csv'
    county_geo = f'{url}/us_counties_20m_topo.json'


    df = pd.read_csv(county_data, na_values=[' '])

    colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 50e3)
    employed_series = df.set_index('FIPS_Code')['Employed_2011']


    def style_function(feature):
        employed = employed_series.get(int(feature['id'][-5:]), None)
        return {
        'fillOpacity': 0.5,
        'weight': 0,
        'fillColor': '#black' if employed is None else colorscale(employed)
        }
    
    m_ca = folium.Map(location = [36.17, -119.7462], zoom_start = 6, tiles = 'Stamen Toner')

    folium.TopoJson(
        json.loads(requests.get(county_geo).text),
        'objects.us_counties_20m',
        style_function=style_function
        ).add_to(m_ca)

    return m_ca._repr_html_()

@app.route('/Florida')
def flmap():

    m_fl = folium.Map(location = [27.8333, -81.717], zoom_start = 6, tiles = 'Stamen Toner')

    return m_fl._repr_html_()

@app.route('/Illinois')
def ilmap():

    m_il = folium.Map(location = [40.3363,-89.0022], zoom_start = 6, tiles = 'Stamen Toner')

    return m_il._repr_html_()

@app.route('/New York')
def nymap():

    m_ny = folium.Map(location = [42.1497, -74.9384], zoom_start = 6, tiles = 'Stamen Toner')

    return m_ny._repr_html_()

@app.route('/Texas')
def txmap():

    m_tx = folium.Map(location = [31.1060,-97.6475], zoom_start = 6, tiles = 'Stamen Toner')

    return m_tx._repr_html_()


if __name__ == '__main__':
    app.run(debug = True)
