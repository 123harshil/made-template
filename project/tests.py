import unittest
import logging
import os
import sqlite3
import pandas as pd


class TestData(unittest.TestCase):

    def setUp(self):
        logging.info("setting up the data")
        try:
            # Set up SQLite databases
            self.traffic_db_path = "D:\\made\\traffic.sqlite"
            self.conn1 = sqlite3.connect(self.traffic_db_path)
            self.query1 = f"SELECT * FROM traffic;"
            self.df1 = pd.read_sql_query(self.query1, self.conn1)

            self.weather_db_path = "D:\\made\\weather.sqlite"
            self.conn2 = sqlite3.connect(self.weather_db_path)
            self.query2 = f"SELECT * FROM weather;"
            self.df2 = pd.read_sql_query(self.query2, self.conn2)
        except Exception as e:
            self.fail(f"Failed to set up: {e}")

    def test_traffic_database(self):
        logging.info("Running traffic database...")
        try:
            # Test if the traffic table exists in the database
            cursor = self.conn1.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            self.assertIn('traffic', table_names)
            print("Test passed: traffic table exists in the database.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_weather_database(self):
        logging.info("checking weather database...")
        try:
            # Test if the weather table exists in the database
            cursor = self.conn2.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            self.assertIn('weather', table_names)
            print("Test passed: weather table exists in the database.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_df1(self):
        logging.info("checking df1_dataframe...")
        try:
            # Test if the df1 DataFrame is not empty
            self.assertFalse(self.df1.empty)
            print("Test passed: DataFrame is not empty.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_df2(self):
        logging.info("Running df2 dataframe...")
        try:
            # Test if the df2 DataFrame is not empty
            self.assertFalse(self.df2.empty)
            print("Test passed: DataFrame is not empty.")
        except Exception as e:
            self.fail(f"Test failed: {e}")


if __name__ == '__main__':
    unittest.main()
