import os
import zipfile
import pandas as pd
import sqlite3
import pytest
from sqlalchemy import create_engine, inspect
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
# Assuming your data loading code is in a separate function or class method

def load_traffic_data():
    # Your code to load traffic data into SQLite database
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('hasibullahaman/traffic-prediction-dataset','Traffic.csv')

    df = pd.read_csv("Traffic.csv")
    df.head()

    Traffic = pd.read_csv('Traffic.csv')
    con = sqlite3.connect('Traffic.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS weather_data ('Time','Date','Day of the week','CarCount','BikeCount','BusCount','TruckCount','Total','Traffic Situation')")
    data_row = df.values.tolist()
    data_to_add = [(d_row[0],d_row[1],d_row[2],d_row[3],d_row[4],d_row[5],d_row[6],d_row[7],d_row[8]) for d_row in data_row]
    cursor.executemany("INSERT INTO weather_data values(?,?,?,?,?,?,?,?,?)", data_to_add)
    con.commit()
    con.close()
    pass

def load_weather_data():
    # Your code to load weather data into SQLite database
    df = pd.read_csv("weatherHistory.csv")
    df.head()

    weather = pd.read_csv('weatherHistory.csv')
    con = sqlite3.connect('weather.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS weather_data ('Formatted Date','Summary','Precip Type','Temperature (C)','Apparent Temperature (C)','Humidity','Wind Speed (km/h)','Wind Bearing (degrees)','Visibility (km)','Loud Cover','Pressure (millibars)','Daily Summary')")
    data_row = df.values.tolist()
    data_to_add = [(d_row[0],d_row[1],d_row[2],d_row[3],d_row[4],d_row[5],d_row[6],d_row[7],d_row[8],d_row[9],d_row[10],d_row[11]) for d_row in data_row]
    cursor.executemany("INSERT INTO weather_data values(?,?,?,?,?,?,?,?,?,?,?,?)", data_to_add)
    con.commit()
    con.close()
    pass

# Test case to check if the tables and data are loaded correctly

def test_data_loading():
    # Load traffic data
    load_traffic_data()

    # Load weather data
    load_weather_data()

    # Connect to the SQLite database and check tables and data
    traffic_db_path = 'Traffic.db'
    weather_db_path = 'weather.db'

    engine_traffic = create_engine(f'sqlite:///{traffic_db_path}')
    engine_weather = create_engine(f'sqlite:///{weather_db_path}')

    inspector_traffic = inspect(engine_traffic)
    inspector_weather = inspect(engine_weather)

    # Check if tables are created
    assert 'weather_data' in inspector_traffic.get_table_names()
    assert 'weather_data' in inspector_weather.get_table_names()

    # Check if tables contain data
    conn_traffic = engine_traffic.connect()
    conn_weather = engine_weather.connect()

    # Check the number of records in traffic_data and weather_data tables
    result_traffic = conn_traffic.execute("SELECT COUNT(*) FROM weather_data").scalar()
    result_weather = conn_weather.execute("SELECT COUNT(*) FROM weather_data").scalar()

    assert result_traffic > 0
    assert result_weather > 0

    # Close connections
    conn_traffic.close()
    conn_weather.close()

# Run the test using pytest
