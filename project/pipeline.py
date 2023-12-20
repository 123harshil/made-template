import kaggle
import zipfile
import pandas as pd
import numpy as np
import sqlite3

def download_traffic_data():
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('hasibullahaman/traffic-prediction-dataset', 'Traffic.csv')

def create_traffic_table():
    con = sqlite3.connect('Traffic.db')
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS traffic_data ('Time','Date','Day of the week','CarCount','BikeCount','BusCount','TruckCount','Total','Traffic Situation')")

    return con, cursor

def insert_traffic_data(con, cursor):
    df = pd.read_csv("Traffic.csv")
    data_row = df.values.tolist()
    data_to_add = [(d_row[0],d_row[1],d_row[2],d_row[3],d_row[4],d_row[5],d_row[6],d_row[7],d_row[8]) for d_row in data_row]
    cursor.executemany("INSERT INTO traffic_data VALUES(?,?,?,?,?,?,?,?,?)", data_to_add)
    con.commit()
    con.close()

def create_weather_table():
    con = sqlite3.connect('weather.db')
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS weather_data ('Formatted Date','Summary','Precip Type','Temperature (C)','Apparent Temperature (C)','Humidity','Wind Speed (km/h)','Wind Bearing (degrees)','Visibility (km)','Loud Cover','Pressure (millibars)','Daily Summary')")

    return con, cursor

def insert_weather_data(con, cursor):
    df = pd.read_csv("weather.csv")
    data_row = df.values.tolist()
    data_to_add = [(d_row[0],d_row[1],d_row[2],d_row[3],d_row[4],d_row[5],d_row[6],d_row[7],d_row[8],d_row[9],d_row[10],d_row[11]) for d_row in data_row]
    cursor.executemany("INSERT INTO weather_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", data_to_add)
    con.commit()
    con.close()

def main():
    download_traffic_data()

    traffic_con, traffic_cursor = create_traffic_table()
    insert_traffic_data(traffic_con, traffic_cursor)

    weather_con, weather_cursor = create_weather_table()
    insert_weather_data(weather_con, weather_cursor)

if __name__ == "__main__":
    main()
