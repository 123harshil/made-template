import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Read the CSV data
url = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'
df = pd.read_csv(url, sep=';', decimal=',')

# Drop the "Status" column
df = df.drop(columns=['Status'])

# Data cleaning: Filter rows with valid values
valid_verkehr = ['FV', 'RV', 'nur DPN']
valid_range = (-90, 90)

# Filter out rows with missing values in the 'IFOPT' column
df = df.dropna(subset=['IFOPT'])

# Apply filtering conditions
valid_verkehr_mask = df['Verkehr'].isin(valid_verkehr)
valid_range_mask = df['Laenge'].between(*valid_range) & df['Breite'].between(*valid_range)
valid_ifopt_mask = df['IFOPT'].str.match(r'^..:[0-9]+:[0-9]+(:[0-9]+)?$')

# Apply masks
df = df[valid_verkehr_mask & valid_range_mask & valid_ifopt_mask]

# Connect to SQLite database
engine = create_engine('sqlite:///trainstops.sqlite', echo=False)

# Define the table structure and data types
table_name = 'trainstops'
df.to_sql(table_name, engine, if_exists='replace', index=False, dtype={
    "EVA_NR": sqlalchemy.BIGINT,
    "DS100": sqlalchemy.TEXT,
    "IFOPT": sqlalchemy.TEXT,
    "NAME": sqlalchemy.TEXT,
    "Verkehr": sqlalchemy.TEXT,
    "Laenge": sqlalchemy.FLOAT,
    "Breite": sqlalchemy.FLOAT,
    "Betreiber_Name": sqlalchemy.TEXT,
    "Betreiber_Nr": sqlalchemy.BIGINT
})