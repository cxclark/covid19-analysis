from flask import Flask, Response, request, render_template, jsonify
import numpy as np
import pandas as pd
import pickle
import requests
import folium
import json

app = Flask("myApp")

#Home Page
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/California')
def camap():

    df = pd.read_csv('data/ca_counties.csv')
    with open('data/ca-counties2.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['name']
    
    m_ca = folium.Map(location = [36.17, -119.7462], zoom_start = 6)

    choropleth = folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'covid_severity'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_ca)
    
    choropleth.geojson.add_child(folium.features.GeoJsonTooltip(
        ['name', 'Severity', 'Pop', 'Income', 'Insurance', 'Sex', 'Age', 'Test', 'Obesity'],
        aliases = ['County', 'Severity', 'Pop-Den', 'Inc/Capita', 'Insurance', 'Gender: Male', 'Age 45-74', 'Test/100 ppl', 'Obesity Rate'],
        style=('background-color: grey; color: white;'),
        localize=True
        ).add_to(m_ca))

    folium.LayerControl().add_to(m_ca)
    
    return m_ca._repr_html_()

@app.route('/Florida')
def flmap():
    df = pd.read_csv('data/fl_folium.csv')
    with open('data/fl-counties2.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['NAME10']
    
    m_fl = folium.Map(location = [27.8333, -81.717], zoom_start = 6)
    
    choropleth = folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'covid_severity'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_fl)

    choropleth.geojson.add_child(folium.features.GeoJsonTooltip(
        ['NAME10', 'Severity', 'Pop', 'Income', 'Insurance', 'Sex', 'Age', 'Test', 'Obesity'],
        aliases = ['County', 'Severity', 'Pop-Den', 'Inc/Capita', 'Insurance', 'Gender: Male', 'Age 45-74', 'Test/100 ppl', 'Obesity Rate'],
        style=('background-color: grey; color: white;'),
        localize=True
        ).add_to(m_fl))

    folium.LayerControl().add_to(m_fl)
    
    return m_fl._repr_html_()

@app.route('/Illinois')
def ilmap():
    df = pd.read_csv('data/il_counties.csv')
    with open('data/il-counties2.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['name']
    
    m_il = folium.Map(location = [40.3363,-89.0022], zoom_start = 6)
    
    choropleth = folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'covid_severity'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_il)
    
    choropleth.geojson.add_child(folium.features.GeoJsonTooltip(
        ['name', 'Severity', 'Pop', 'Income', 'Insurance', 'Sex', 'Age', 'Test', 'Obesity'],
        aliases = ['County', 'Severity', 'Pop-Den', 'Inc/Capita', 'Insurance', 'Gender: Male', 'Age 45-74', 'Test/100 ppl', 'Obesity Rate'],
        style=('background-color: grey; color: white;'),
        localize=True
        ).add_to(m_il))

    folium.LayerControl().add_to(m_il)
    
    return m_il._repr_html_()

@app.route('/New York')
def nymap():

    df = pd.read_csv('data/ny_folium.csv')
    with open('data/ny-counties2.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['name']
    
    m_ny = folium.Map(location = [42.1497, -74.9384], zoom_start = 6)
    
    choropleth = folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['County', 'covid_severity'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_ny)
    
    choropleth.geojson.add_child(folium.features.GeoJsonTooltip(
        ['name', 'Severity', 'Pop', 'Income', 'Insurance', 'Sex', 'Age', 'Test', 'Obesity'],
        aliases = ['County', 'Severity', 'Pop-Den', 'Inc/Capita', 'Insurance', 'Gender: Male', 'Age 45-74', 'Test/100 ppl', 'Obesity Rate'],
        style=('background-color: grey; color: white;'),
        localize=True
        ).add_to(m_ny))

    folium.LayerControl().add_to(m_ny)
    
    return m_ny._repr_html_()

@app.route('/Texas')
def txmap():
    df = pd.read_csv('data/tx_folium.csv')
    with open('data/tx-counties2.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['COUNTY']
    
    m_tx = folium.Map(location = [31.1060,-97.6475], zoom_start = 6)
    
    choropleth = folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'covid_severity'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_tx)

    choropleth.geojson.add_child(folium.features.GeoJsonTooltip(
        ['COUNTY','Severity', 'Pop', 'Income', 'Insurance', 'Sex', 'Age', 'Test', 'Obesity'],
        aliases = ['County', 'Severity', 'Pop-Den', 'Inc/Capita', 'Insurance', 'Gender: Male', 'Age 45-74', 'Test/100 ppl', 'Obesity Rate'],
        style=('background-color: grey; color: white;'),
        localize=True
        ).add_to(m_tx))
    
    folium.LayerControl().add_to(m_tx)
    
    return m_tx._repr_html_()

@app.route('/Prediction')

def prediction():
    return render_template('prediction.html')

@app.route("/predictor")
def make_predictions():

    # load in the form data from the incoming request
    user_input = request.args

    X_test = np.array(
        [
            float(user_input["inc_per_capita_inc_dol"]),
            (float(user_input["percent_sex_age_pop_45_to_74"])/100),
            (float(user_input["percent_sex_age_pop_male"])/100),
            (float(user_input["percent_health_ins_noninst_pop_cov_yes"])/100),
            float(user_input["pop_density"]),
            (float(user_input["tests_per_100_people"])/100)
        ]
    ).reshape(1, -1)

    model = pickle.load(open("data/model.p", "rb"))
    pred = model.predict(X_test)
    pred = pred[0]

    if pred == 1:
        pred = 'Low'
    elif pred == 2:
        pred = 'Medium'
    elif pred == 3:
        pred = 'High'
    return render_template("results.html", prediction=pred)

if __name__ == '__main__':
    app.run(debug = True)
