import opendatasets as od
import sqlite3
import pandas as pd
import logging

# dataset links
dataset_links = [
  "https://www.kaggle.com/datasets/hasibullahaman/traffic-prediction-dataset", # elon must tweets
  "https://www.kaggle.com/datasets/muthuj7/weather-dataset" # tesla stocks
]

# have to provide kaggle json file to download the .csv files
od.download(dataset_links[0])


# storing the elon must tweets into a sqlite database
traffic_data = './traffic-prediction-dataset/Traffic.csv'
df1 = pd.read_csv(traffic_data)
traffic_db_path = "D:\\made\\traffic.sqlite"
logging.info(f'storing the traffic data into a database under data folder ')
conn = sqlite3.connect(traffic_db_path)
df1.to_sql('traffic', conn, index=False, if_exists='replace')

od.download(dataset_links[1])

# storing the tesla tweets into a sqlite dataase
weather_data = 'weather-dataset/weatherHistory.csv'
df2 = pd.read_csv(weather_data)
conn = sqlite3.connect("D:\\made\\weather.sqlite")
logging.info(f'storing the weather data into a database under data folder ')
df2.to_sql('weather', conn, index=False, if_exists='replace')
# closing the database connection
conn.close()
