import re
import time
from typing import Callable, Any
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Function to extract CSV data from URL with retries
def extract_csv_from_url(url: str, max_tries: int = 5, sec_wait_before_retry: float = 5) -> pd.DataFrame:
    df = None
    for i in range(1, max_tries + 1):
        try:
            df = pd.read_csv(url, sep=';', decimal=',')
            break
        except:
            print(f"Couldn't extract CSV from the given URL! (Try {i}/{max_tries})")
            if i < max_tries:
                time.sleep(sec_wait_before_retry)
    if df is None:
        raise Exception(f"Failed to extract CSV from the given URL {url}")
    return df

# Function to drop rows with invalid values
def drop_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    valid_verkehr = ['FV', 'RV', 'nur DPN']
    df = df.drop(columns=['Status'])
    df = df.dropna()
    df = df[df['Verkehr'].isin(valid_verkehr)]
    df = df[(df['Laenge'].between(-90, 90)) & (df['Breite'].between(-90, 90))]
    df = df[df['IFOPT'].apply(lambda x: bool(re.match(r'^..:\d+:?\d*$', str(x))))]  # Regex pattern
    return df

# Function to create SQLite database and store DataFrame
def store_to_sqlite(df: pd.DataFrame, db_name: str = 'trainstops.sqlite', table_name: str = 'trainstops'):
    engine = create_engine(f'sqlite:///{db_name}', echo=False)
    df.to_sql(table_name, engine, index=False, if_exists='replace', dtype={
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

# Main execution
if __name__ == '__main__':
    # URL to the CSV file
    DATA_URL = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'

    # Extract DataFrame from the CSV with retries
    df = extract_csv_from_url(DATA_URL)

    # Drop rows with invalid values
    df = drop_invalid_rows(df)

    # Store DataFrame into SQLite database
    store_to_sqlite(df)
