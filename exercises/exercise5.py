import urllib.request
import pandas as pd
from io import BytesIO
from zipfile import ZipFile
from sqlalchemy import create_engine

data_url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
file_name = 'GTFS.zip'
urllib.request.urlretrieve(data_url, file_name)

with ZipFile(file_name,'r') as zip_ref:
    df = pd.read_csv(BytesIO(zip_ref.read('stops.txt')))

stop_data = df[['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id']]
df = df[df['zone_id'] == 2001]

df = df[(df['stop_lat'].between(-90, 90)) & (df['stop_lon'].between(-90, 90))]

engine = create_engine('sqlite:///gtfs.sqlite')

df.to_sql('stops', engine, if_exists='replace', index=False)