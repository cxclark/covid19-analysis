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
    return render_template('form.html')

@app.route('/California')
def camap():

    df = pd.read_csv('data/ca_folium.csv')
    with open('data/california-counties.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['name']
    
    m_ca = folium.Map(location = [36.17, -119.7462], zoom_start = 6)
    
    folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'death_rate'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_ca)
    
    folium.LayerControl().add_to(m_ca)
    
    return m_ca._repr_html_()

@app.route('/Florida')
def flmap():
    df = pd.read_csv('data/fl_folium.csv')
    with open('data/tl_2010_12_county10.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['NAME10']
    
    m_fl = folium.Map(location = [27.8333, -81.717], zoom_start = 6)
    
    folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'death_rate'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_fl)
    
    folium.LayerControl().add_to(m_fl)
    
    return m_fl._repr_html_()

@app.route('/Illinois')
def ilmap():
    df = pd.read_csv('data/il_folium.csv')
    with open('data/illinois-counties.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['name']
    
    m_il = folium.Map(location = [40.3363,-89.0022], zoom_start = 6)
    
    folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'death_rate'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_il)
    
    folium.LayerControl().add_to(m_il)
    
    return m_il._repr_html_()

@app.route('/New York')
def nymap():

    df = pd.read_csv('data/ny_folium.csv')
    with open('data/new-york-counties.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['name']
    
    m_ny = folium.Map(location = [42.1497, -74.9384], zoom_start = 6)
    
    folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['County', 'death_rate'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_ny)
    
    folium.LayerControl().add_to(m_ny)
    
    return m_ny._repr_html_()

@app.route('/Texas')
def txmap():
    df = pd.read_csv('data/tx_folium.csv')
    with open('data/tx_counties.geojson') as f:
        json_counties = json.load(f)
    
    for i in json_counties['features']:
        i['id'] = i['properties']['COUNTY']
    
    m_tx = folium.Map(location = [31.1060,-97.6475], zoom_start = 6)
    
    folium.Choropleth(
        geo_data = json_counties,
        name = 'choropleth',
        data = df,
        columns = ['county', 'death_rate'],
        key_on = 'feature.id',
        fill_color = "Reds",
        fill_opacity = .6,
        line_opacity = .5,
        legend_name = 'Death Rate',
        highlight = True
        ).add_to(m_tx)
    
    folium.LayerControl().add_to(m_tx)
    
    return m_tx._repr_html_()

if __name__ == '__main__':
    app.run(debug = True)
