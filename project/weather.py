import kaggle
import zipfile
import pandas as pd
import numpy as np
import sqlite3
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.dataset_download_file('muthuj7/weather-dataset','weatherHistory.csv')
with zipfile.ZipFile("weatherHistory.csv.zip","r") as zip_ref:
    zip_ref.extractall()
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
