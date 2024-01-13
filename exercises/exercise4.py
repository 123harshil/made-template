import zipfile
import os
from urllib.request import urlretrieve
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import BIGINT, TEXT, FLOAT

# Step 1: Download and unzip data
download_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
zip_file_path = "mowesta-dataset.zip"
extracted_folder = "mowesta-dataset"

# Download ZIP file
urlretrieve(download_url, zip_file_path)

# Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

# Step 2: Read CSV data
csv_file_path = os.path.join(extracted_folder, "data.csv")

# Read CSV with specified separator, handle errors and skip bad lines
try:
    df = pd.read_csv(csv_file_path, sep=';', error_bad_lines=False)
except pd.errors.ParserError as e:
    print(f"Error while parsing CSV: {e}")
    print("You may need to inspect and adjust the file manually.")

# Step 3: Print actual column names
print("Actual column names:", df.columns)

# Manually adjust column names based on the printed names
adjusted_columns = [
    'Geraet', 'Hersteller', 'Model', 'Monat', 'Temperatur in °C (DWD)',
    'Latitude (WGS84)', 'Longitude (WGS84)', 'Verschleierung (m)',
    'Aufenthaltsdauer im Freien (ms)', 'Batterietemperatur in °C',
    'Geraet aktiv'
]

# Step 4: Reshape data
if df is not None:
    df = df[adjusted_columns]

    # Rename columns
    df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"}, inplace=True)

    # Step 5: Discard columns to the right of "Geraet aktiv"
    df = df.loc[:, :"Geraet aktiv"]

    # Step 6: Validate data
    df = df[df["Geraet"] > 0]

    # Step 7: Transform data
    # Step 7: Transform data
# Step 7: Transform data
    df["Temperatur"] = (df["Temperatur"].astype(str).str.replace(',', '.', regex=True).str.split(';', expand=True).astype(float) * 9/5) + 32
    df["Batterietemperatur"] = (df["Batterietemperatur"].astype(str).str.replace(',', '.', regex=True).str.split(';', expand=True).astype(float) * 9/5) + 32



    # Step 8: Write data to SQLite database
    db_engine = create_engine('sqlite:///temperatures.sqlite')
    df.to_sql('temperatures', con=db_engine, index=False, if_exists='replace', dtype={"Geraet": BIGINT, "Hersteller": TEXT, "Model": TEXT, "Monat": BIGINT, "Temperatur": FLOAT, "Batterietemperatur": FLOAT, "Geraet aktiv": TEXT})

    print("Data written to SQLite database successfully.")
